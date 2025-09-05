"""
This module provides all-atom complete molecules.

These molecules are fully defined and can be used directly in molecular simulations.

Available Molecules
-------------------
- `MonatomicIon`: A monatomic ion.

Examples
--------
>>> from mbuild_polybuild.aa_molecules import MonatomicIon
>>> ion = MonatomicIon(element="Na")
>>> ion.save("monatomic_ion.mol2", overwrite=True)
"""

from mbuild_polybuild.aa_molecules.ion import MonatomicIon as MonatomicIon
