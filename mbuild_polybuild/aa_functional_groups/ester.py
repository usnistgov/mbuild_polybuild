"""Ester moiety."""

import mbuild as mb

import mbuild_polybuild.toolbox as tb


class Ester(mb.Compound):
    """
    An ester group -C(=O)O-.

    Available ports as follows:
        'port[0]' : connection with C
        'port[1]' : connection with O

    Parameters
    ----------
    ion : bool, Optional, default=False
    """

    def __init__(self, ion=False):
        super(Ester, self).__init__()

        mb.load(
            tb._import_pdb("ester.pdb"),
            compound=self,
            relative_to_module=self.__module__,
            infer_hierarchy=False,
        )
        self.translate(-self[0].pos)

        tb.atom2port(self)

        if ion:
            self.remove(self["port[1]"], reset_labels=True)


if __name__ == "__main__":
    m = Ester()
    m.save("ester.mol2", overwrite=True)
