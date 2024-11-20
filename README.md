mBuild Polymer Builder
==============================

## [NIST Disclaimer][nist-disclaimer]

Certain commercial equipment, instruments, or materials are identified in this paper to foster understanding. Such identification does not imply recommendation or endorsement by the National Institute of Standards and Technology, nor does it imply that the materials or equipment identified are necessarily the best available for the purpose.

## Summary

This mbuild recipe allows for the generation of complex monomers with controlled tacticity. DOI: 10.18434/mds2-3640

mbuild_polybuild is bound by a [Code of Conduct](https://github.com/usnistgov/mbuild_polybuild/blob/main/CODE_OF_CONDUCT.md).

## Installation

To build mbuild_polybuild from source,
we highly recommend using virtual environments.
If possible, we strongly recommend that you use
[Anaconda](https://docs.conda.io/en/latest/) as your package manager.
Below we provide instructions for `pip`.

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

## Copyright

Works of NIST employees are not not subject to copyright protection in the United States

<!-- References -->

[nist-disclaimer]: https://www.nist.gov/open/license
