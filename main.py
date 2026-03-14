import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPainter, QPen, QColor

# System tray
from PyQt6.QtWidgets import QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon, QAction

class MathOverlay(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setup_tray_icon()
    
    def initUI(self):
        # Rendre l'overlay transparent
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Flags de la fenêtre
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |     # pas de bordure
            Qt.WindowType.WindowStaysOnTopHint |    # toujours au premier plan
            Qt.WindowType.WindowTransparentForInput # les clics passent à travers
        )

        self.showFullScreen()

    def setup_tray_icon(self):
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(self.style().StandardPixmap.SP_ComputerIcon))

        # Menu clic-droit sur l'icone
        tray_menu = QMenu()
        quit_action = QAction("Quitter", self)
        quit_action.triggered.connect(QApplication.instance().quit)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    overlay = MathOverlay()
    sys.exit(app.exec())