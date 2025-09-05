"""Monotomic Ion"""

import mbuild as mb


class MonatomicIon(mb.Compound):
    """
    A monatomic ion.

    This class initializes a monatomic ion by specifying its element.

    Parameters
    ----------
    element : str, optional, default=None
        The chemical symbol of the monatomic ion. Must be one of the following:
        "H", "Li", "Na", "K", "Rb", "Cs", "Mg", "Ca", "Sr", "Ba", "F", "Cl", "Br", "I".

    Examples
    --------
    >>> from mbuild_polybuild.aa_molecules.ion import MonatomicIon
    >>> ion = MonatomicIon(element="Na")
    """

    def __init__(self, element=None):
        """
        Initialize the monatomic ion.

        This method creates a monatomic ion by specifying its element.

        Parameters
        ----------
        element : str, optional, default=None
            The chemical symbol of the monatomic ion. Must be one of the following:
            "H", "Li", "Na", "K", "Rb", "Cs", "Mg", "Ca", "Sr", "Ba", "F", "Cl", "Br", "I".
        """
        super(MonatomicIon, self).__init__()

        ions = ["H", "Li", "Na", "K", "Rb", "Cs", "Mg", "Ca", "Sr", "Ba", "F", "Cl", "Br", "I"]
        if element not in ions:
            raise ValueError("element must be one of the following monatomic ions: {}".format(ions))

        self.add(mb.Particle(name=element, element=element))


if __name__ == "__main__":
    m = MonatomicIon()
    m.save("monatomic_ion.mol2", overwrite=True)
