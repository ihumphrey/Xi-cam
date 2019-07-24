# Creating a GUIPlugin

The GUIPlugin class provides an interface for writing a widget-based plugin.
The GUIPlugin class is intended to be derived.

## Core Concepts

The core concepts to keep in mind when creating a GUIPlugin are data models,
workflows, stages, and GUI layouts.

### Workflows

### Stages

Stages are used to organize user workflow in a GUIPlugin. For example, if we
have a GUIPlugin called MovieEnhance, we could break apart its user workflow
into separate but related components. MovieEnhance could be broken down into
a user workflow where the user can view the raw images and select a
region-of-interest, "enhance" the region-of-interest, then crop for a final
enhanced product image. These steps can be represented by stages: Raw,
Enhance, Crop.

From a programming perspective, a GUIPlugin must have at least one stage.

```python
self.stages = {'Default': GUILayout(QLabel('default widget'))}
```

Stages are defined in the base GUIPlugin class as an ordered dictionary,
where each key represents a stage (in order) and each associated value
is a GUILayout that defines the organization of widgets in that stage.

```python
self.stages = {
    'Examine': GUILayout(...),
    'Enhance': GUILayout(...),
    'Crop': GUILayout(...)
}
```

When clicking the MoveEnhance plugin on the top of the main window, you will see:

> MovieEnhance > Examine | Enhance | Crop | &uarr;

The Examine stage will be shown first, and you can move between the different
stages by clicking on them (Examine, Enhance, or Crop). To go back to seeing
a list of plugins, click the up arrow (&uarr;).

### GUI Layouts

The GUILayout class represents a layout of widgets to use in a GUIPlugin stage.
The layout is organized as a 3x3 grid on the main window of Xi-cam. These cells
are named according to their positions in the grid: center, top, bottom, left,
lefttop, leftbottom, right, righttop, rightbottom. 

When creating a GUILayout,
a *center* widget must be provided; the other positions are optional. Also note
that the *left* and *lefttop* widgets are already occupied by the main window's
data resource browser (i.e. file browser) and image preview widget, respectively.
It is possible to provide your own *left* and *lefttop* widgets but is not
recommended as it will replace those main window widgets.

### Data Models

The GUIPlugin class provides an interface for storing and accessing data within
the GUIPlugin. The interface methods are appendHeader, currentheader, and headers.

**appendHeader** is used to add data to the GUIPlugin. This data is added to an
internal model so it can be shared across stages of the GUIPlugin.

**currentheader** is used to retrieve the "current" data.

**headers** is used to get a list of all of the data items in the data model.

## Implementation

After reviewing the core concepts, we can start implementing our own GUIPlugin.
We will create a simple GUIPlugin that allows viewing loaded images, then we
will extend that plugin with more features until we have a MovieEnhance plugin.

### Creating the Plugin and the Plugin Marker File

For more information, see [] **TODO update this reference**

We will create two files, *MovieEnhancePlugin.yapsy-plugin* and 
*MovieEnhancePlugin.py*.

*MovieEnhancePlugin.yapsy-plugin*:
```
[Core]
Name = MovieEnhancePlugin
Module = /path/to/MovieEnhancePlugin.py

[Documentation]
Author = My Name
Version = 0.1.0
Website = http://website.somedomain
Description = Allows for movie-like image enhancements
```

*MovieEnhancePlugin.py*
```python
from qtpy.QtGui import QStandardItemModel
from qtpy.QtCore import QItemSelectionModel
from xicam.plugins import GUIPlugin, GUILayout
from xicam.gui.widgets.tabview import TabView


class MovieEnhancePlugin(GUIPlugin):
    def __init__(self):
        # Set up data model
        self.headerModel = QStandardItemModel
        self.selectionModel = QItemSelectionModel(self.headerModel)
        
        # Set up workflows
        
        # Set up widgets
        self.examineView = TabView(self.headerModel,
                                   widgetcls=,
                                   selectionmodel=,
                                   bindings=,
                                   geometry=)
        
        # Set up stages
        self.stages = {
            'Examine': GUILayout(),
            'Enhance': GUILayout(),
            'Crop': GUILayout()
        }
        
        super(MovieEnhancePlugin, self).__init__(self)
```
