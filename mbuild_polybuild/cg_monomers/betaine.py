"""Ester moiety."""

import mbuild as mb

from mbuild_polybuild.cg_monomers.bead import Bead


class Betaine(mb.Compound):
    """
    A generalized representation of a betaine monomer. "_B"*backbone_length()

    Available ports as follows:
        'up' : Connection with one side of monomer
        'down' : Connection with another side of the monomer

    Parameters
    ----------
    backbone_length : int, Optional, default=1
        Number of beads in backbone chain of a monomer. This chain is perpendicular to the pendent group close to the center.
    spacer_backbone : int, Optional, default=2
        Number of backbone groups between cation and backbone chain.
    spacer_ion : int, Optional, default=1
        Number of backbone groups between cation and terminal anion.
    polar_backbone : bool, Optional, default=False
        If true, a polar group "_P" is added to the base of the pendent where it meets the chain
    cap_group : bool, Optional, default=False
        Remove "down" port for monomer to create capping monomer.
    """

    def __init__(self, backbone_length=1, spacer_backbone=2, spacer_ion=1, polar_backbone=False, cap_group=False):
        super(Betaine, self).__init__()

        # Make Backbone Chain
        groupB_2 = Bead(name="_B", Nports=2)
        groupB_3 = Bead(name="_B", Nports=3)
        groupBP = Bead(name="_BP", Nports=2)

        down_port = None
        for i in range(backbone_length):
            if backbone_length == 1:
                self.add((groupB_3))
                up_port = groupB_3["up"]
                down_port = groupB_3["down"]
            elif i == int(backbone_length / 2):
                self.add((groupB_3))
                mb.force_overlap(move_this=groupB_3, from_positions=groupB_3["up"], to_positions=down_port)
                down_port = groupB_3["down"]
            elif down_port is None:
                tmp_bead = mb.compound.clone(groupB_2)
                self.add((tmp_bead))
                up_port = tmp_bead["up"]
                down_port = tmp_bead["down"]
            else:
                tmp_bead = mb.compound.clone(groupB_2)
                self.add((tmp_bead))
                mb.force_overlap(move_this=tmp_bead, from_positions=tmp_bead["up"], to_positions=down_port)
                down_port = tmp_bead["down"]
        side_port = groupB_3["branch_up"]

        # Add backbone spacer and optionally add polar group at base
        if polar_backbone and spacer_backbone == 0:
            raise ValueError("Polar pendent group cannot be added with a spacer of zero")
        elif polar_backbone:
            groupP_2 = Bead(name="_P", Nports=2)
            self.add((groupP_2))
            mb.force_overlap(move_this=groupP_2, from_positions=groupP_2["up"], to_positions=side_port)
            side_port = groupP_2["down"]

        for i in range(spacer_backbone - polar_backbone):
            tmp_bead = mb.compound.clone(groupBP)
            self.add((tmp_bead))
            mb.force_overlap(move_this=tmp_bead, from_positions=tmp_bead["up"], to_positions=side_port)
            side_port = tmp_bead["down"]

        # Add cation
        groupC_2 = Bead(name="_C", Nports=2)
        self.add((groupC_2))
        mb.force_overlap(move_this=groupC_2, from_positions=groupC_2["up"], to_positions=side_port)
        side_port = groupC_2["down"]

        # Add spacer between ions
        for i in range(spacer_ion):
            tmp_bead = mb.compound.clone(groupBP)
            self.add((tmp_bead))
            mb.force_overlap(move_this=tmp_bead, from_positions=tmp_bead["up"], to_positions=side_port)
            side_port = tmp_bead["down"]

        # Add anion
        groupA_1 = Bead(name="_A", Nports=1)
        self.add((groupA_1))
        mb.force_overlap(move_this=groupA_1, from_positions=groupA_1["up"], to_positions=side_port)

        # Hoist port labels to top level.
        self.add(up_port, "up", containment=False)
        if cap_group:
            self.remove(
                down_port,
                # reset_labels=True
            )
        else:
            self.add(down_port, "down", containment=False)


if __name__ == "__main__":
    m = Betaine()
    m.save("betaine.mol2", overwrite=True)
