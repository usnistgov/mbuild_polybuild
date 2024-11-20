"""Contains helper functions for forming molecules"""

import os
import json
import numpy as np
from collections import OrderedDict

import mbuild as mb
from foyer.utils.nbfixes import apply_nbfix as foyer_apply_nbfix

import mbuild_polybuild


def _import_pdb(filename):
    """Export file object from pdb files distributed with mbuild-polybuild.

    Parameters
    ----------
    filename : str
        Filename of desired molecular structure.

    Returns
    -------
    File path
    """

    return os.path.join(mbuild_polybuild.__file__[:-12], "_pdb_files", filename)


def atom2port(Obj, atom_type="NO"):
    """
    This function serves to easily create ports in the desired trajectory, by replacing
    a certain atom type with a port in the direction it was pointing.

    Parameters
    ----------
    Obj : obj
        This is the instance for which to create ports.
    atom_type : str, Optional, default="NO"
        This atom type will be removed from the Compound and a port along the trajectory
        of the bond will remain. The default value is the obscure atom, Nobelium. This
        comparison is not case sensitive.

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
    Generate copolymer sequence

    Parameters
    ----------
    Ncopolymers : int
        Number of copolymers
    Nmonomers : number of monomers in the chain
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
    Recursively use the 'apply_nbfix' function to a structure instance using parameters from a .json file.

    Parameters
    ----------
    structure : obj
        Structure object with a forcefield already applied
    filename : str
        Name of the file containing parameters of type "filetype"
    filetype : str, Optional, default="json"
        File type to import
    units : str, Optional, default="real"
        Flag to signal unit conversions. Although foyers normal parameter files expect energy units of kcal/mol and distance units of angstroms, the foyer function ``apply_nbfix`` expects kJ/mol and nm respectively. Thus, the flag "real" will convert between the two. If ``units=None`` then no units conversion is applied.

    Returns
    -------
    structure : obj
        Same input structure with updated parameters.
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
