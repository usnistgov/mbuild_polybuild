"""Acrylamide moiety."""

import mbuild as mb

from mbuild_polybuild.aa_monomers.acrylamide import Acrylamide
from mbuild_polybuild.aa_functional_groups.ammonium import Ammonium
from mbuild_polybuild.aa_functional_groups.sulfonate import Sulfonate


class Sbaa(mb.Compound):
    """
    A sulfobetaine acrylamide monomer.
    This function used our custom ester Compound.

    The following port names lead to the following atoms:
        'port[3]' : quaternary carbon backbone
        'down' : secondary carbon backbone

    Parameters
    ----------
    spacer_backbone : int, Optional, default=2
        This is the number of methylene groups between the backbone group and the first ion.
    spacer_ion : int, Optional, default=2
        This is the number of methylene groups between the backbone group and the second ion.
    """

    def __init__(self, spacer_backbone=2, spacer_ion=2, switch_backbone_chiral=False):
        super(Sbaa, self).__init__()

        if isinstance(spacer_ion, int) or isinstance(spacer_backbone, int):
            raise ValueError("Spacer length must be an integer")

        # Create Moieties
        acrylamide = Acrylamide(cap_branch=False, chiral_switch=switch_backbone_chiral)
        spacer_b = mb.recipes.Alkane(n=spacer_backbone, cap_front=False, cap_end=False)
        ammonium = Ammonium(substituents=2, alkane=[1])
        spacer_i = mb.recipes.Alkane(n=spacer_ion, cap_front=False, cap_end=False)
        sulfonate = Sulfonate()

        # Assemble Pieces
        self.add(acrylamide, "acrylamide")
        self.add(spacer_b, "spacer_backbone")
        mb.force_overlap(move_this=spacer_b, from_positions=spacer_b["up"], to_positions=acrylamide["port[1]"])

        self.add(ammonium, "ammonium")
        mb.force_overlap(move_this=ammonium, from_positions=ammonium["port[2]"], to_positions=spacer_b["down"])

        self.add(spacer_i, "spacer_ion")
        mb.force_overlap(move_this=spacer_i, from_positions=spacer_i["up"], to_positions=ammonium["port[3]"])

        self.add(sulfonate, "sulfonate")
        mb.force_overlap(move_this=sulfonate, from_positions=sulfonate["port[0]"], to_positions=spacer_i["down"])

        # Hoist acrylamide port label to top level.
        self.add(self["acrylamide"]["down"], "down", containment=False)
        self.add(self["acrylamide"]["port[3]"], "up", containment=False)


if __name__ == "__main__":
    m = Sbaa()
    m.save("sbaa.mol2", overwrite=True)
