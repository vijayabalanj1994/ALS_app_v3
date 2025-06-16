# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QSizePolicy,
    QSlider, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1344, 899)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #BFD7ED;\n"
"}")
        self.actionBrowse_Image = QAction(MainWindow)
        self.actionBrowse_Image.setObjectName(u"actionBrowse_Image")
        font1 = QFont()
        font1.setBold(True)
        self.actionBrowse_Image.setFont(font1)
        self.actionRun_Analysis = QAction(MainWindow)
        self.actionRun_Analysis.setObjectName(u"actionRun_Analysis")
        self.actionExport_Results = QAction(MainWindow)
        self.actionExport_Results.setObjectName(u"actionExport_Results")
        self.actionClear_All = QAction(MainWindow)
        self.actionClear_All.setObjectName(u"actionClear_All")
        self.actionExport_Results_2 = QAction(MainWindow)
        self.actionExport_Results_2.setObjectName(u"actionExport_Results_2")
        self.a_browse_image = QAction(MainWindow)
        self.a_browse_image.setObjectName(u"a_browse_image")
        self.a_browse_image.setFont(font)
        self.a_run_analysis = QAction(MainWindow)
        self.a_run_analysis.setObjectName(u"a_run_analysis")
        self.a_run_analysis.setFont(font)
        self.a_export_results = QAction(MainWindow)
        self.a_export_results.setObjectName(u"a_export_results")
        self.a_export_results.setFont(font)
        self.a_clear = QAction(MainWindow)
        self.a_clear.setObjectName(u"a_clear")
        self.a_clear.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(224, 539))
        self.groupBox_2.setMaximumSize(QSize(224, 539))
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"    background-color: #BFD7ED;\n"
"    border: none;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(200, 25))
        self.label_7.setMaximumSize(QSize(200, 25))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"QLabel {\n"
"    background-color: #60A3D9;\n"
"    color: black;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}")
        self.label_7.setFrameShape(QFrame.WinPanel)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.lb_input_image = QLabel(self.groupBox_2)
        self.lb_input_image.setObjectName(u"lb_input_image")
        self.lb_input_image.setMinimumSize(QSize(200, 200))
        self.lb_input_image.setMaximumSize(QSize(200, 200))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(True)
        self.lb_input_image.setFont(font3)
        self.lb_input_image.setStyleSheet(u"QLabel {\n"
"    background-color: #BDC3C7;\n"
"}")
        self.lb_input_image.setFrameShape(QFrame.WinPanel)
        self.lb_input_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_input_image)

        self.label_23 = QLabel(self.groupBox_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(200, 25))
        self.label_23.setMaximumSize(QSize(200, 25))
        self.label_23.setFrameShape(QFrame.NoFrame)

        self.verticalLayout.addWidget(self.label_23)

        self.label_18 = QLabel(self.groupBox_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(200, 25))
        self.label_18.setMaximumSize(QSize(200, 25))
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"QLabel {\n"
"    background-color: #60A3D9;\n"
"    color: black;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}")
        self.label_18.setFrameShape(QFrame.WinPanel)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_18)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(200, 25))
        self.label_13.setMaximumSize(QSize(200, 25))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setItalic(True)
        self.label_13.setFont(font4)
        self.label_13.setFrameShape(QFrame.NoFrame)

        self.verticalLayout.addWidget(self.label_13)

        self.lb_case_id = QLineEdit(self.groupBox_2)
        self.lb_case_id.setObjectName(u"lb_case_id")
        self.lb_case_id.setMinimumSize(QSize(200, 25))
        self.lb_case_id.setMaximumSize(QSize(200, 25))

        self.verticalLayout.addWidget(self.lb_case_id)

        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(200, 25))
        self.label_14.setMaximumSize(QSize(200, 25))
        self.label_14.setFont(font4)
        self.label_14.setFrameShape(QFrame.NoFrame)

        self.verticalLayout.addWidget(self.label_14)

        self.lb_image_no = QLineEdit(self.groupBox_2)
        self.lb_image_no.setObjectName(u"lb_image_no")
        self.lb_image_no.setMinimumSize(QSize(200, 25))
        self.lb_image_no.setMaximumSize(QSize(200, 25))

        self.verticalLayout.addWidget(self.lb_image_no)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(200, 25))
        self.label_15.setMaximumSize(QSize(200, 25))
        self.label_15.setFont(font4)
        self.label_15.setFrameShape(QFrame.NoFrame)

        self.verticalLayout.addWidget(self.label_15)

        self.lb_region = QLineEdit(self.groupBox_2)
        self.lb_region.setObjectName(u"lb_region")
        self.lb_region.setMinimumSize(QSize(200, 25))
        self.lb_region.setMaximumSize(QSize(200, 25))

        self.verticalLayout.addWidget(self.lb_region)


        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(631, 539))
        self.groupBox.setSizeIncrement(QSize(631, 539))
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"    background-color: #BFD7ED;\n"
"    border: none;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 25))
        self.label.setMaximumSize(QSize(200, 25))
        self.label.setFont(font2)
        self.label.setStyleSheet(u"QLabel {\n"
"    background-color: #003B73;\n"
"    color: white;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}")
        self.label.setFrameShape(QFrame.WinPanel)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.lb_cam_image = QLabel(self.groupBox)
        self.lb_cam_image.setObjectName(u"lb_cam_image")
        self.lb_cam_image.setMinimumSize(QSize(200, 200))
        self.lb_cam_image.setMaximumSize(QSize(200, 200))
        self.lb_cam_image.setFont(font3)
        self.lb_cam_image.setStyleSheet(u"QLabel {\n"
"    background-color: #BDC3C7;\n"
"}")
        self.lb_cam_image.setFrameShape(QFrame.WinPanel)
        self.lb_cam_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lb_cam_image)

        self.label_24 = QLabel(self.groupBox)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(200, 25))
        self.label_24.setMaximumSize(QSize(200, 25))
        self.label_24.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_3.addWidget(self.label_24)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(200, 25))
        self.label_2.setMaximumSize(QSize(200, 25))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"QLabel {\n"
"    background-color: #003B73;\n"
"    color: white;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}")
        self.label_2.setFrameShape(QFrame.WinPanel)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.lb_cam_circle_image = QLabel(self.groupBox)
        self.lb_cam_circle_image.setObjectName(u"lb_cam_circle_image")
        self.lb_cam_circle_image.setMinimumSize(QSize(200, 200))
        self.lb_cam_circle_image.setMaximumSize(QSize(200, 200))
        self.lb_cam_circle_image.setFont(font3)
        self.lb_cam_circle_image.setStyleSheet(u"QLabel {\n"
"    background-color: #BDC3C7;\n"
"}")
        self.lb_cam_circle_image.setFrameShape(QFrame.WinPanel)
        self.lb_cam_circle_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lb_cam_circle_image)


        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(631, 539))
        self.groupBox_4.setSizeIncrement(QSize(631, 539))
        self.groupBox_4.setStyleSheet(u"QGroupBox {\n"
"    background-color: #BFD7ED;\n"
"    border: none;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_30 = QLabel(self.groupBox_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(400, 25))
        self.label_30.setMaximumSize(QSize(400, 25))
        self.label_30.setFont(font2)
        self.label_30.setStyleSheet(u"QLabel {\n"
"    background-color: #003B73;\n"
"    color: white;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}")
        self.label_30.setFrameShape(QFrame.WinPanel)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_30)

        self.lb_focused_image = QLabel(self.groupBox_4)
        self.lb_focused_image.setObjectName(u"lb_focused_image")
        self.lb_focused_image.setMinimumSize(QSize(400, 400))
        self.lb_focused_image.setMaximumSize(QSize(400, 400))
        self.lb_focused_image.setFont(font3)
        self.lb_focused_image.setStyleSheet(u"QLabel {\n"
"    background-color: #BDC3C7;\n"
"}")
        self.lb_focused_image.setFrameShape(QFrame.WinPanel)
        self.lb_focused_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lb_focused_image)

        self.label_27 = QLabel(self.groupBox_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(200, 7))
        self.label_27.setMaximumSize(QSize(200, 7))
        self.label_27.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_2.addWidget(self.label_27)

        self.lb_slider_value = QLabel(self.groupBox_4)
        self.lb_slider_value.setObjectName(u"lb_slider_value")
        self.lb_slider_value.setMinimumSize(QSize(400, 25))
        self.lb_slider_value.setMaximumSize(QSize(400, 25))
        self.lb_slider_value.setFont(font2)
        self.lb_slider_value.setStyleSheet(u"QLabel {\n"
"    color: #003B73;\n"
"}")
        self.lb_slider_value.setFrameShape(QFrame.NoFrame)
        self.lb_slider_value.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lb_slider_value)

        self.s_filter_slider = QSlider(self.groupBox_4)
        self.s_filter_slider.setObjectName(u"s_filter_slider")
        self.s_filter_slider.setMinimumSize(QSize(400, 0))
        self.s_filter_slider.setMaximumSize(QSize(400, 16777215))
        self.s_filter_slider.setValue(80)
        self.s_filter_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.s_filter_slider)


        self.gridLayout.addWidget(self.groupBox_4, 0, 2, 1, 1)

        self.lb_status = QLabel(self.centralwidget)
        self.lb_status.setObjectName(u"lb_status")
        self.lb_status.setMinimumSize(QSize(200, 30))
        self.lb_status.setMaximumSize(QSize(16777215, 30))
        self.lb_status.setFont(font)
        self.lb_status.setStyleSheet(u"QLabel {\n"
"    background-color: #F44336;  /* Medium red (Material Design red 500) */\n"
"    color: white;               /* White text for contrast */\n"
"    padding: 4px;\n"
"    border-radius: 3px;\n"
"}")
        self.lb_status.setFrameShape(QFrame.WinPanel)

        self.gridLayout.addWidget(self.lb_status, 2, 0, 1, 4)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 0))
        self.groupBox_3.setStyleSheet(u"QGroupBox {\n"
"    background-color: #BFD7ED;\n"
"    border: none;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(250, 25))
        self.label_5.setMaximumSize(QSize(200, 25))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"QLabel {\n"
"    color: #0C2D48;\n"
"}")
        self.label_5.setFrameShape(QFrame.NoFrame)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.p_bar_control = QProgressBar(self.groupBox_3)
        self.p_bar_control.setObjectName(u"p_bar_control")
        self.p_bar_control.setMinimumSize(QSize(200, 25))
        self.p_bar_control.setMaximumSize(QSize(16777215, 25))
        self.p_bar_control.setFont(font2)
        self.p_bar_control.setValue(0)

        self.gridLayout_2.addWidget(self.p_bar_control, 2, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(250, 25))
        self.label_8.setMaximumSize(QSize(250, 25))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"QLabel {\n"
"    color: #0C2D48;\n"
"}")
        self.label_8.setFrameShape(QFrame.NoFrame)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)

        self.p_bar_concordant = QProgressBar(self.groupBox_3)
        self.p_bar_concordant.setObjectName(u"p_bar_concordant")
        self.p_bar_concordant.setMinimumSize(QSize(200, 25))
        self.p_bar_concordant.setMaximumSize(QSize(16777215, 25))
        self.p_bar_concordant.setFont(font2)
        self.p_bar_concordant.setValue(0)

        self.gridLayout_2.addWidget(self.p_bar_concordant, 3, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(250, 25))
        self.label_19.setMaximumSize(QSize(250, 25))
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"QLabel {\n"
"    color: #0C2D48;\n"
"}")
        self.label_19.setFrameShape(QFrame.NoFrame)
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_19, 4, 0, 1, 1)

        self.p_bar_discordant = QProgressBar(self.groupBox_3)
        self.p_bar_discordant.setObjectName(u"p_bar_discordant")
        self.p_bar_discordant.setMinimumSize(QSize(200, 25))
        self.p_bar_discordant.setMaximumSize(QSize(16777215, 25))
        self.p_bar_discordant.setFont(font2)
        self.p_bar_discordant.setValue(0)

        self.gridLayout_2.addWidget(self.p_bar_discordant, 4, 1, 1, 1)

        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(200, 25))
        self.label_25.setMaximumSize(QSize(16777215, 25))
        self.label_25.setFont(font2)
        self.label_25.setStyleSheet(u"QLabel {\n"
"    background-color: #0C2D48;\n"
"    color: white;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}")
        self.label_25.setFrameShape(QFrame.WinPanel)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_25, 0, 0, 1, 2)

        self.lb_prediction = QLabel(self.groupBox_3)
        self.lb_prediction.setObjectName(u"lb_prediction")
        self.lb_prediction.setMinimumSize(QSize(200, 50))
        self.lb_prediction.setMaximumSize(QSize(16777215, 50))
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        self.lb_prediction.setFont(font5)
        self.lb_prediction.setFrameShape(QFrame.StyledPanel)
        self.lb_prediction.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_prediction, 6, 1, 1, 1)

        self.label_26 = QLabel(self.groupBox_3)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(200, 25))
        self.label_26.setMaximumSize(QSize(16777215, 25))
        self.label_26.setFont(font2)
        self.label_26.setStyleSheet(u"QLabel {\n"
"    color: #60A3D9;\n"
"}")
        self.label_26.setFrameShape(QFrame.NoFrame)
        self.label_26.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_26, 5, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(200, 25))
        self.label_17.setMaximumSize(QSize(16777215, 25))
        self.label_17.setFont(font2)
        self.label_17.setStyleSheet(u"QLabel {\n"
"    color: #60A3D9;\n"
"}")
        self.label_17.setFrameShape(QFrame.NoFrame)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_17, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 3)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(431, 0))
        self.groupBox_5.setStyleSheet(u"QGroupBox {\n"
"    background-color: #BFD7ED;\n"
"    border: none;\n"
"}")
        self.formLayout_2 = QFormLayout(self.groupBox_5)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_21 = QLabel(self.groupBox_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(200, 25))
        self.label_21.setMaximumSize(QSize(16777215, 25))
        self.label_21.setFont(font2)
        self.label_21.setStyleSheet(u"QLabel {\n"
"    background-color: #60A3D9;\n"
"    color: black;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"}")
        self.label_21.setFrameShape(QFrame.WinPanel)

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.label_21)

        self.textEdit = QTextEdit(self.groupBox_5)
        self.textEdit.setObjectName(u"textEdit")

        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.textEdit)


        self.gridLayout.addWidget(self.groupBox_5, 0, 3, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1344, 30))
        self.menubar.setStyleSheet(u"QMenuBar {\n"
"    background-color: #2980B9;\n"
"    color: white;\n"
"    font-size: 12pt;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    padding: 4px 10px;\n"
"    font-size: 12pt;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background-color: #2C3E50; /* Slightly darker on hover */\n"
"    color: white;\n"
"    font-size: 12pt;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.menuControls = QMenu(self.menubar)
        self.menuControls.setObjectName(u"menuControls")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuControls.menuAction())
        self.menuControls.addAction(self.a_browse_image)
        self.menuControls.addAction(self.a_run_analysis)
        self.menuControls.addAction(self.a_export_results)
        self.menuControls.addAction(self.a_clear)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionBrowse_Image.setText(QCoreApplication.translate("MainWindow", u"Browse Image", None))
        self.actionRun_Analysis.setText(QCoreApplication.translate("MainWindow", u"Clear Image", None))
        self.actionExport_Results.setText(QCoreApplication.translate("MainWindow", u"Export Results", None))
        self.actionClear_All.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.actionExport_Results_2.setText(QCoreApplication.translate("MainWindow", u"Export Results", None))
        self.a_browse_image.setText(QCoreApplication.translate("MainWindow", u"Browse Image", None))
        self.a_run_analysis.setText(QCoreApplication.translate("MainWindow", u"Run Analysis", None))
        self.a_export_results.setText(QCoreApplication.translate("MainWindow", u"Export Results", None))
        self.a_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.groupBox_2.setTitle("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Input Image", None))
        self.lb_input_image.setText(QCoreApplication.translate("MainWindow", u"Waiting for Image", None))
        self.label_23.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Meta Data", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Case ID:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Image ID:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Region:", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Model Focus Heat-Map", None))
        self.lb_cam_image.setText(QCoreApplication.translate("MainWindow", u"Waiting for Image", None))
        self.label_24.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Areas Of Focus", None))
        self.lb_cam_circle_image.setText(QCoreApplication.translate("MainWindow", u"Waiting for Image", None))
        self.groupBox_4.setTitle("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Model Focu Inspector ", None))
        self.lb_focused_image.setText(QCoreApplication.translate("MainWindow", u"Waiting for Image", None))
        self.label_27.setText("")
        self.lb_slider_value.setText(QCoreApplication.translate("MainWindow", u"Focus Toggle - 80%", None))
        self.lb_status.setText(QCoreApplication.translate("MainWindow", u"Status: Waiting for Image", None))
        self.groupBox_3.setTitle("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Healthy :-", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ALS with Cognitive Imparment :-", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"ALS without  Cognitive Imparment :-", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Model Analysis", None))
        self.lb_prediction.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Modell Prediction", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Model Predioction Confidence ", None))
        self.groupBox_5.setTitle("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Notes:", None))
        self.menuControls.setTitle(QCoreApplication.translate("MainWindow", u"Controls", None))
    # retranslateUi

