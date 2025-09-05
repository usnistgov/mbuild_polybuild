"""Toolbox Module

This module contains helper functions for forming molecules, generating sequences, and applying forcefield parameters.

Functions
---------
- _import_pdb: Retrieve the file path of a PDB file distributed with mbuild-polybuild.
- atom2port: Replace specific atom types with ports in a given trajectory.
- random_sequence: Generate a random copolymer sequence.
- apply_nbfix: Apply non-bonded interaction fixes to a structure using parameters from a file.
"""

import os
import json
import numpy as np
from collections import OrderedDict

import mbuild as mb
from foyer.utils.nbfixes import apply_nbfix as foyer_apply_nbfix

import mbuild_polybuild


def _import_pdb(filename):
    """
    Retrieve the file path of a PDB file distributed with mbuild-polybuild.

    Parameters
    ----------
    filename : str
        Filename of the desired molecular structure.

    Returns
    -------
    str
        Full file path to the PDB file.

    Examples
    --------
    >>> path = _import_pdb("amide.pdb")
    >>> print(path)
    "/path/to/_pdb_files/amide.pdb"
    """

    return os.path.join(mbuild_polybuild.__file__[:-12], "_pdb_files", filename)


def atom2port(Obj, atom_type="NO"):
    """
    Replace specific atom types with ports in the given trajectory.

    Parameters
    ----------
    Obj : mb.Compound
        The compound instance for which to create ports.
    atom_type : str, optional, default="NO"
        Atom type to be replaced with a port. Comparison is case-insensitive.

    Examples
    --------
    >>> from mbuild import Compound
    >>> compound = Compound()
    >>> atom2port(compound, atom_type="H")
    """

    atom_type = atom_type.lower()

    # Remove unwanted bond to produce ports
    flag_found = False
    for bond in list(Obj.bonds()):
        flag = False
        for tmp in bond:
            if tmp.name.lower() == atom_type:
                flag = True
        if flag:
            flag_found = True
            Obj.remove_bond(bond)

    if flag_found:
        # Remove unwanted ports and atoms
        remove_array = []
        for child in Obj.children:
            if isinstance(child, mb.port.Port):
                if child.anchor.name.lower() == atom_type:
                    remove_array.append(child)
                else:
                    pass
            else:
                if child.name.lower() == atom_type:
                    remove_array.append(child)
        Obj.remove(
            remove_array,
            # reset_labels=True
        )
        new_labels = OrderedDict()
        for child in Obj.children:
            if "Port" in child.name:
                label = [key for key, x in Obj.labels.items() if id(x) == id(child)][0]
                if "port" in label:
                    label = "{0}[$]".format("port")
            else:
                label = "{0}[$]".format(child.name)

            if label.endswith("[$]"):
                label = label[:-3]
                if label not in new_labels:
                    new_labels[label] = []
                label_pattern = label + "[{}]"

                count = len(new_labels[label])
                new_labels[label].append(child)
                label = label_pattern.format(count)
            new_labels[label] = child
        Obj.labels = new_labels


def random_sequence(Ncopolymers, Nmonomers):
    """
    Generate a random copolymer sequence.

    Parameters
    ----------
    Ncopolymers : int
        Number of distinct copolymers.
    Nmonomers : int
        Number of monomers in the chain.

    Returns
    -------
    str
        A string representing the random copolymer sequence.

    Examples
    --------
    >>> sequence = random_sequence(3, 10)
    >>> print(sequence)
    "ABACABCBAC"
    """

    copolymer_options = "ABCDEFGHIJK"
    cut_off = 1 / Ncopolymers

    Rng = np.random.default_rng()
    tmp = Rng.random((Nmonomers,))
    sequence_numbers = tmp // cut_off
    sequence_letters = "".join([copolymer_options[int(x)] for x in sequence_numbers])

    return sequence_letters


def apply_nbfix(structure, filename, filetype="json", units="real"):
    """
    Apply non-bonded interaction fixes to a structure using parameters from a file.

    Parameters
    ----------
    structure : mb.Compound
        The structure object with a forcefield already applied.
    filename : str
        Name of the file containing parameters.
    filetype : str, optional, default="json"
        File type to import (e.g., "json").
    units : str, optional, default="real"
        Unit system for parameters. "real" converts between kcal/mol and angstroms.

    Returns
    -------
    mb.Compound
        The input structure with updated parameters.

    Examples
    --------
    >>> from mbuild import Compound
    >>> structure = Compound()
    >>> updated_structure = apply_nbfix(structure, "params.json")
    """

    if units is None or units == "lj":
        convert_epsilon = 1.0
        convert_sigma = 1.0
    elif units == "real":
        convert_epsilon = 1 / 4.184  # Convert from kJ/mol to kcal/mol
        convert_sigma = 10  # Convert from nm to angstroms
    else:
        raise ValueError("`units` can be 'real', 'lj', or None.")

    if filetype == "json":
        if os.path.isfile(filename):
            with open(filename, "r") as f:
                output = f.read()
            data_dict = json.loads(output)
        else:
            raise ImportError("File, {}, does not exist.".format(filename))

    types = list(set([atom.type for atom in structure.atoms]))

    for name1, tmp_dict in data_dict.items():
        if name1 in types:
            for name2, param_dict in tmp_dict.items():
                if name2 in types:
                    structure = foyer_apply_nbfix(
                        struct=structure,
                        atom_type1=name1,
                        atom_type2=name2,
                        sigma=param_dict["sigma"] * convert_sigma,
                        epsilon=param_dict["epsilon"] * convert_epsilon,
                    )

    return structure
