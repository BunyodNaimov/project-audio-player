import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class AudioPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Audio Player")
        self.setGeometry(200, 200, 300, 100)

        self.media_player = QMediaPlayer(self)

        self.btn_open = QPushButton("Open", self)
        self.btn_open.setGeometry(10, 10, 80, 30)
        self.btn_open.clicked.connect(self.open_file)

        self.btn_play = QPushButton("Play", self)
        self.btn_play.setGeometry(100, 10, 80, 30)
        self.btn_play.clicked.connect(self.play_audio)

        self.btn_stop = QPushButton("Stop", self)
        self.btn_stop.setGeometry(190, 10, 80, 30)
        self.btn_stop.clicked.connect(self.stop_audio)

    def open_file(self):
        file_dialog = QFileDialog()
        file_path = file_dialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav)")[0]
        if file_path:
            self.media_player.setMedia(QMediaContent(file_path))

    def play_audio(self):
        self.media_player.play()

    def stop_audio(self):
        self.media_player.stop()


if __name__ == '__main__':
    os.environ["QT_QPA_PLATFORM"] = "wayland"
    app = QApplication(sys.argv)
    player = AudioPlayer()
    player.show()
    sys.exit(app.exec_())
