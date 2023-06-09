# Introduction

## What is it?

fst_catalog is a set of functions that help cataloging fst file records.

## fst_catalog philosophy

Provide a structured catalog of records that belong together according to their grid and generation process.


# Requirements

- pandas>=1.5.3
- numpy>=1.23.5
- fstpy @ git+https://gitlab.science.gc.ca/CMDS/fstpy.git
- fstd2nc @ git+https://github.com/neishm/fstd2nc.git
- pyproj


# Installation

Use the git repository package:

    python3 -m pip install git+http://gitlab.science.gc.ca/CMDS/fst_catalog.git

### Use fst_catalog

``` python
# inside your script
import fst_catalog
import datetime
from pathlib import Path
current_date = datetime.datetime.now()
year_month_day_string = current_date.strftime('%Y%m%d')

filter = '00_01*'
base_path1 = Path('/home/smco500/cmcprod/ppp5/suites/gdps/g1/gridpt.usr/prog/eta')

files = glob(f'{base_path1}/{year_month_day_string}{filter}')

cat = FstCatalog(files).catalog()
cat.voir_view()
cat.df
cat.files
cat.get_dataset(22)
```

For more examples and information check out the [documentation](https://web.science.gc.ca/~spst900/fst_catalog/master/index.html)

# Contributing

## Getting the source code

``` bash
git clone git@gitlab.science.gc.ca:cmds/fst_catalog.git
# create a new branch
git checkout -b my_change
# modify the code
# commit your changes
# fetch changes
git fetch
# merge recent master
git merge origin/master
# push your changes
git push my_change
```

Then create a merge request on science\'s gitlab
<https://gitlab.science.gc.ca/CMDS/fst_catalog/merge_requests>


# Acknowledgements

Great thanks to:

-   [Micheal Neish](mailto:Micheal.Neish@canada.ca) for the awsome
    fstd2nc project, great insights on how to develop xarray structure
    from CMC standard files and great functions to work on fst files.
