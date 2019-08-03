# Resources

## Example Xi-cam Plugins

* [Xi-cam Log Plugin](https://github.com/synchrotrons/Xi-cam.plugins.Log) -
Example of a simple single-stage GUIPlugin.

* [Xi-cam NCEM Plugin](https://github.com/synchrotrons/Xi-cam.NCEM) -
Example of a multi-stage GUIPlugin with more functionality.

## Python

```TODO -- replace this first one with a different introductory python```
* [Python OOP Introduction and Tutorial](https://realpython.com/python3-object-oriented-programming/) -
A starting point for learning about object-oriented programming and how to write object-oriented code in Python3.

* [Presentation on OOP in Python](https://www.cs.colorado.edu/~kena/classes/5448/f12/presentation-materials/li.pdf) -


## Qt

[Qt](https://www.qt.io/what-is-qt/?utm_campaign=Navigation%202019&utm_source=megamenu) 
is a framework written in C++ for developing graphical user interfaces. 
PySide2 and PyQt5 are two different python bindings to the Qt C++ API. 
QtPy is a wrapper that allows for writing python Qt code with either PySide2 or PyQt5 installed.

Xi-cam uses [QtPy](https://pypi.org/project/QtPy/) to interact with different Python bindings to Qt.
QtPy allows you *"to write your code as if you were using PySide2 but import Qt modules from qtpy instead of PySide2 
(or PyQt5)"*. 
The references below show PySide2 examples and documentation; when writing a Xi-cam
plugin, make sure to use the `qtpy` modules when importing.

* [PyQt5 GUI Tutorial](https://build-system.fman.io/pyqt5-tutorial) - Introductory tutorial for learning the basic
concepts of Qt. *Note: this tutorial is written for PyQt5, remember to import from `qtpy` instead of `PyQt5` or 
`PySide2` when writing code for Xi-cam.*

* [PySide2 Documentation](https://pyside.github.io/docs/pyside/) - Documentation for PySide2. Since the QtPy API
resembles PySide2, this documentation is helpful for looking up python Qt modules and classes that you may use.

