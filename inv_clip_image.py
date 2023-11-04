# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import with_statement
from __future__ import unicode_literals
from __future__ import nested_scopes
from __future__ import generators
# Form implementation generated from reading ui file 'D:/Portable Python-2.7.17/venv/inv_clip_image/inv_clip_image.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(s):
        return s


try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(554, 339)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,
                                       QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.howToUse = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,
                                       QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.howToUse.sizePolicy().hasHeightForWidth())
        self.howToUse.setSizePolicy(sizePolicy)
        self.howToUse.setScaledContents(False)
        self.howToUse.setWordWrap(False)
        self.howToUse.setObjectName(_fromUtf8("howToUse"))
        self.verticalLayout.addWidget(self.howToUse)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.widget = QtGui.QWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,
                                       QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_im = QtGui.QLabel(self.widget)
        self.label_im.setMaximumSize(QtCore.QSize(256, 256))
        self.label_im.setText(_fromUtf8(""))
        # self.label_im.setPixmap(QtGui.QPixmap(_fromUtf8("77023588_p0.png")))
        self.label_im.setScaledContents(True)
        self.label_im.setWordWrap(False)
        self.label_im.setObjectName(_fromUtf8("label_im"))
        self.horizontalLayout.addWidget(self.label_im)
        self.label_invIm = QtGui.QLabel(self.widget)
        self.label_invIm.setMaximumSize(QtCore.QSize(256, 256))
        self.label_invIm.setText(_fromUtf8(""))
        # self.label_invIm.setPixmap(QtGui.QPixmap(_fromUtf8("77023588_p0.png")))
        self.label_invIm.setScaledContents(True)
        self.label_invIm.setObjectName(_fromUtf8("label_invIm"))
        self.horizontalLayout.addWidget(self.label_invIm)
        self.label_im.raise_()
        self.label_invIm.raise_()
        self.label_invIm.raise_()
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.startInv)
        self.im = ""
        self.Invim = ""

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "反色剪贴板中的图像", None))
        self.howToUse.setText(
            _translate("Form", "复制图片，点击开始，生成该图片的反色，写入剪贴板中", None))
        self.pushButton.setText(_translate("Form", "开始", None))

    def startInv(self):
        cb = QtGui.QApplication.clipboard()
        im = cb.image(mode=cb.Clipboard)
        if not im.isNull():
            self.im = QtGui.QPixmap(im)
            im.invertPixels()
            self.Invim = QtGui.QPixmap(im)
            self.label_im.setPixmap(self.im)
            self.label_invIm.setPixmap(self.Invim)
            cb.clear(mode=cb.Clipboard)
            cb.setImage(im, mode=cb.Clipboard)
            test = cb.image(mode=cb.Clipboard)
            i = 0
            # https://bugreports.qt.io/browse/QTBUG-27097
            while test.isNull():
                cb.clear(mode=cb.Clipboard)
                cb.setImage(im, mode=cb.Clipboard)
                test = cb.image(mode=cb.Clipboard)
                i = i + 1
                print(i)
                if i >= 5:
                    QtGui.QMessageBox.about(
                        None, 'about',
                        _translate(
                            "Form",
                            "QClipboard::setMimeData: Failed to set data on clipboard ()",
                            None))
                    break


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
