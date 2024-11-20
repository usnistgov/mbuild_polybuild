"""Methacrylate moiety."""

import mbuild as mb

from mbuild_polybuild.aa_monomers.methacrylate import Methacrylate
from mbuild_polybuild.aa_functional_groups.ammonium import Ammonium
from mbuild_polybuild.aa_functional_groups.ester import Ester


class Cbma(mb.Compound):
    """
    An carboxybetaine methacrylate monomer.
    This function used our custom ester Compound.

    The following port names lead to the following atoms:
        'up' : quaternary carbon backbone
        'down' : secondary carbon backbone

    Parameters
    ----------
    spacer_backbone : int, Optional, default=2
        This is the number of methylene groups between the backbone group and the first ion.
    spacer_ion : int, Optional, default=2
        This is the number of methylene groups between the backbone group and the second ion.
    """

    def __init__(self, spacer_backbone=2, spacer_ion=2, switch_backbone_chiral=False):
        super(Cbma, self).__init__()

        if isinstance(spacer_ion, int) or isinstance(spacer_backbone, int):
            raise ValueError("Spacer length must be an integer")

        # Create Moieties
        methacrylate = Methacrylate(cap_branch=False, chiral_switch=switch_backbone_chiral)
        spacer_b = mb.recipes.Alkane(n=spacer_backbone, cap_front=False, cap_end=False)
        ammonium = Ammonium(substituents=2, alkane=[1])
        spacer_i = mb.recipes.Alkane(n=spacer_ion, cap_front=False, cap_end=False)
        ester = Ester(ion=True)

        # Assemble Pieces
        self.add(methacrylate, "methacrylate")
        self.add(spacer_b, "spacer_backbone")
        mb.force_overlap(move_this=spacer_b, from_positions=spacer_b["up"], to_positions=methacrylate["port[1]"])

        self.add(ammonium, "ammonium")
        mb.force_overlap(move_this=ammonium, from_positions=ammonium["port[2]"], to_positions=spacer_b["down"])

        self.add(spacer_i, "spacer_ion")
        mb.force_overlap(move_this=spacer_i, from_positions=spacer_i["up"], to_positions=ammonium["port[3]"])

        self.add(ester, "ester")
        mb.force_overlap(move_this=ester, from_positions=ester["port[0]"], to_positions=spacer_i["down"])

        # Hoist methacrylate port label to top level.
        self.add(self["methacrylate"]["down"], "down", containment=False)
        self.add(self["methacrylate"]["up"], "up", containment=False)


if __name__ == "__main__":
    m = Cbma()
    m.save("cbma.mol2", overwrite=True)
