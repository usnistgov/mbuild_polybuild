"""Tridecafluorooctylthiopropanol moiety."""

import mbuild as mb

import mbuild_polybuild.toolbox as tb


class TFTB(mb.Compound):
    """An trifluoroethylthiobutanol"""

    def __init__(self):
        super(TFTB, self).__init__()

        mb.load(
            tb._import_pdb("trifluoroethylthiobutanol.pdb"),
            compound=self,
            relative_to_module=self.__module__,
            infer_hierarchy=False,
        )
        self.translate(-self[0].pos)

        tb.atom2port(self)


if __name__ == "__main__":
    m = TFTB()
    m.save("trifluoroethylthiobutanol.mol2", overwrite=True)
