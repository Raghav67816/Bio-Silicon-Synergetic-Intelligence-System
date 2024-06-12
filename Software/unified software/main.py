# Import dependencies
from sys import exit, argv
from app_ui import Ui_MainWindow
from PySide6.QtCore import QSettings
from settings_app import open_settings
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel

class UnifiedApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.stylesheets = {"dark":"""
      * QPushButton {
    color: #1f1f1f;
    background-color: #296dff;
    
}
 QMainWindow {
    background-color: #1f1f1f;
    
}
QApplication {
    background-color: #1f1f1f;
    
    
}
QFrame {
    color: #ebebeb;
    background-color: #1f1f1f;
}
QTabWidget {
    color: #ebebeb;
    background-color: #1f1f1f;
}
QTabBar {
    color: #ebebeb;
    background-color: #1f1f1f;
    
}
QGroupBox {
    color: #ebebeb;
    background-color: #1f1f1f;
    
}
QDialog {
   background-color: #1f1f1f;
    
}
QFileDialog {
    background-color: #1f1f1f;
    
}
QLineEdit{
    background-color: #ebebeb;
    
}
QComboBox{
    background-color: #ebebeb;
    
}
    QComboBox QAbstractItemView {
        background-color: #ebebeb; 
        color: #1f1f1f; 
        selection-background-color: #296dff; 
        selection-color:#ebebeb;  
    }

QPushButton:hover {
    color:#1f1f1f;
    background-color: #80a8ff;
}

QToolButton {
    background-color: #80a8ff;
}
QProgressBar {
     background-color: #ebebeb;
 }

 QProgressBar::chunk {
     background-color: #05B8CC;
 }
    """}
        self.setColorPalette(self.stylesheets["dark"])
        self.settings_obj = QSettings("./config/default.ini", QSettings.Format.IniFormat)
        
        self.featureDisplayed = False
        self.ui.settingsBtn.clicked.connect(self.handle_settings_app)

    # handle settings dialog events
    def handle_settings_app(self):
        dialog_exec = open_settings()
        if dialog_exec == 1:
            self.add_features_to_display()
        else:
            pass

    """
    add_features_to_display

    Adds features to "Extracted Featuers" group box.
    """
    def add_features_to_display(self):
        self.clear_features()
        if not self.featureDisplayed:
            features = []
            for i in range(0, 6):
                val = self.settings_obj.value(f"features/{i}")
                if val != "":
                    features.append(val)

                    obj_name_label = val.lower().replace(" ", "_")

                    label_widget = QLabel(self)
                    value_widget = QLabel(self)

                    label_widget.setText(val)
                    label_widget.setObjectName(f"{obj_name_label}_label")

                    value_widget.setText("--")
                    value_widget.setObjectName(f"{obj_name_label}_val")

                    self.ui.extFeaturesLayout.addRow(label_widget, value_widget)

                self.ui.extFeaturesLayout.setHorizontalSpacing(20)
                self.ui.extFeaturesLayout.setVerticalSpacing(10)
                self.featureDisplayed = True
        else:
            pass

    """
    clear_features

    Remove all features
    """
    def setColorPalette(self,stylesheet):
        app.setStyleSheet(stylesheet)
		
    def clear_features(self):
        labels = self.ui.extFeaturesGBox.findChildren(QLabel)
        if len(labels) == 0:
            pass

        else:
            for label in labels:
                label.deleteLater()
            self.featureDisplayed = False



#main_window = uic.loadUi('ui files/app.ui')
app = QApplication(argv)
# Find all buttons in the main window
window = UnifiedApp()
window.show()
exit(app.exec())
