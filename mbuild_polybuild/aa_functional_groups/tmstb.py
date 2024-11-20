"""Trimethylsilylpropylthiobutanol moiety."""

import mbuild as mb

import mbuild_polybuild.toolbox as tb


class TMSTB(mb.Compound):
    """A trimethylsilylpropylthiobutanol"""

    def __init__(self):
        super(TMSTB, self).__init__()

        mb.load(
            tb._import_pdb("trimethylsilylpropylthiobutanol.pdb"),
            compound=self,
            relative_to_module=self.__module__,
            infer_hierarchy=False,
        )
        self.translate(-self[0].pos)

        tb.atom2port(self)


if __name__ == "__main__":
    m = TMSTB()
    m.save("trimethylsilylpropylthiobutanol.mol2", overwrite=True)
