# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmFESPCAGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmFESPCA(object):
    def setupUi(self, frmFESPCA):
        frmFESPCA.setObjectName("frmFESPCA")
        frmFESPCA.resize(758, 741)
        self.btnInFile = QtWidgets.QPushButton(frmFESPCA)
        self.btnInFile.setGeometry(QtCore.QRect(690, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.label_33 = QtWidgets.QLabel(frmFESPCA)
        self.label_33.setGeometry(QtCore.QRect(30, 20, 131, 16))
        self.label_33.setObjectName("label_33")
        self.btnOutFile = QtWidgets.QPushButton(frmFESPCA)
        self.btnOutFile.setGeometry(QtCore.QRect(690, 60, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.txtInFile = QtWidgets.QLineEdit(frmFESPCA)
        self.txtInFile.setGeometry(QtCore.QRect(160, 20, 521, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnConvert = QtWidgets.QPushButton(frmFESPCA)
        self.btnConvert.setGeometry(QtCore.QRect(590, 690, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.label_35 = QtWidgets.QLabel(frmFESPCA)
        self.label_35.setGeometry(QtCore.QRect(30, 60, 111, 16))
        self.label_35.setObjectName("label_35")
        self.txtOutFile = QtWidgets.QLineEdit(frmFESPCA)
        self.txtOutFile.setGeometry(QtCore.QRect(160, 60, 521, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnClose = QtWidgets.QPushButton(frmFESPCA)
        self.btnClose.setGeometry(QtCore.QRect(30, 690, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.tabWidget = QtWidgets.QTabWidget(frmFESPCA)
        self.tabWidget.setGeometry(QtCore.QRect(30, 100, 701, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.txtOTask = QtWidgets.QLineEdit(self.tab)
        self.txtOTask.setGeometry(QtCore.QRect(420, 290, 113, 21))
        self.txtOTask.setObjectName("txtOTask")
        self.txtmLabel = QtWidgets.QComboBox(self.tab)
        self.txtmLabel.setGeometry(QtCore.QRect(260, 170, 121, 26))
        self.txtmLabel.setEditable(True)
        self.txtmLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtmLabel.setObjectName("txtmLabel")
        self.cbmLabel = QtWidgets.QCheckBox(self.tab)
        self.cbmLabel.setGeometry(QtCore.QRect(140, 170, 111, 20))
        self.cbmLabel.setObjectName("cbmLabel")
        self.txtScan = QtWidgets.QComboBox(self.tab)
        self.txtScan.setGeometry(QtCore.QRect(260, 450, 121, 26))
        self.txtScan.setEditable(True)
        self.txtScan.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtScan.setObjectName("txtScan")
        self.txtTask = QtWidgets.QComboBox(self.tab)
        self.txtTask.setGeometry(QtCore.QRect(260, 290, 121, 26))
        self.txtTask.setEditable(True)
        self.txtTask.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtTask.setObjectName("txtTask")
        self.txtSubject = QtWidgets.QComboBox(self.tab)
        self.txtSubject.setGeometry(QtCore.QRect(260, 130, 121, 26))
        self.txtSubject.setEditable(True)
        self.txtSubject.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtSubject.setObjectName("txtSubject")
        self.txtOmLabel = QtWidgets.QLineEdit(self.tab)
        self.txtOmLabel.setGeometry(QtCore.QRect(420, 170, 113, 21))
        self.txtOmLabel.setObjectName("txtOmLabel")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 60, 16))
        self.label_2.setObjectName("label_2")
        self.txtODM = QtWidgets.QLineEdit(self.tab)
        self.txtODM.setGeometry(QtCore.QRect(420, 250, 113, 21))
        self.txtODM.setObjectName("txtODM")
        self.cbTask = QtWidgets.QCheckBox(self.tab)
        self.cbTask.setGeometry(QtCore.QRect(140, 290, 81, 20))
        self.cbTask.setChecked(True)
        self.cbTask.setObjectName("cbTask")
        self.txtDM = QtWidgets.QComboBox(self.tab)
        self.txtDM.setGeometry(QtCore.QRect(260, 250, 121, 26))
        self.txtDM.setEditable(True)
        self.txtDM.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtDM.setObjectName("txtDM")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(140, 90, 60, 16))
        self.label_3.setObjectName("label_3")
        self.cbNScan = QtWidgets.QCheckBox(self.tab)
        self.cbNScan.setGeometry(QtCore.QRect(140, 450, 91, 20))
        self.cbNScan.setChecked(False)
        self.cbNScan.setObjectName("cbNScan")
        self.cbCond = QtWidgets.QCheckBox(self.tab)
        self.cbCond.setGeometry(QtCore.QRect(140, 410, 101, 20))
        self.cbCond.setChecked(True)
        self.cbCond.setObjectName("cbCond")
        self.cbDM = QtWidgets.QCheckBox(self.tab)
        self.cbDM.setGeometry(QtCore.QRect(140, 250, 121, 20))
        self.cbDM.setChecked(False)
        self.cbDM.setObjectName("cbDM")
        self.txtCol = QtWidgets.QComboBox(self.tab)
        self.txtCol.setGeometry(QtCore.QRect(260, 210, 121, 26))
        self.txtCol.setEditable(True)
        self.txtCol.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCol.setObjectName("txtCol")
        self.cbCol = QtWidgets.QCheckBox(self.tab)
        self.cbCol.setGeometry(QtCore.QRect(140, 210, 111, 20))
        self.cbCol.setChecked(True)
        self.cbCol.setObjectName("cbCol")
        self.txtOCond = QtWidgets.QLineEdit(self.tab)
        self.txtOCond.setGeometry(QtCore.QRect(420, 410, 113, 21))
        self.txtOCond.setObjectName("txtOCond")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(300, 20, 61, 16))
        self.label.setObjectName("label")
        self.txtOLabel = QtWidgets.QLineEdit(self.tab)
        self.txtOLabel.setGeometry(QtCore.QRect(420, 90, 113, 21))
        self.txtOLabel.setObjectName("txtOLabel")
        self.txtCounter = QtWidgets.QComboBox(self.tab)
        self.txtCounter.setGeometry(QtCore.QRect(260, 370, 121, 26))
        self.txtCounter.setEditable(True)
        self.txtCounter.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCounter.setObjectName("txtCounter")
        self.txtLabel = QtWidgets.QComboBox(self.tab)
        self.txtLabel.setGeometry(QtCore.QRect(260, 90, 121, 26))
        self.txtLabel.setEditable(True)
        self.txtLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtLabel.setObjectName("txtLabel")
        self.txtOScan = QtWidgets.QLineEdit(self.tab)
        self.txtOScan.setGeometry(QtCore.QRect(420, 450, 113, 21))
        self.txtOScan.setObjectName("txtOScan")
        self.cbCounter = QtWidgets.QCheckBox(self.tab)
        self.cbCounter.setGeometry(QtCore.QRect(140, 370, 81, 20))
        self.cbCounter.setChecked(False)
        self.cbCounter.setObjectName("cbCounter")
        self.txtOCol = QtWidgets.QLineEdit(self.tab)
        self.txtOCol.setGeometry(QtCore.QRect(420, 210, 113, 21))
        self.txtOCol.setObjectName("txtOCol")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(450, 20, 61, 16))
        self.label_5.setObjectName("label_5")
        self.txtData = QtWidgets.QComboBox(self.tab)
        self.txtData.setGeometry(QtCore.QRect(260, 50, 121, 26))
        self.txtData.setEditable(True)
        self.txtData.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtData.setObjectName("txtData")
        self.txtRun = QtWidgets.QComboBox(self.tab)
        self.txtRun.setGeometry(QtCore.QRect(260, 330, 121, 26))
        self.txtRun.setEditable(True)
        self.txtRun.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtRun.setObjectName("txtRun")
        self.txtCond = QtWidgets.QComboBox(self.tab)
        self.txtCond.setGeometry(QtCore.QRect(260, 410, 121, 26))
        self.txtCond.setEditable(True)
        self.txtCond.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCond.setObjectName("txtCond")
        self.txtOCounter = QtWidgets.QLineEdit(self.tab)
        self.txtOCounter.setGeometry(QtCore.QRect(420, 370, 113, 21))
        self.txtOCounter.setObjectName("txtOCounter")
        self.txtOSubject = QtWidgets.QLineEdit(self.tab)
        self.txtOSubject.setGeometry(QtCore.QRect(420, 130, 113, 21))
        self.txtOSubject.setObjectName("txtOSubject")
        self.cbRun = QtWidgets.QCheckBox(self.tab)
        self.cbRun.setGeometry(QtCore.QRect(140, 330, 81, 20))
        self.cbRun.setChecked(True)
        self.cbRun.setObjectName("cbRun")
        self.txtOData = QtWidgets.QLineEdit(self.tab)
        self.txtOData.setGeometry(QtCore.QRect(420, 50, 113, 21))
        self.txtOData.setObjectName("txtOData")
        self.txtORun = QtWidgets.QLineEdit(self.tab)
        self.txtORun.setGeometry(QtCore.QRect(420, 330, 113, 21))
        self.txtORun.setObjectName("txtORun")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(140, 130, 60, 16))
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.txtNumFea = QtWidgets.QSpinBox(self.tab_2)
        self.txtNumFea.setGeometry(QtCore.QRect(220, 200, 160, 24))
        self.txtNumFea.setMinimum(1)
        self.txtNumFea.setObjectName("txtNumFea")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 141, 16))
        self.label_4.setObjectName("label_4")
        self.lblFeaNum = QtWidgets.QLabel(self.tab_2)
        self.lblFeaNum.setGeometry(QtCore.QRect(400, 200, 191, 16))
        self.lblFeaNum.setObjectName("lblFeaNum")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 641, 80))
        self.groupBox.setObjectName("groupBox")
        self.cbScale = QtWidgets.QCheckBox(self.groupBox)
        self.cbScale.setGeometry(QtCore.QRect(20, 40, 191, 20))
        self.cbScale.setChecked(True)
        self.cbScale.setObjectName("cbScale")
        self.rbScale = QtWidgets.QRadioButton(self.groupBox)
        self.rbScale.setGeometry(QtCore.QRect(210, 40, 161, 20))
        self.rbScale.setChecked(True)
        self.rbScale.setObjectName("rbScale")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(370, 40, 131, 20))
        self.radioButton.setObjectName("radioButton")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(30, 240, 141, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(30, 280, 151, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(30, 320, 141, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(30, 360, 141, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(30, 400, 171, 16))
        self.label_11.setObjectName("label_11")
        self.txtAlpha = QtWidgets.QLineEdit(self.tab_2)
        self.txtAlpha.setGeometry(QtCore.QRect(220, 240, 160, 21))
        self.txtAlpha.setObjectName("txtAlpha")
        self.txtRidge = QtWidgets.QLineEdit(self.tab_2)
        self.txtRidge.setGeometry(QtCore.QRect(220, 280, 160, 21))
        self.txtRidge.setObjectName("txtRidge")
        self.txtMaxIter = QtWidgets.QLineEdit(self.tab_2)
        self.txtMaxIter.setGeometry(QtCore.QRect(220, 320, 160, 21))
        self.txtMaxIter.setObjectName("txtMaxIter")
        self.txtTole = QtWidgets.QLineEdit(self.tab_2)
        self.txtTole.setGeometry(QtCore.QRect(220, 360, 160, 21))
        self.txtTole.setObjectName("txtTole")
        self.txtJobs = QtWidgets.QLineEdit(self.tab_2)
        self.txtJobs.setGeometry(QtCore.QRect(220, 400, 160, 21))
        self.txtJobs.setObjectName("txtJobs")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 440, 641, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(150, 40, 111, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.rbLars = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbLars.setGeometry(QtCore.QRect(30, 40, 111, 20))
        self.rbLars.setChecked(True)
        self.rbLars.setObjectName("rbLars")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 100, 641, 80))
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_2.setGeometry(QtCore.QRect(190, 40, 131, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.rbALScale = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbALScale.setGeometry(QtCore.QRect(30, 40, 161, 20))
        self.rbALScale.setChecked(True)
        self.rbALScale.setObjectName("rbALScale")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(frmFESPCA)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmFESPCA)
        frmFESPCA.setTabOrder(self.txtInFile, self.btnInFile)
        frmFESPCA.setTabOrder(self.btnInFile, self.txtOutFile)
        frmFESPCA.setTabOrder(self.txtOutFile, self.btnOutFile)
        frmFESPCA.setTabOrder(self.btnOutFile, self.tabWidget)
        frmFESPCA.setTabOrder(self.tabWidget, self.cbmLabel)
        frmFESPCA.setTabOrder(self.cbmLabel, self.cbCol)
        frmFESPCA.setTabOrder(self.cbCol, self.cbDM)
        frmFESPCA.setTabOrder(self.cbDM, self.cbTask)
        frmFESPCA.setTabOrder(self.cbTask, self.cbRun)
        frmFESPCA.setTabOrder(self.cbRun, self.cbCounter)
        frmFESPCA.setTabOrder(self.cbCounter, self.cbCond)
        frmFESPCA.setTabOrder(self.cbCond, self.cbNScan)
        frmFESPCA.setTabOrder(self.cbNScan, self.txtData)
        frmFESPCA.setTabOrder(self.txtData, self.txtLabel)
        frmFESPCA.setTabOrder(self.txtLabel, self.txtSubject)
        frmFESPCA.setTabOrder(self.txtSubject, self.txtmLabel)
        frmFESPCA.setTabOrder(self.txtmLabel, self.txtCol)
        frmFESPCA.setTabOrder(self.txtCol, self.txtDM)
        frmFESPCA.setTabOrder(self.txtDM, self.txtTask)
        frmFESPCA.setTabOrder(self.txtTask, self.txtRun)
        frmFESPCA.setTabOrder(self.txtRun, self.txtCounter)
        frmFESPCA.setTabOrder(self.txtCounter, self.txtScan)
        frmFESPCA.setTabOrder(self.txtScan, self.txtOData)
        frmFESPCA.setTabOrder(self.txtOData, self.txtOLabel)
        frmFESPCA.setTabOrder(self.txtOLabel, self.txtOSubject)
        frmFESPCA.setTabOrder(self.txtOSubject, self.txtOmLabel)
        frmFESPCA.setTabOrder(self.txtOmLabel, self.txtOCol)
        frmFESPCA.setTabOrder(self.txtOCol, self.txtODM)
        frmFESPCA.setTabOrder(self.txtODM, self.txtOTask)
        frmFESPCA.setTabOrder(self.txtOTask, self.txtORun)
        frmFESPCA.setTabOrder(self.txtORun, self.txtOCounter)
        frmFESPCA.setTabOrder(self.txtOCounter, self.txtOCond)
        frmFESPCA.setTabOrder(self.txtOCond, self.txtOScan)
        frmFESPCA.setTabOrder(self.txtOScan, self.txtCond)
        frmFESPCA.setTabOrder(self.txtCond, self.cbScale)
        frmFESPCA.setTabOrder(self.cbScale, self.rbScale)
        frmFESPCA.setTabOrder(self.rbScale, self.radioButton)
        frmFESPCA.setTabOrder(self.radioButton, self.txtNumFea)
        frmFESPCA.setTabOrder(self.txtNumFea, self.btnConvert)
        frmFESPCA.setTabOrder(self.btnConvert, self.btnClose)

    def retranslateUi(self, frmFESPCA):
        _translate = QtCore.QCoreApplication.translate
        frmFESPCA.setWindowTitle(_translate("frmFESPCA", "Sparse Principal Component Analysis (PCA)"))
        self.btnInFile.setText(_translate("frmFESPCA", "..."))
        self.label_33.setText(_translate("frmFESPCA", "Input Data"))
        self.btnOutFile.setText(_translate("frmFESPCA", "..."))
        self.btnConvert.setText(_translate("frmFESPCA", "Convert"))
        self.label_35.setText(_translate("frmFESPCA", "Output Data"))
        self.btnClose.setText(_translate("frmFESPCA", "Close"))
        self.txtOTask.setText(_translate("frmFESPCA", "task"))
        self.cbmLabel.setText(_translate("frmFESPCA", "Label (matrix)"))
        self.txtOmLabel.setText(_translate("frmFESPCA", "mlabel"))
        self.label_2.setText(_translate("frmFESPCA", "Data"))
        self.txtODM.setText(_translate("frmFESPCA", "design"))
        self.cbTask.setText(_translate("frmFESPCA", "Task"))
        self.label_3.setText(_translate("frmFESPCA", "Label"))
        self.cbNScan.setText(_translate("frmFESPCA", "NScan"))
        self.cbCond.setText(_translate("frmFESPCA", "Condition"))
        self.cbDM.setText(_translate("frmFESPCA", "Design Matrix"))
        self.cbCol.setText(_translate("frmFESPCA", "Coordinate"))
        self.txtOCond.setText(_translate("frmFESPCA", "condition"))
        self.label.setText(_translate("frmFESPCA", "Input"))
        self.txtOLabel.setText(_translate("frmFESPCA", "label"))
        self.txtOScan.setText(_translate("frmFESPCA", "nscan"))
        self.cbCounter.setText(_translate("frmFESPCA", "Counter"))
        self.txtOCol.setText(_translate("frmFESPCA", "coordinate"))
        self.label_5.setText(_translate("frmFESPCA", "Output"))
        self.txtOCounter.setText(_translate("frmFESPCA", "counter"))
        self.txtOSubject.setText(_translate("frmFESPCA", "subject"))
        self.cbRun.setText(_translate("frmFESPCA", "Run"))
        self.txtOData.setText(_translate("frmFESPCA", "data"))
        self.txtORun.setText(_translate("frmFESPCA", "run"))
        self.label_6.setText(_translate("frmFESPCA", "Subject"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmFESPCA", "Data"))
        self.label_4.setText(_translate("frmFESPCA", "Number of features"))
        self.lblFeaNum.setText(_translate("frmFESPCA", "No Data"))
        self.groupBox.setTitle(_translate("frmFESPCA", "<Input Data Normalization>"))
        self.cbScale.setText(_translate("frmFESPCA", "Scale Data X~N(0,1)"))
        self.rbScale.setText(_translate("frmFESPCA", "Subject Level"))
        self.radioButton.setText(_translate("frmFESPCA", "Whole Data"))
        self.label_7.setText(_translate("frmFESPCA", "Alpha"))
        self.label_8.setText(_translate("frmFESPCA", "Ridge Alpha"))
        self.label_9.setText(_translate("frmFESPCA", "Maximum Iterations"))
        self.label_10.setText(_translate("frmFESPCA", "Tolerance"))
        self.label_11.setText(_translate("frmFESPCA", "Number of parallel jobs"))
        self.txtAlpha.setText(_translate("frmFESPCA", "1"))
        self.txtRidge.setText(_translate("frmFESPCA", "0.01"))
        self.txtMaxIter.setText(_translate("frmFESPCA", "1000"))
        self.txtTole.setText(_translate("frmFESPCA", "1e-08"))
        self.txtJobs.setText(_translate("frmFESPCA", "1"))
        self.groupBox_2.setTitle(_translate("frmFESPCA", "<Method>"))
        self.radioButton_3.setText(_translate("frmFESPCA", "cd"))
        self.rbLars.setText(_translate("frmFESPCA", "lars"))
        self.groupBox_3.setTitle(_translate("frmFESPCA", "<Analysis Level>"))
        self.radioButton_2.setText(_translate("frmFESPCA", "Whole Data"))
        self.rbALScale.setText(_translate("frmFESPCA", "Subject Level"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmFESPCA", "Parameters"))
