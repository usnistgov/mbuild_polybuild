"""
This module provides all-atom fragments that are not classified as functional groups.

These fragments are designed for use in molecular simulations and can be combined
with other components to build complex molecular systems.

Available Fragments
-------------------
- `C`: A quaternary carbon moiety.

Examples
--------
>>> from mbuild_polybuild.aa_fragments import C
>>> c = C()
>>> c.save("c_quaternary.mol2", overwrite=True)
"""

from mbuild_polybuild.aa_fragments.c_quaternary import C as C
