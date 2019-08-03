# Creating a GUIPlugin

Xi-cam provides the GUIPlugin class for writing a Qt widget-based plugin.
By deriving a GUIPlugin, you can define a custom plugin in Xi-cam that can
be used to load, process, and analyze data.

See the
[Resources](resources.md) page for more information about Qt and QtPy.

## Prerequisites

If you have not installed Xi-cam for development, follow the instructions on the 
[Installing Xi-cam](install.md) page.

Also, *make sure that your xicam virtual environment (venv) is activated*. 

For Windows, commands will be run with
Git Bash. For macOS and Linux, commands will be run on the terminal.

## Core Concepts

The core concepts to keep in mind when creating a GUIPlugin are data models,
workflows, stages, and GUI layouts.

### Stages

Stages are used to organize user work flow in a GUIPlugin.
Each stage represents a collection of widgets used to perform some task. 
A GUIPlugin must have at least one stage.

Stages are defined as as an ordered dictionary,
where each key represents a stage's name and each associated value
is a [GUILayout](#gui-layouts) that defines the organization of widgets for that stage.
The key will be used at the stage's display name in Xi-cam.

As an example, we could have a Demo GUIPlugin that has the stages
X and Y. To set these stages, we would set the
GUIPlugin's stages property:

```python
self.stages = {
    'X': GUILayout(xWidget),
    'Y': GUILayout(yWidget),}
```

This creates two stages, X and Y, in your GUIPlugin.
When clicking the Demo plugin on the top of the main window, you would see:

> Demo | X | Y | &uarr;

[//]: <> (For example, if we
have a GUIPlugin called MovieEnhance, we could break apart its user work flow
into separate but related components. MovieEnhance could be broken down into
a user workflow where the user can view the raw images and select a
region-of-interest, "enhance" the region-of-interest, then crop for a final
enhanced product image. These steps can be represented by stages: Examine,
Enhance, Crop.)

### GUI Layouts

The GUILayout class represents a layout of widgets to use in a GUIPlugin stage.
The main window in Xi-cam is organized in a 3 x 3 grid. 
These cells in the grid are named according to their positions in the grid: 
center, top, bottom, left, lefttop, leftbottom, right, righttop, rightbottom. 

When creating a GUILayout, a *center* widget must be provided; 
the other positions are optional. 
Also note that the *lefttop* and *left* widgets are already occupied 
by the main window's preview widget
and data resource browser (i.e. file browser), respectively.
Although it is possible to provide your own *left* and *lefttop* widgets,
it is not recommended as it will replace those main window widgets.

### Data Models

### GUIPlugin header methods

*If you have a custom file format or a file format is not already handled by Xi-cam's DataHandlerPlugins, you will need to
implement your own. Please see [DataHandlerPlugin](TODO -- broken link) for more detailed information about writing
your own DataHandlerPlugin.*

```TODO -- is there a way to easily see registered data handlers? (.hdf, .jpg, .bin, etc. are currently loadable)```

The GUIPlugin class provides an interface for storing and accessing data within
your derived GUIPlugin. The interface methods are appendHeader, currentheader, and headers.

```TODO -- hook in GUIPlugin documentation here...```

**appendHeader** is intended to be used to internalize data in your derived GUIPlugin.

**currentheader** is intended to be used to retrieve the current (active, focused, etc.) internalized data.

**headers** is used to get a list of all of the data items in the data model.

### Workflows

## Implementation

After reviewing the core concepts, we can start implementing our own GUIPlugin.
We will create a simple GUIPlugin that allows viewing loaded images, then we
will extend that plugin with more features until we have a MovieEnhance plugin.

When first starting to write Xi-cam GUIPlugins, it is recommended to use a `cookiecutter`
template to set up some basic code and infrastructure for you.

### Using cookiecutter to Create the Plugin
[cookiecutter](https://cookiecutter.readthedocs.io/en/latest/readme.html) is a tool for creating
python projects from a template file.

There is a Xi-cam GUIPlugin template for cookiecutter that helps set up some packaging infrastructure
and boiler-plate code for a GUIPlugin. Follow the instructions here:
[Xi-cam.templates.GuiPlugin repo](https://github.com/synchrotrons/Xi-cam.templates.GuiPlugin).

When cookiecutter is run with the GUIPlugin template file, it will prompt for some information
that is used to create the package. Most of the prompts will have default values, indicated
as `[somevalue]` next to the prompt.

Here are the prompts with descriptions and values that we will use:

prompt | description | our value
--- | --- | ---
package_name     | name of the plugin package (also the name displayed in Xi-cam)     | mydemo
display_name     | name of plugin (shows up in docs and README)                       | My Demo Plugin
plugin_version   | current plugin version number                                      |
plugin_file_name | file to put the generated plugin code into                         |
author_name      | name of the plugin's author                                        | \<Your Name\>
author_email     | author's email                                                     | \<Your Email\>
author_url       | url for the author/plugin (this is used as the plugin repo url)    | \<Your Plugin Repo\>
description      | description of the plugin                                          | Demonstrates a simple GUIPlugin
keywords         | keywords to tag the plugin with                                    |
dependencies     | packages the plugin depends on                                     | 
plugin_code      | additional code to put in the plugin implementation file           |
stages_code      | python dictionary to set the plugin's stages to                    |
yapsy_ext        | file extension of the plugin marker file                           |

This generates the following in your current directory:

```
Xi-cam.plugins.mydemo/
  docs/
    ...
  LICENSE.md
  MANIFEST.in
  README.md
  requirements.txt
  setup.cfg
  setup.py
  tests/
    ...
  update_docs.sh
  xicam/
    mydemo/
      __init__.py
      mydemo.yapsy-plugin
```

#### Setting up VCS (Version Control System)

You will need to initialize the directory cookiecutter created, `Xi-cam.plugins.mydemo`, 
as a repository:

```
cd Xi-cam.plugins.mydemo
git init .
```

### Creating the Plugin and the Plugin Marker File without cookiecutter

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
        
        enhanceWidget = QLabel('An enhance widget would eventually replace this label')
        cropWidget = QLabel('A crop widget would eventually replace this label')
        # Set up stages
        self.stages = {
            'Examine': GUILayout(self.examineView),
            'Enhance': GUILayout(enhanceWidget),
            'Crop': GUILayout(cropWidget)
        }
        
        super(MovieEnhancePlugin, self).__init__(self)
```
)

### Installing the plugin

After creating the plugin, we need to tell Xi-cam that it is available to use. One way to do this is to create an
editable pip install. Make sure you are in your plugin's directory (Xi-cam.plugins.mydemo), then run:

```
pip install -e .
```

This will allow Xi-cam to see your plugin and load it.

### Verifying

Run xicam to verify that your plugin loads properly.
At the top-right of the Xi-cam main window, you should see *mydemo*.
When you click it, you should see the text *Stage 1* in the middle of the main window.

