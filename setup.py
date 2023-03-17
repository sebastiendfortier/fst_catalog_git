from setuptools import setup, find_packages

setup(
    name='fst_catalog',
    version='1.0.0',
    description='Library of functions for working with FST files',
    author='Sebastien Fortier',
    author_email='sebastien.fortier@ec.gc.ca',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.5.3',
        'numpy>=1.23.5',
        'fstpy @ git+https://gitlab.science.gc.ca/CMDS/fstpy.git',
        'fstd2nc @ git+https://github.com/neishm/fstd2nc.git',
        'pyproj>=3.3.1',
        'xarray>=2023.2.0',
        'cartopy>=0.21.0',
        'hvplot>=0.8.2'
    ]
)
