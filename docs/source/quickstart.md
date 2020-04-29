# QuickStart Guide

This is a quick-start guide that will help you install Xi-CAM
and create a simple plugin inside of Xi-CAM.
For more in-depth documentation, see:

* GUIPlugin documentation
* OperationPlugin documentation
* Workflow documentation
* API Reference

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
[here](https://github.com/Xi-CAM/Xi-CAM.QuickStartPlugin).

## GUIPlugin

First, we need to create and install a GUIPlugin for Xi-CAM.
A GUIPlugin is the user-facing plugin that you will see when loading Xi-CAM.

For purposes of this quick-start tutorial,
we will create a GUIPlugin named "Quick Start Plugin".


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