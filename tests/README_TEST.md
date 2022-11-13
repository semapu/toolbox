# Description

This folder contains the Python tests for the toolbox. Moreover, it is explained the porpuse, how to configure 
and run Pylint

# Python tests

### Execution -- Folder

To run the test, execute the following command from toolbok/ (inside)

    [shell]

    pytest ./tests/

# Pylint

### Description

TO BE DONE ...

### Steps

1. Install pylint: `pip install pylint`

2. Download the `pylintrc`, from [official source](https://google.github.io/styleguide/pylintrc)

3. Install the Pylint `plugging from PyCharm`
   1. File > Settings > Pylint\
   2. Define Pylint executable -> File from the environemtn
   3. Path to pylintr -> Downloaded in step 2
   4. If necessary, define the arguments. Current arguments: `--indent-string "    " --indent-after-paren 4`
      (based on PEP8).


### References

1. [Pycharm, Pylint, Pytest, and VCS](http://docenti.ing.unipi.it/m.cimino/lsse/pres/Alfeo,%20Introduction%20to%20PyCharm,%20PyLint,%20PyTest,%20and%20CVS.pdf)