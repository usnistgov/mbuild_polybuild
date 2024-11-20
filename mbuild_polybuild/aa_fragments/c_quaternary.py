"""Quaternary moiety."""

import mbuild as mb

import mbuild_polybuild.toolbox as tb


class C(mb.Compound):
    """Quaternary C"""

    def __init__(self):
        super(C, self).__init__()

        mb.load(
            tb._import_pdb("c_quaternary.pdb"),
            compound=self,
            relative_to_module=self.__module__,
            infer_hierarchy=False,
        )
        self.translate(-self[0].pos)

        tb.atom2port(self)


if __name__ == "__main__":
    m = C()
    m.save("c_quaternary.mol2", overwrite=True)
