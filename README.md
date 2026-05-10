# SlicerScriptedExtensionExample

Minimal scripted extension for testing direct source installs in 3D Slicer.

NOTE: The functionality to install "from source" that is described below does not yet exist in Slicer. It is something I am experimenting with.

## Install Badge

[![Install in Slicer](https://img.shields.io/badge/Install%20in-Slicer-0084c7)](slicer://extensions/install-source?manifest=https%3A%2F%2Fraw.githubusercontent.com%2Febrahimebrahim%2FSlicerScriptedExtensionExample%2Fmain%2Fslicer-extension.json)

The badge opens Slicer with a remote manifest URL. The manifest's `installSource`
field tells Slicer to install this repository from Git.

## Direct Git Install

In Slicer, open the Extensions Manager, choose **Install from source...**, then
choose **Git...** and enter:

```text
https://github.com/ebrahimebrahim/SlicerScriptedExtensionExample.git
```

The ref will be `main` by default.
