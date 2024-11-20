"""Methoxyphenylthiobutanol moiety."""

import mbuild as mb

import mbuild_polybuild.toolbox as tb


class MPTB(mb.Compound):
    """An methoxyphenylthiobutanol"""

    def __init__(self):
        super(MPTB, self).__init__()

        mb.load(
            tb._import_pdb("methoxyphenylthiobutanol.pdb"),
            compound=self,
            relative_to_module=self.__module__,
            infer_hierarchy=False,
        )
        self.translate(-self[0].pos)

        tb.atom2port(self)


if __name__ == "__main__":
    m = MPTB()
    m.save("methoxyphenylthiobutanol.mol2", overwrite=True)
