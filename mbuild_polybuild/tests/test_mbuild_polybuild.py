"""
Unit and regression test for the mbuild_polybuild package.
"""

import pytest
import sys
import mbuild as mb

# Import all classes for comprehensive testing
from mbuild_polybuild.aa_functional_groups import (
    Amide, Ammonium, Ester, MEA, MHTA, MPTB, PTP, Phenyl, 
    Sulfonate, TFTB, TFTP, TMSTB
)
from mbuild_polybuild.aa_monomers import (
    Acrylamide, Cbma, Ethylene, Methacrylate, Sbaa, Sbma
)
from mbuild_polybuild.aa_fragments import C
from mbuild_polybuild.aa_molecules import MonatomicIon
from mbuild_polybuild.cg_monomers import Bead, Betaine

def test_mbuild_polybuild_imported():
    """ Sample test, will always pass so long as import statement worked """
    assert "mbuild_polybuild" in sys.modules


# Test parameter matrices for comprehensive coverage
@pytest.mark.parametrize("class_type", [
    Amide, Ester, MEA, MHTA, MPTB, PTP, Phenyl, Sulfonate, TFTB, TFTP, TMSTB
])
def test_aa_functional_groups_instantiation(class_type):
    """Test that all AA functional group classes can be instantiated."""

    instance = class_type()
    assert isinstance(instance, mb.Compound)
    assert hasattr(instance, 'children')


@pytest.mark.parametrize("substituents", [0, 1, 2, 3])
def test_ammonium_substituents(substituents):
    """Test Ammonium class with different substituent counts."""

    if substituents == 0:
        # Test that substituents=0 with alkane parameter raises ValueError
        with pytest.raises(ValueError):
            Ammonium(substituents=substituents, alkane=[2])
        # Test that substituents=0 without additional params is valid
        instance = Ammonium(substituents=substituents)
        assert isinstance(instance, mb.Compound)
    else:
        instance = Ammonium(substituents=substituents, alkane=[2])
        assert isinstance(instance, mb.Compound)


@pytest.mark.parametrize("class_type,params", [
    (Acrylamide, {"cap_branch": True}),
    (Acrylamide, {"cap_ternary": True}),
    (Acrylamide, {"chiral_switch": True}),
    (Ethylene, {"cap_branch": True}),
    (Ethylene, {"cap_primary": True}),
    (Methacrylate, {"cap_branch": True}),
    (Methacrylate, {"cap_ternary": True}),
    (Methacrylate, {"chiral_switch": True}),
])
def test_aa_monomers_with_parameters(class_type, params):
    """Test AA monomer classes with various parameter combinations."""

    instance = class_type(**params)
    assert isinstance(instance, mb.Compound)
    assert hasattr(instance, 'children')


@pytest.mark.parametrize("spacer_backbone,spacer_ion", [
    (1, 1), (2, 2), (3, 1), (1, 3)
])
def test_betaine_monomers_spacers(spacer_backbone, spacer_ion):
    """Test betaine monomer classes with different spacer configurations."""

    for class_type in [Sbaa, Sbma, Cbma]:
        print(spacer_backbone, spacer_ion, type(spacer_backbone), type(spacer_ion))
        instance = class_type(spacer_backbone=spacer_backbone, spacer_ion=spacer_ion)
        assert isinstance(instance, mb.Compound)


@pytest.mark.parametrize("backbone_length,spacer_backbone,spacer_ion,polar_backbone", [
    (1, 1, 1, False),
    (2, 2, 1, False),
    (3, 2, 2, True),
    (1, 0, 1, False),
])
def test_cg_betaine_parameters(backbone_length, spacer_backbone, spacer_ion, polar_backbone):
    """Test CG Betaine class with various parameter combinations."""

    if polar_backbone and spacer_backbone == 0:
        with pytest.raises(ValueError):
            Betaine(backbone_length=backbone_length, spacer_backbone=spacer_backbone, 
                   spacer_ion=spacer_ion, polar_backbone=polar_backbone)
    else:
        instance = Betaine(backbone_length=backbone_length, spacer_backbone=spacer_backbone,
                         spacer_ion=spacer_ion, polar_backbone=polar_backbone)
        assert isinstance(instance, mb.Compound)


@pytest.mark.parametrize("name,nports", [
    ("_B", 2), ("_B", 3), ("_C", 2), ("_A", 1)
])
def test_cg_bead_parameters(name, nports):
    """Test CG Bead class with different names and port counts."""

    if nports == 0:
        with pytest.raises(ValueError):
            Bead(name=name, Nports=nports)
    elif nports > 4:
        with pytest.raises(ImportError):
            Bead(name=name, Nports=nports)
    else:
        instance = Bead(name=name, Nports=nports)
        assert isinstance(instance, mb.Compound)


def test_aa_fragments():
    """Test AA fragment classes."""

    c_fragment = C()
    assert isinstance(c_fragment, mb.Compound)


@pytest.mark.parametrize("element", ["Na", "K", "Cl"])
def test_aa_molecules_ion(element):
    """Test MonatomicIon class with different elements."""

    ion = MonatomicIon(element=element)
    assert isinstance(ion, mb.Compound)


def test_compound_port_functionality():
    """Test that compounds have proper port functionality."""

    # Test that compounds can be created and have expected attributes
    amide = Amide()
    assert hasattr(amide, 'labels')
    
    # Test that ports exist where expected
    ester = Ester()
    assert len(ester.children) > 0


def test_error_handling():
    """Test proper error handling in classes."""

    # Test invalid substituent configuration for Ammonium
    with pytest.raises(ValueError):
        Ammonium(substituents=0, alkane=[3])
            
    # Test invalid Bead port count
    with pytest.raises(ValueError):
        Bead(name="_B", Nports=0)
            
    # Test invalid Betaine polar configuration
    with pytest.raises(ValueError):
        Betaine(spacer_backbone=0, polar_backbone=True)
