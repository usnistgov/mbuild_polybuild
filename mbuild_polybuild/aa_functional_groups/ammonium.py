"""Ammonium moiety."""

import mbuild as mb
from mbuild.port import Port

import mbuild_polybuild.toolbox as tb


class Ammonium(mb.Compound):
    """
    An ammonium group -C(=O)O-.

    The following ports are available for ammonium: 'port[0]' 'port[1]'

    Parameters
    ----------
    substituents : int, Optional, default=0
        The number of substituent groups to add to the ammonium center
    alkane : int/list, Optional, default=None
        If `int`, this is the length of the carbon chain of the assigned number of substituent groups
        If a list, the length must be equal to the `substituent` parameter, defining the carbon chain length of each group
    custom : list, Optional, default=None
        This list contains compounds to be added as substituents. It may be of length 1 or equal to the `substituent` parameter.
    ports : list[str], Optional, default=None
        This list of strings contains the name of the port to attach to the ammonium group for each `Compound` in `custom`.
        It must be the same length as `custom`. If the name of a port is unknown or there is only one option, that list entry
        may be None. However, if the substiuent has multiple ports, the `str` must be defined.
    """

    def __init__(self, substituents=0, alkane=None, custom=None, ports=None):
        super(Ammonium, self).__init__()

        # Create ammonium center
        mb.load(
            tb._import_pdb("ammonium.pdb"),
            compound=self,
            relative_to_module=self.__module__,
            infer_hierarchy=False,
        )
        self.translate(-self[0].pos)
        tb.atom2port(self)

        # Check for substituents
        used_ports = 0
        if (custom is not None or alkane is not None) and substituents == 0:
            raise ValueError("The number of substituents is set to zero.")

        if custom is not None:
            flag_alkane = False
            try:
                l_compounds = len(custom)
            except Exception:
                l_compounds = 1
                custom = [custom]

            for compound in custom:
                flag = isinstance(compound, mb.Compound)
                if not flag:
                    raise TypeError("The `custom` parameter should contain objects of the `Compound` class.")

            if l_compounds > 1 and l_compounds != substituents:
                raise ValueError("The number of given Compounds must equal the number of requested substituents.")
        elif alkane is not None:
            flag_alkane = True
            try:
                l_compounds = len(alkane)
            except Exception:
                l_compounds = 1
                alkane = [alkane]

            if l_compounds == 1:
                l_compounds = substituents
                alkane = [alkane[0] for x in range(l_compounds)]
            elif l_compounds != substituents:
                raise ValueError(
                    "If list of alkane lengths is provided, it must be the of the length `substituents` defines."
                )

            custom = []
            for l_chain in alkane:
                Alkane = mb.recipes.Alkane(n=l_chain, cap_front=False)
                custom.append(Alkane)

        for i in range(substituents):
            if l_compounds == 1:
                compound = custom[0]
            else:
                compound = custom[i]

            self.add(compound, "substituent{}".format(i + 1))

            # Get port name
            if flag_alkane:
                port_name = "up"
            else:
                port_labels = [key for key, val in compound.labels.items() if isinstance(val, Port)]
                if len(port_labels) > 1:
                    if ports is None:
                        raise ValueError(
                            "Substituent custom[{}], has ports, {}. Define the port you want to use with the `ports` list input.".format(
                                i, port_labels
                            )
                        )
                    elif len(ports) != l_compounds:
                        raise ValueError(
                            "The `ports` list must be the same length as the custom list to avoid ambiguity. Buffer with None for substituents with only one port option."
                        )
                    elif not isinstance(ports[i], str):
                        raise ValueError(
                            "The port name for custom[{}] is required, but the provided value, {}, is insufficient.".format(
                                i, ports[i]
                            )
                        )
                    elif ports[i] not in port_labels:
                        raise ValueError(
                            "The provided port, {}, is not found in the ports for custom[{}], {}".format(
                                ports[i], i, port_labels
                            )
                        )
                    else:
                        port_name = ports[i]
                        # Hoist other port label to top level.
                        for name in port_labels:
                            if name != port_name:
                                self.add(self["substituent{}".format(i + 1)][name], name, containment=False)
                else:
                    if ports[i] not in port_labels:
                        raise ValueError(
                            "The provided port, {}, is not found in the ports for custom[{}], {}".format(
                                ports[i], i, port_labels
                            )
                        )
                    port_name = port_labels[0]

            # Make bond
            mb.force_overlap(
                move_this=compound, from_positions=compound[port_name], to_positions=self["port[{}]".format(used_ports)]
            )
            used_ports += 1


if __name__ == "__main__":
    m = Ammonium()
    m.save("ammonium.mol2", overwrite=True)
