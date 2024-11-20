"""Methacrylate moiety."""

import mbuild as mb
from mbuild.port import Port

from mbuild_polybuild.aa_functional_groups.ester import Ester
from mbuild_polybuild.aa_fragments.c_quaternary import C as C_qu


class Methacrylate(mb.Compound):
    """
    An methacrylate monomer.
    This function used our custom ester Compound.

    The following port names lead to the following atoms:
        'up' : quaternary carbon backbone
        'down' : secondary carbon backbone
        'port[1]' : ester group

    Parameters
    ----------
    functional_group : mb.Compound
        Add a custom functional group to connect to the ester, completing a monomer
    port_name : str
        If more than one port is found on the functional_group, define the target port label here.
    cap_branch : bool, Optional, default=True
        Choose whether to cap the ester group with a hydrogen
    cap_ternary : bool, Optional, default=False
        Choose whether to cap what would be a quaternary carbon as a ternary group
    cap_primary : bool, Optional, default=False
        Choose whether to cap what would be a secondary carbon as a primary carbon
    chiral_switch : bool, Optional, default=False
        When this is true, the methyl group and ester group switch places

    """

    def __init__(
        self,
        functional_group=None,
        port_name=None,
        cap_branch=True,
        cap_ternary=False,
        cap_primary=False,
        chiral_switch=False,
    ):
        super(Methacrylate, self).__init__()

        # Make methacrylate base
        methyl = mb.recipes.Alkane(n=1, cap_front=False)
        ch2 = mb.lib.moieties.CH2()
        c_qu = C_qu()
        ester = Ester()

        self.add(c_qu, "quaternary C")
        self.add(ch2, "CH2")
        mb.force_overlap(move_this=ch2, from_positions=ch2["up"], to_positions=c_qu["port[0]"])

        self.add(methyl, "methyl")
        self.add(ester, "ester")
        if chiral_switch:
            mb.force_overlap(move_this=methyl, from_positions=methyl["up"], to_positions=c_qu["port[1]"])
            mb.force_overlap(move_this=ester, from_positions=ester["port[0]"], to_positions=c_qu["port[2]"])
        else:
            mb.force_overlap(move_this=methyl, from_positions=methyl["up"], to_positions=c_qu["port[2]"])
            mb.force_overlap(move_this=ester, from_positions=ester["port[0]"], to_positions=c_qu["port[1]"])

        # Optionally cap backbone with hydrogen
        if cap_ternary:
            hyd1 = mb.lib.atoms.H()
            self.add(hyd1, "cap quat")
            mb.force_overlap(move_this=hyd1, from_positions=hyd1["up"], to_positions=c_qu["port[3]"])
        else:
            self.add(self["quaternary C"]["port[3]"], "up", containment=False)
        if cap_primary:
            hyd2 = mb.lib.atoms.H()
            self.add(hyd2, "cap CH2")
            mb.force_overlap(move_this=hyd2, from_positions=hyd2["up"], to_positions=ch2["down"])
        else:
            self.add(self["CH2"]["down"], "down", containment=False)

        # Optionally cap ester with hydrogen, or add custom substituent
        if functional_group is not None:
            if not isinstance(functional_group, mb.Compound):
                raise ValueError("Provided functional_group should be based on the mb.Compound class.")
            self.add(functional_group, "substituent")

            port_labels = [key for key, val in functional_group.labels.items() if isinstance(val, Port)]
            if len(port_labels) > 1:
                if port_name is None:
                    raise ValueError(
                        "Functional_group has, {}. Define the port you want to use with `port_name`.".format(
                            port_labels
                        )
                    )
                elif not isinstance(port_name, str):
                    raise ValueError(
                        "The port_name is required, but the provided value, {}, is insufficient.".format(port_name)
                    )
                elif port_name not in port_labels:
                    raise ValueError(
                        "The provided port, {}, is not found in the ports for functional_group, {}".format(
                            port_name, port_labels
                        )
                    )
                # Hoist other port label to top level.
                for name in port_labels:
                    if name != port_name:
                        self.add(self["substituent"][name], name, containment=False)
            else:
                port_name = port_labels[0]

            mb.force_overlap(
                move_this=functional_group, from_positions=functional_group[port_name], to_positions=ester["port[1]"]
            )
        elif cap_branch:
            hyd3 = mb.lib.atoms.H()
            self.add(hyd3, "cap COO")
            mb.force_overlap(move_this=hyd3, from_positions=hyd3["up"], to_positions=ester["port[1]"])
        else:
            self.add(self["ester"]["port[1]"], "port[1]", containment=False)

        self.reset_labels()


if __name__ == "__main__":
    m = Methacrylate()
    m.save("methacrylate.mol2", overwrite=True)
