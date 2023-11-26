# invert_clipboard_image
读取剪贴板中的图片，反色后写入剪贴板

# requirements
PyQt4 from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4

Python 2.7

# 使用Chat GPT生成代码

以下内容使用Chat GPT生成

To add a GUI using PyQt4 to your image manipulation script, you'll need to create a PyQt4 application and connect it with your existing functionality. Below is a simple example of how you can integrate a PyQt4 GUI with your image manipulation script:

First, make sure to install PyQt4 if you haven't already:

```bash
pip install PyQt4
```

Now, you can modify your script as follows:

```python
from PyQt4 import QtGui
from PIL import ImageGrab, Image
from io import BytesIO
import win32clipboard
import sys

class ImageInverterApp(QtGui.QWidget):
    def __init__(self):
        super(ImageInverterApp, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Inverter')

        self.btnLoad = QtGui.QPushButton('Load from Clipboard', self)
        self.btnLoad.clicked.connect(self.load_image_from_clipboard)

        self.btnInvert = QtGui.QPushButton('Invert Colors', self)
        self.btnInvert.clicked.connect(self.invert_image_colors)

        self.btnSave = QtGui.QPushButton('Save to Clipboard', self)
        self.btnSave.clicked.connect(self.save_image_to_clipboard)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.btnLoad)
        vbox.addWidget(self.btnInvert)
        vbox.addWidget(self.btnSave)

        self.setLayout(vbox)

    def load_image_from_clipboard(self):
        try:
            self.original_image = self.get_image_from_clipboard()
            QtGui.QMessageBox.information(self, 'Success', 'Image loaded from clipboard successfully.')
        except Exception as e:
            QtGui.QMessageBox.warning(self, 'Error', str(e))

    def invert_image_colors(self):
        if hasattr(self, 'original_image'):
            self.inverted_image = self.invert_image_colors_func(self.original_image)
            QtGui.QMessageBox.information(self, 'Success', 'Image colors inverted successfully.')
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'No image loaded.')

    def save_image_to_clipboard(self):
        if hasattr(self, 'inverted_image'):
            self.set_image_to_clipboard(self.inverted_image)
            QtGui.QMessageBox.information(self, 'Success', 'Inverted image saved to clipboard successfully.')
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'No inverted image available.')

    def get_image_from_clipboard(self):
        im = ImageGrab.grabclipboard()
        if im is not None:
            return im.convert("RGB")
        else:
            raise Exception("No image found in the clipboard.")

    def invert_image_colors_func(self, image):
        return Image.eval(image, lambda x: 255 - x)

    def set_image_to_clipboard(self, image):
        output = BytesIO()
        image.save(output, format="BMP")
        data = output.getvalue()[14:]
        output.close()

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = ImageInverterApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

```

This script creates a simple PyQt4 application with three buttons: one for loading an image from the clipboard, one for inverting the colors, and one for saving the inverted image back to the clipboard. The functionality of loading, inverting, and saving is encapsulated in the corresponding methods.

Run this script, and a window with the buttons should appear. Click the buttons to perform the respective actions. Note that you might need to adapt the script further based on your specific needs and preferences.
