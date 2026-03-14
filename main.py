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

        self.target_rect = None  # Contiendra (x, y, w, h) de l'élément à entourer
        self.solution_text = ""  # Contiendra le résultat de l'équation

        self.target_rect = (200, 200, 300, 60)
        self.solution_text = "x = 5"
    
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

    def paintEvent(self, event):
        # S'il n'y a rien à entourer, on n'entoure rien
        if self.target_rect is None: 
            return
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing) # Traits lisses

        # Config du pinceau rouge
        pen = QPen(QColor(255, 0, 0), 3)
        painter.setPen(pen)

        x, y, w, h = self.target_rect   # On récup les coordonnées du rectangle à dessiner
        painter.drawRect(x,y,w,h)       # On le dessine
        painter.drawText(x + w + 10, y + (h // 2), f"Solution: {self.solution_text}") # On dessine la solution de l'equation à l'interieur




if __name__ == '__main__':
    app = QApplication(sys.argv)
    overlay = MathOverlay()
    sys.exit(app.exec())