# lumimodel
The LHC luminosity model.

# cl2pd
A simple package to convert CERN Logging information (using pytimber/CALS, mat-files, massi-files, TFS-files) into a pandas dataframe. 

This data type is very convenient to represent time series and it offers a large set of methods to manage missing data, to do data aggregation and group operation, to perform data wrangling, to handle timezones, to plots data, etc...
For a schematic and succinct introduction to pandas please refers for example to 
http://datasciencefree.com/pandas.pdf.

An important source of inspiration was the package **pytimber** by R. De Maria et al. and their generous approach in sharing tools and foster collaborations.

## Install the package
You can install the package, for instance on the SWAN terminal (www.swan.cern.ch), using:
```
pip install --user git+https://github.com/sterbini/lumimodel.git
```
or to upgrade it
```
pip install --upgrade --user git+https://github.com/sterbini/lumimodel.git
```
or to upgrade a fork of the project
```
pip install --upgrade --user git+https://github.com/sterbini/lumimodel.git@fork_name
```

# Example 

```
from lumimodel import luminosity as lm
lm.get_bunch_luminosity()

```
