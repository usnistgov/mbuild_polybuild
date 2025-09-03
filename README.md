mBuild Polymer Builder
==============================

## [NIST Disclaimer][nist-disclaimer]

Certain commercial equipment, instruments, or materials are identified in this paper to foster understanding. Such identification does not imply recommendation or endorsement by the National Institute of Standards and Technology, nor does it imply that the materials or equipment identified are necessarily the best available for the purpose.

## Summary

This mbuild recipe allows for the generation of complex monomers with controlled tacticity. DOI: [10.18434/mds2-3640](10.18434/mds2-3640)

mbuild_polybuild is bound by a [Code of Conduct](https://github.com/usnistgov/mbuild_polybuild/blob/main/CODE_OF_CONDUCT.md).

### [Documentation][docs4nist]

## Dependencies

This package is tested for python 3.10+ on all Windows, MacOS, and Linux systems.
No python library dependenices are required before installation.

## Installation

To build mbuild_polybuild from source, we highly recommend using virtual environments.
Below we provide instructions for `pip`.

#### Download

``git clone https://github.com/usnistgov/mbuild_polybuild``

### User with pip

To build the package from source, run:

```
pip install .
```

If you want to create a development environment, install
the dependencies required for tests and docs with:

```
pip install .[test,doc]
```

### Developer with pip

To build the package from source in editable mode, run:

```
pip install -e .[test,doc]
```

Initialize pre-commit for automatic formatting.

```
pre-commit install
```

## License

The license in this repository is superseded by the most updated language
on of the Public Access to NIST Research [*Copyright, Fair Use, and Licensing
Statement for SRD, Data, and Software*][nist-open].

### Contact

Jennifer A. Clark, PhD\
[Debra J. Audus, PhD][daudus] (debra.audus@nist.gov)\
[Jack F. Douglas, PhD][jdouglas]

Affilation:
[Polymer Analytics Project][polyanal]\
[Polymer and Complex Fluids Group][group1]\
[Materials Science and Engineering Division][msed]\
[Material Measurement Laboratory][mml]\
[National Institute of Standards and Technology][nist]

## Citation

Jennifer A. Clark, Debra J. Audus, Jack F. Douglas (2024), Polymer Builder Extension for MosDef-mBuild: mbuild_polybuild, National Institute of Standards and Technology, https://doi.org/10.18434/mds2-3640

## Copyright

Works of NIST employees are not not subject to copyright protection in the United States

<!-- References -->

[nist-disclaimer]: https://www.nist.gov/open/license
[nist-open]: https://www.nist.gov/open/license#software
[docs4nist]: https://www.nist.gov/docs4nist/
[daudus]: https://www.nist.gov/people/debra-audus
[jdouglas]: https://www.nist.gov/people/jack-f-douglas
[polyanal]: https://www.nist.gov/programs-projects/polymer-analytics
[group1]: https://www.nist.gov/mml/materials-science-and-engineering-division/polymers-and-complex-fluids-group
[msed]: https://www.nist.gov/mml/materials-science-and-engineering-division
[mml]: https://www.nist.gov/mml
[nist]: https://www.nist.gov
