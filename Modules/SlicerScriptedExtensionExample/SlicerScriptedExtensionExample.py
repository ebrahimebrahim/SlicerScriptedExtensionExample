import qt

from slicer.ScriptedLoadableModule import ScriptedLoadableModule, ScriptedLoadableModuleWidget


class SlicerScriptedExtensionExample(ScriptedLoadableModule):
    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        parent.title = "Scripted Extension Example"
        parent.categories = ["Examples"]
        parent.contributors = ["Slicer Developer"]
        parent.helpText = "Minimal extension used to test source-scripted installs."
        parent.acknowledgementText = "Created for source-scripted extension install testing."


class SlicerScriptedExtensionExampleWidget(ScriptedLoadableModuleWidget):
    def setup(self):
        ScriptedLoadableModuleWidget.setup(self)

        label = qt.QLabel("Scripted extension installed from source loaded successfully.")
        label.setWordWrap(True)
        self.layout.addWidget(label)
        self.layout.addStretch(1)
