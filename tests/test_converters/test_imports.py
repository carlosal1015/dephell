import pytest

from dephell.converters import ImportsConverter


@pytest.mark.parametrize('lines, expected', [
    (['from django import forms'], {'Django'}),
    (['from django.forms import Form'], {'Django'}),    # import from
    (['from dephell import __version__'], {'dephell'}),
    (['from dephell import *'], {'dephell'}),           # starred import
    (['from haystack import *'], {'django_haystack'}),  # aliasing
    (['import haystack'], {'django_haystack'}),         # simple import
    (['1/0'], set()),                                   # exception
])
def test_imports_parser(lines, expected):
    converter = ImportsConverter()
    modules = converter._get_modules(content='\n'.join(lines))
    assert modules == expected
