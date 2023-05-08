# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QAbstractScrollArea, QGridLayout, QLabel,
                               QPushButton, QSizePolicy, QTextEdit, QWidget)


class Ui_Form(object):
    def setupUi(self, Form: QWidget):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(396, 589)
        font = QFont()
        font.setFamilies([u"Rubik"])
        Form.setFont(font)
        Form.setStyleSheet(open("data/style.css", 'r').read())
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 150, 410, 441))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.sqrt_btn = QPushButton(self.gridLayoutWidget)
        self.sqrt_btn.setObjectName(u"sqrt_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sqrt_btn.sizePolicy().hasHeightForWidth())
        self.sqrt_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.sqrt_btn, 1, 2, 1, 1)

        self.cos_btn = QPushButton(self.gridLayoutWidget)
        self.cos_btn.setObjectName(u"cos_btn")
        sizePolicy.setHeightForWidth(self.cos_btn.sizePolicy().hasHeightForWidth())
        self.cos_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.cos_btn, 1, 1, 1, 1)

        self.n8_btn = QPushButton(self.gridLayoutWidget)
        self.n8_btn.setObjectName(u"n8_btn")
        sizePolicy.setHeightForWidth(self.n8_btn.sizePolicy().hasHeightForWidth())
        self.n8_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.n8_btn, 2, 1, 1, 1)

        self.n9_btn = QPushButton(self.gridLayoutWidget)
        self.n9_btn.setObjectName(u"n9_btn")
        sizePolicy.setHeightForWidth(self.n9_btn.sizePolicy().hasHeightForWidth())
        self.n9_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.n9_btn, 2, 2, 1, 1)

        self.n6_btn = QPushButton(self.gridLayoutWidget)
        self.n6_btn.setObjectName(u"n6_btn")
        sizePolicy.setHeightForWidth(self.n6_btn.sizePolicy().hasHeightForWidth())
        self.n6_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.n6_btn, 3, 2, 1, 1)

        self.n3_btn = QPushButton(self.gridLayoutWidget)
        self.n3_btn.setObjectName(u"n3_btn")
        sizePolicy.setHeightForWidth(self.n3_btn.sizePolicy().hasHeightForWidth())
        self.n3_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.n3_btn, 4, 2, 1, 1)

        self.division_btn = QPushButton(self.gridLayoutWidget)
        self.division_btn.setObjectName(u"division_btn")
        sizePolicy.setHeightForWidth(self.division_btn.sizePolicy().hasHeightForWidth())
        self.division_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.division_btn, 4, 3, 1, 1)

        self.equals_btn = QPushButton(self.gridLayoutWidget)
        self.equals_btn.setObjectName(u"equals_btn")
        sizePolicy.setHeightForWidth(self.equals_btn.sizePolicy().hasHeightForWidth())
        self.equals_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.equals_btn, 5, 3, 1, 1)

        self.add_btn = QPushButton(self.gridLayoutWidget)
        self.add_btn.setObjectName(u"add_btn")
        sizePolicy.setHeightForWidth(self.add_btn.sizePolicy().hasHeightForWidth())
        self.add_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.add_btn, 1, 3, 1, 1)

        self.multiply_btn = QPushButton(self.gridLayoutWidget)
        self.multiply_btn.setObjectName(u"multiply_btn")
        sizePolicy.setHeightForWidth(self.multiply_btn.sizePolicy().hasHeightForWidth())
        self.multiply_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.multiply_btn, 3, 3, 1, 1)

        self.subst_btn = QPushButton(self.gridLayoutWidget)
        self.subst_btn.setObjectName(u"subst_btn")
        sizePolicy.setHeightForWidth(self.subst_btn.sizePolicy().hasHeightForWidth())
        self.subst_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.subst_btn, 2, 3, 1, 1)

        self.dot_btn = QPushButton(self.gridLayoutWidget)
        self.dot_btn.setObjectName(u"dot_btn")
        sizePolicy.setHeightForWidth(self.dot_btn.sizePolicy().hasHeightForWidth())
        self.dot_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.dot_btn, 5, 2, 1, 1)

        self.to_num = QPushButton(self.gridLayoutWidget)
        self.to_num.setObjectName(u"to_num")
        sizePolicy.setHeightForWidth(self.to_num.sizePolicy().hasHeightForWidth())
        self.to_num.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.to_num, 5, 0, 1, 1)

        self.sin_btn = QPushButton(self.gridLayoutWidget)
        self.sin_btn.setObjectName(u"sin_btn")
        sizePolicy.setHeightForWidth(self.sin_btn.sizePolicy().hasHeightForWidth())
        self.sin_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.sin_btn, 1, 0, 1, 1)

        self.n4_btn = QPushButton(self.gridLayoutWidget)
        self.n4_btn.setObjectName(u"n4_btn")
        sizePolicy.setHeightForWidth(self.n4_btn.sizePolicy().hasHeightForWidth())
        self.n4_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.n4_btn, 3, 0, 1, 1)

        self.n1_btn = QPushButton(self.gridLayoutWidget)
        self.n1_btn.setObjectName(u"n1_btn")
        sizePolicy.setHeightForWidth(self.n1_btn.sizePolicy().hasHeightForWidth())
        self.n1_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.n1_btn, 4, 0, 1, 1)

        self.n5_btn = QPushButton(self.gridLayoutWidget)
        self.n5_btn.setObjectName(u"n5_btn")
        sizePolicy.setHeightForWidth(self.n5_btn.sizePolicy().hasHeightForWidth())
        self.n5_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.n5_btn, 3, 1, 1, 1)

        self.n0_btn = QPushButton(self.gridLayoutWidget)
        self.n0_btn.setObjectName(u"n0_btn")
        sizePolicy.setHeightForWidth(self.n0_btn.sizePolicy().hasHeightForWidth())
        self.n0_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.n0_btn, 5, 1, 1, 1)

        self.ce_btn = QPushButton(self.gridLayoutWidget)
        self.ce_btn.setObjectName(u"ce_btn")
        sizePolicy.setHeightForWidth(self.ce_btn.sizePolicy().hasHeightForWidth())
        self.ce_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.ce_btn, 0, 2, 1, 1)

        self.c_btn = QPushButton(self.gridLayoutWidget)
        self.c_btn.setObjectName(u"c_btn")
        sizePolicy.setHeightForWidth(self.c_btn.sizePolicy().hasHeightForWidth())
        self.c_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.c_btn, 0, 3, 1, 1)

        self.pow_btn = QPushButton(self.gridLayoutWidget)
        self.pow_btn.setObjectName(u"pow_btn")
        sizePolicy.setHeightForWidth(self.pow_btn.sizePolicy().hasHeightForWidth())
        self.pow_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pow_btn, 0, 1, 1, 1)

        self.n2_btn = QPushButton(self.gridLayoutWidget)
        self.n2_btn.setObjectName(u"n2_btn")
        sizePolicy.setHeightForWidth(self.n2_btn.sizePolicy().hasHeightForWidth())
        self.n2_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.n2_btn, 4, 1, 1, 1)

        self.custom_btn = QPushButton(self.gridLayoutWidget)
        self.custom_btn.setObjectName(u"custom_btn")
        sizePolicy.setHeightForWidth(self.custom_btn.sizePolicy().hasHeightForWidth())
        self.custom_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.custom_btn, 0, 0, 1, 1)

        self.n7_btn = QPushButton(self.gridLayoutWidget)
        self.n7_btn.setObjectName(u"n7_btn")
        sizePolicy.setHeightForWidth(self.n7_btn.sizePolicy().hasHeightForWidth())
        self.n7_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.n7_btn, 2, 0, 1, 1)

        self.label_res = QLabel(Form)
        self.label_res.setObjectName(u"label_res")
        self.label_res.setGeometry(QRect(0, 0, 391, 28))
        self.label_res.setLayoutDirection(Qt.LeftToRight)
        self.label_res.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_res.setStyleSheet("color: #777;")
        self.te_res = QLabel(Form)
        self.te_res.setObjectName(u"te_res")
        self.te_res.setGeometry(QRect(3, 50, 391, 91))
        self.te_res.setFont(font)
        self.te_res.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.te_res.setStyleSheet("font-size: 36px;")
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.sqrt_btn.setText(QCoreApplication.translate("Form", u"sqrt", None))
        self.cos_btn.setText(QCoreApplication.translate("Form", u"cos", None))
        self.n8_btn.setText(QCoreApplication.translate("Form", u"8", None))
        self.n9_btn.setText(QCoreApplication.translate("Form", u"9", None))
        self.n6_btn.setText(QCoreApplication.translate("Form", u"6", None))
        self.n3_btn.setText(QCoreApplication.translate("Form", u"3", None))
        self.division_btn.setText(QCoreApplication.translate("Form", u"/", None))
        self.equals_btn.setText(QCoreApplication.translate("Form", u"=", None))
        self.add_btn.setText(QCoreApplication.translate("Form", u"+", None))
        self.multiply_btn.setText(QCoreApplication.translate("Form", u"*", None))
        self.subst_btn.setText(QCoreApplication.translate("Form", u"-", None))
        self.dot_btn.setText(QCoreApplication.translate("Form", u".", None))
        self.to_num.setText(QCoreApplication.translate("Form", u"num", None))
        self.sin_btn.setText(QCoreApplication.translate("Form", u"sin", None))
        self.n4_btn.setText(QCoreApplication.translate("Form", u"4", None))
        self.n1_btn.setText(QCoreApplication.translate("Form", u"1", None))
        self.n5_btn.setText(QCoreApplication.translate("Form", u"5", None))
        self.n0_btn.setText(QCoreApplication.translate("Form", u"0", None))
        self.ce_btn.setText(QCoreApplication.translate("Form", u"CE", None))
        self.c_btn.setText(QCoreApplication.translate("Form", u"C", None))
        self.pow_btn.setText(QCoreApplication.translate("Form", u"^", None))
        self.n2_btn.setText(QCoreApplication.translate("Form", u"2", None))
        self.custom_btn.setText(QCoreApplication.translate("Form", u"Custom", None))
        self.n7_btn.setText(QCoreApplication.translate("Form", u"7", None))
        self.label_res.setText(QCoreApplication.translate("Form", u"0", None))
    # retranslateUi
