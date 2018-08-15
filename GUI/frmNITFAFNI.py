#!/usr/bin/env python3
import os
import sys

import numpy as np
import scipy.io as io

import nibabel as nb
import subprocess as sub

from PyQt5.QtWidgets import *
from sklearn import preprocessing

from Base.utility import strRange

from Base.utility import getVersion, getBuild, getDirSpaceINI, getDirSpace
from GUI.frmNITFAFNIGUI import *

class frmNITFAFNI(Ui_frmNITFAFNI):
    ui = Ui_frmNITFAFNI()
    dialog = None
    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self):
        global dialog
        global ui
        ui = Ui_frmNITFAFNI()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        dialog = QtWidgets.QMainWindow()
        ui.setupUi(dialog)
        self.set_events(self)


        p = sub.Popen(['which', '3dcopy'], stdout=sub.PIPE, stderr=sub.PIPE)
        FAFNI, errors = p.communicate()
        FAFNI = FAFNI.decode("utf-8").replace("\n","")
        if not len(FAFNI):
            print("Cannot find 3dcopy Path!")
        elif not os.path.isfile(FAFNI):
            print("Cannot find 3dcopy binary file!")
        else:
            ui.txtFAFNI.setText(FAFNI)

        p = sub.Popen(['which', '3drefit'], stdout=sub.PIPE, stderr=sub.PIPE)
        FSUMA, errors = p.communicate()
        FSUMA = FSUMA.decode("utf-8").replace("\n","")
        if not len(FSUMA):
            print("Cannot find 3drefit Path!")
        elif not os.path.isfile(FSUMA):
            print("Cannot find 3drefit binary file!")
        else:
            ui.txtFSUMA.setText(FSUMA)



        dialog.setWindowTitle("easy fMRI Convert Nifti1 to AFNI - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()


    # This function initiate the events procedures
    def set_events(self):
        global ui
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnInFile.clicked.connect(self.btnInFile_click)
        ui.btnAFNI.clicked.connect(self.btnAFNI_click)
        ui.btnConvert.clicked.connect(self.btnConvert_click)
        ui.btnFAFNI.clicked.connect(self.btnFAFNI_click)
        ui.btnFSUMA.clicked.connect(self.btnFSUMA_click)


    def btnClose_click(self):
        global dialog
        dialog.close()


    def btnInFile_click(self):
        fdialog = QFileDialog()
        filename = fdialog.getOpenFileName(None, "Open image file ...", os.path.dirname(ui.txtInFile.text()),
                                           options=QFileDialog.DontUseNativeDialog)
        filename = filename[0]
        if len(filename):
            if os.path.isfile(filename):
                ui.txtInFile.setText(filename)

    def btnFAFNI_click(self):
        fdialog = QFileDialog()
        filename = fdialog.getOpenFileName(None, "Open AFNI file ...", os.path.dirname(ui.txtFAFNI.text()),
                                           options=QFileDialog.DontUseNativeDialog)[0]
        if len(filename):
            if os.path.isfile(filename):
                ui.txtFAFNI.setText(filename)

    def btnFSUMA_click(self):
        fdialog = QFileDialog()
        filename = fdialog.getOpenFileName(None, "Open SUMA file ...", os.path.dirname(ui.txtFSUMA.text()),
                                           options=QFileDialog.DontUseNativeDialog)[0]
        if len(filename):
            if os.path.isfile(filename):
                ui.txtFSUMA.setText(filename)


    def btnAFNI_click(self):
        global ui
        current = ui.txtAFNI.text()
        if not len(current):
            current = os.getcwd()
        flags = QFileDialog.DontUseNativeDialog
        dialog = QFileDialog()
        ofile = dialog.getSaveFileName(None, "Output File", current, "", "", flags)[0]
        if len(ofile):
            ui.txtAFNI.setText(ofile)


    def btnConvert_click(self):
        msgBox = QMessageBox()

        # InFile
        InFile = ui.txtInFile.text()
        if not len(InFile):
            msgBox.setText("Please enter input file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        if not os.path.isfile(InFile):
            msgBox.setText("Input file not found!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        # OutFile
        AFNI = ui.txtAFNI.text()
        if not len(AFNI):
            msgBox.setText("Please enter output file!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        CopyFile = ui.txtFAFNI.text()
        if not len(CopyFile):
            msgBox.setText("Please select 3dcopy command!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        if not os.path.isfile(CopyFile):
            msgBox.setText("Please select 3dcopy command!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        RefitFile = ui.txtFSUMA.text()
        if not len(RefitFile):
            msgBox.setText("Please select 3drefit command!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return
        if not os.path.isfile(RefitFile):
            msgBox.setText("Please select 3drefit command!")
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            return

        print("Saving image ...")
        cmd = CopyFile + " " + InFile + " " + AFNI
        print("Running: " + cmd)
        os.system(cmd)
        cmd = RefitFile + "  -view tlrc -space MNI " + AFNI + " " + AFNI + "+tlrc."
        print("Running: " + cmd)
        os.system(cmd)
        print("DONE!")

        msgBox.setText("Image file is generated.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frmNITFAFNI.show(frmNITFAFNI)
    sys.exit(app.exec_())