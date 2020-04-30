# QuickStart Guide

This is a quick-start guide that will help you install Xi-CAM
and create a simple plugin inside of Xi-CAM.

## Install Xi-CAM

If you haven't already installed Xi-CAM, follow the installation
instructions for your operating system:

* [Linux Installation](install-linux.md)
* [macOS Installation](install-macos.md)
* [Windows Installation](install-windows.md)

## Overview

Let's dive into an example first that we can explore.

We will create a `GUIPlugin` - 
this will be a plugin that you will be able to select and see within Xi-CAM.
We can define the looks and feel of the `GUIPlugin` by using a `GUILayout`.

We will also create a few `OperationPlugins` - 
These plugins are basically functions that take in data
and output derived data.

After creating some `OperationPlugins`,
we will need a way to actually run data through the operations.
To do this, we will add these `OperationPlugins` into a `Workflow`.
Then, we will create a button in the GUI to execute the workflow.

Note that starting code for this guide can be found
[here](https://github.com/Xi-CAM/Xi-CAM.ExamplePlugin).

## Xi-CAM Main Window

Let's look at what the main window looks like first:

```eval_rst
.. figure:: _static/xicam-main.png
  :alt: Xi-CAM main window after loading.

  The main window of Xi-CAM after it has finished loading.
```

When Xi-CAM finishes loading, we see the window as shown above.
Any installed plugins will be visible (and selectable) at the top
(note that you will probably not have any installed yet).

We can also see some of the default widgets provided:
* a welcome widget in the *center* of the window
* a preview widget in the top-left (*lefttop*) of the window
* a data browser widget on the *left* of the window

When creating our GUIPlugin, we will provide our own *center* widget,
but we will not be modifying the *lefttop* or the *left* widgets.

## GUIPlugin

Now that we have a basic overview of the Xi-CAM main window,
we need to create and install a GUIPlugin for Xi-CAM.

A GUIPlugin is the user-facing plugin that you will see when loading Xi-CAM
(they will show up in the top area of the main window).

### Clone the ExamplePlugin Repository

For purposes of this quick-start tutorial,
we will create a GUIPlugin named "Example Plugin".

Go ahead and open a terminal (or if on Windows, you can use your Anaconda prompt)
and make sure that your xicam environment that you created is active.

`cd` to a directory of your choice (like your home directory),
then get the starting code:

```bash
git clone https://github.com/Xi-CAM/Xi-CAM.ExamplePlugin
cd Xi-CAM.ExamplePlugin
```

### Install the ExamplePlugin

Now that we have downloaded the starting code for our `ExamplePlugin`,
we need to actually *install* the plugin so Xi-CAM can see it.

To do this, we use what's called an *editable pip install*.
Ensuring that you are in the `Xi-CAM.ExamplePlugin` directory, run:

```bash
pip install -e .
```

Next, run xicam:

```bash
xicam
```

You should now have "Example Plugin" appear at the top of your Xi-CAM window.

### Exploring the ExamplePlugin

Go ahead and click on the "Example Plugin" text;
this will select and activate the `ExamplePlugin` GUIPlugin.

```eval_rst
.. figure:: _static/xicam-example-plugin.png
  :alt: Interface for the Example Plugin

  The interface for the "Example Plugin".
```

Notice that the top has the "Example Plugin" selected.
All this GUIPlugin contains right now is the text "Stage 1..." in the center of the window.

### Modifying the ExamplePlugin

Let's make some modifications to the `ExamplePlugin` so it can load an image from a local databroker.

#### Configuring the Sample Databroker Catalog

First, we will need to configure a catalog.

There should be a `configure/` directory in the repository we cloned.
This contains a catalog configuration file, a msgpack catalog, and a script.

Feel free to inspect the script before you run it;
it will attempt to set up a msgpack catalog source for Xi-CAM to use:

```bash
cd configure
python setup_catalog.py
cd ..
```

#### Changing the Layout

#### Loading a Catalog 


## OperationPlugin

Now that we have our GUIPlugin created and installed in Xi-CAM,
we can start creating our operations.

An operation can be thought of as a function; input data is sent into the operation,
and the operation generates some output with the given input.

The OperationPlugin API makes use of python decorators for easily defining
and creating operations.

In the 

## Workflow


####NOTES TO SELF
* Write a demo repo for this, with good commits
* Quickstarting can be exploring the completed demo
* Need to provide catalog example data, catalog file, how to do...