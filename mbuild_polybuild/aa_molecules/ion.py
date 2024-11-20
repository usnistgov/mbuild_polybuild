"""Ester moiety."""

import mbuild as mb


class MonatomicIon(mb.Compound):
    """
    An ester group -C(=O)O-.

    Available ports as follows:
        'port[0]' : connection with C
        'port[1]' : connection with O

    Parameters
    ----------
    ion : bool, Optional, default=False
    """

    def __init__(self, element=None):
        super(MonatomicIon, self).__init__()

        ions = ["H", "Li", "Na", "K", "Rb", "Cs", "Mg", "Ca", "Sr", "Ba", "F", "Cl", "Br", "I"]
        if element not in ions:
            raise ValueError("element must be one of the following monatomic ions: {}".format(ions))

        self.add(mb.Particle(name=element, element=element))


if __name__ == "__main__":
    m = MonatomicIon()
    m.save("monatomic_ion.mol2", overwrite=True)
