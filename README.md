# lumimodel
The LHC luminosity model.

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

## Example 

Here you are a simple example.

``` python
from lumimodel import luminosity as lm
lm.get_bunch_luminosity()
```
