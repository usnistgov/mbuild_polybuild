"""Ethylene moiety."""

import mbuild as mb
from mbuild.port import Port

from mbuild_polybuild.aa_fragments.c_quaternary import C as C_qu


class Ethylene(mb.Compound):
    """
    An ethylene backbone monomer.

    Ports
    -----
    - port[3]: Ternary carbon backbone.
    - down: Secondary carbon backbone.
    - port[1]: Amide group.

    Parameters
    ----------
    functional_group : mb.Compound, optional
        Add a custom functional group to connect to the open port on the backbone, completing a monomer.
    port_name : str, optional
        If more than one port is found on the functional_group, define the target port label here.
    cap_branch : bool, optional, default=True
        Choose whether to cap the open side group port with a hydrogen.
    cap_ternary : bool, optional, default=False
        Choose whether to cap what would be a ternary carbon as a secondary group.
    cap_primary : bool, optional, default=False
        Choose whether to cap what would be a secondary carbon as a primary carbon.
    chiral_switch : bool, optional, default=False
        When this is true, the hydrogen group and amide group switch places.

    Examples
    --------
    >>> from mbuild_polybuild.aa_monomers.ethylene import Ethylene
    >>> ethylene = Ethylene()
    >>> ethylene.visualize()

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
        super(Ethylene, self).__init__()

        hyd = mb.lib.atoms.H()
        ch2 = mb.lib.moieties.CH2()
        c_qu = C_qu()

        self.add(c_qu, "quaternary C")
        self.add(ch2, "CH2")
        mb.force_overlap(move_this=ch2, from_positions=ch2["up"], to_positions=c_qu["port[0]"])

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

        # Optionally cap amide with hydrogen, or add custom substituent
        is_port = False
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

            group = functional_group
            group_port = functional_group[port_name]
        elif cap_branch:
            group = mb.lib.atoms.H()
            self.add(group, "cap backbone H, no branch")
            group_port = group["up"]
        else:
            self.add(self["amide"]["port[1]"], "port[1]", containment=False)
            is_port = True

        if not is_port:
            self.add(hyd, "hydrogen")
            if chiral_switch:
                mb.force_overlap(move_this=hyd, from_positions=hyd["up"], to_positions=c_qu["port[1]"])
                mb.force_overlap(move_this=group, from_positions=group_port, to_positions=c_qu["port[2]"])
            else:
                mb.force_overlap(move_this=hyd, from_positions=hyd["up"], to_positions=c_qu["port[2]"])
                mb.force_overlap(move_this=group, from_positions=group_port, to_positions=c_qu["port[1]"])


if __name__ == "__main__":
    m = Ethylene()
    m.save("ethylene.mol2", overwrite=True)
