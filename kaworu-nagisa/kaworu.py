import sys
import random
import requests
from io import BytesIO
from PyQt5.QtCore import Qt, QTimer, QPoint, QBuffer, QByteArray, QSize
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

GIF_URL = "https://i.imgur.com/zCuSHUq.gif"
MAX_LAINS = 100
SCALE_PERCENT = 10  # Resize GIF to 10% of original size

windows = []
running = True

class FloatingGif(QWidget):
    def __init__(self, gif_data):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.label = QLabel(self)
        self.buffer = QBuffer()
        self.buffer.setData(QByteArray(gif_data))
        self.buffer.open(QBuffer.ReadOnly)

        self.movie = QMovie()
        self.movie.setDevice(self.buffer)

        # Load and scale GIF
        self.movie.jumpToNextFrame()
        original_size = self.movie.currentImage().size()
        scaled_size = QSize(
            max(1, original_size.width() * SCALE_PERCENT // 100),
            max(1, original_size.height() * SCALE_PERCENT // 100)
        )
        self.movie.setScaledSize(scaled_size)

        self.label.setMovie(self.movie)
        self.movie.start()

        self.resize(scaled_size.width(), scaled_size.height())

        screen_geometry = QApplication.primaryScreen().geometry()
        max_x = max(0, screen_geometry.width() - scaled_size.width())
        max_y = max(0, screen_geometry.height() - scaled_size.height())
        x = random.randint(0, max_x)
        y = random.randint(0, max_y)
        self.move(x, y)

        self.label.mousePressEvent = self.spawn_another

        self.timer = QTimer()
        self.timer.timeout.connect(self.move_randomly)
        self.timer.start(100)

    def move_randomly(self):
        dx = random.randint(-10, 10)
        dy = random.randint(-10, 10)
        new_pos = self.pos() + QPoint(dx, dy)

        screen_geometry = QApplication.primaryScreen().geometry()
        new_x = max(0, min(screen_geometry.width() - self.width(), new_pos.x()))
        new_y = max(0, min(screen_geometry.height() - self.height(), new_pos.y()))
        self.move(new_x, new_y)

    def spawn_another(self, event):
        spawn_window()

def spawn_window():
    global gif_data
    if len(windows) >= MAX_LAINS:
        return
    win = FloatingGif(gif_data)
    win.show()
    windows.append(win)

def close_all():
    for w in windows:
        w.close()
    sys.exit(0)

def fetch_gif_data(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.content

if __name__ == '__main__':
    app = QApplication(sys.argv)

    gif_data = fetch_gif_data(GIF_URL)

    # Escape key closes everything
    class EscapeFilter(QWidget):
        def eventFilter(self, obj, event):
            if event.type() == event.KeyPress and event.key() == Qt.Key_Escape:
                close_all()
            return False

    escape_filter = EscapeFilter()
    app.installEventFilter(escape_filter)

    spawn_window()

    # Auto-spawn 2 every second (if below 100)
    auto_timer = QTimer()
    auto_timer.timeout.connect(lambda: [spawn_window(), spawn_window()])
    auto_timer.start(1000)

    sys.exit(app.exec_())
