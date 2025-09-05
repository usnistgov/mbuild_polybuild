"""This module provides all-atom functional groups.

These functional groups can be used to build complex molecular systems by
combining them with other components. Each functional group is represented
as a class that inherits from `mb.Compound`.

Available Functional Groups
---------------------------
- `Amide`: An amide group (-C(=O)N(H)-).
- `Ammonium`: An ammonium group.
- `Ester`: An ester group (-C(=O)O-).
- `MEA`: A monoethanolamine group.
- `MHTA`: A methylhydroxypropylthioacetate group.
- `MPTB`: A methoxyphenylthiobutanol group.
- `PTP`: A pyridinylthiopropanol group.
- `Phenyl`: A phenyl group.
- `Sulfonate`: A sulfonate group (-S(=O)2O-).
- `TFTB`: A trifluoroethylthiobutanol group.
- `TFTP`: A tridecafluorooctylthiopropanol group.
- `TMSTB`: A trimethylsilylpropylthiobutanol group.

Examples
--------
>>> from mbuild_polybuild.aa_functional_groups import MHTA
>>> mhta = MHTA()
>>> mhta.save("methylhydroxypropylthioacetate.mol2", overwrite=True)
"""

from mbuild_polybuild.aa_functional_groups.amide import Amide as Amide
from mbuild_polybuild.aa_functional_groups.ammonium import Ammonium as Ammonium
from mbuild_polybuild.aa_functional_groups.ester import Ester as Ester
from mbuild_polybuild.aa_functional_groups.mea import MEA as MEA
from mbuild_polybuild.aa_functional_groups.mhta import MHTA as MHTA
from mbuild_polybuild.aa_functional_groups.mptb import MPTB as MPTB
from mbuild_polybuild.aa_functional_groups.phenyl import Phenyl as Phenyl
from mbuild_polybuild.aa_functional_groups.ptp import PTP as PTP
from mbuild_polybuild.aa_functional_groups.sulfonate import Sulfonate as Sulfonate
from mbuild_polybuild.aa_functional_groups.tftb import TFTB as TFTB
from mbuild_polybuild.aa_functional_groups.tftp import TFTP as TFTP
from mbuild_polybuild.aa_functional_groups.tmstb import TMSTB as TMSTB
