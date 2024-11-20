"""Pyridinylthiopropanol moiety."""

import mbuild as mb

import mbuild_polybuild.toolbox as tb


class PTP(mb.Compound):
    """An pyridinylthiopropanol"""

    def __init__(self):
        super(PTP, self).__init__()

        mb.load(
            tb._import_pdb("pyridinylthiopropanol.pdb"),
            compound=self,
            relative_to_module=self.__module__,
            infer_hierarchy=False,
        )
        self.translate(-self[0].pos)

        tb.atom2port(self)


if __name__ == "__main__":
    m = PTP()
    m.save("pyridinylthiopropanol.mol2", overwrite=True)
