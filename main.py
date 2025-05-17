#создай тут фоторедактор Easy Editor!
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QFileDialog ,QMessageBox, QWidget, QPushButton,QLabel,QListWidget, QVBoxLayout, QHBoxLayout
from PIL import Image , ImageOps, ImageFilter
from PyQt5.QtGui import QPixmap
class ImageProcessore():
    def __init__(self):
        self.filename = None
        self.image = None
        self.dir = None
        self.save_dir = 'Modified/'

    def loadImage(self,filename):
        self.filename = filename
        self.dir = workdir
        image_path = os.path.join(self.dir,self.filename)
        self.image =Image.open(image_path)
    
    def showImage(self,path):
        pixmapimage = QPixmap(path)
        label_width = winner.width()
        label_height = winner.height()
        scaled_pixmap = pixmapimage.scaled(label_width,label_height, Qt.KeepAspectRatio)
        winner.setPixmap(scaled_pixmap)
        winner.setVisible(True)
    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path,self.filename)
        self.image.save(image_path)
    def do_bw(self):
        if apr.selectedItems():

            self.image = ImageOps.grayscale(self.image)
            self.saveImage()
            image_path = os.path.join(self.dir , self.save_dir ,self.filename )
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('Выберите картину')
            error_win.exec()

    def do_left(self):
        if apr.selectedItems():
            self.image = self.image.rotate(90)
            self.saveImage()
            image_path = os.path.join(self.dir , self.save_dir ,self.filename )
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('Выберите картину')
            error_win.exec()
    def do_right(self):
        if apr.selectedItems():
            self.image = self.image.rotate(-90)
            self.saveImage()
            image_path = os.path.join(self.dir , self.save_dir ,self.filename )
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('Выберите картину')
            error_win.exec()
    def do_mirror(self):
        if apr.selectedItems():
            self.image = ImageOps.mirror(self.image)
            self.saveImage()
            image_path = os.path.join(self.dir , self.save_dir ,self.filename )
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('Выберите картину')
            error_win.exec()

    
    def do_sharpen(self):
        if apr.selectedItems():
            try:
                   self.image = self.image.filter(ImageFilter.SHARPEN)
            except:
                error_win = QMessageBox()
                error_win.setText('С такими не работаем')
                error_win.exec()
            self.saveImage()
            image_path = os.path.join(self.dir , self.save_dir ,self.filename )
            self.showImage(image_path)
        else:
            error_win = QMessageBox()
            error_win.setText('Выберите картину')
            error_win.exec()





workimage = ImageProcessore()
def showChosenImage():
    if apr.currentRow() >= 0:
        filename = apr.currentItem().text()
        workimage.loadImage(filename)
        image_path = os.path.join(workimage.dir, filename)
        workimage.showImage(image_path)

workdir = 'путь до Рабочей папки'
def chooseWorkDir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files,extensions):
    result = []
    for filename in files:
        for extension in extensions:
            if filename.endswith(extension):
                result.append(filename)
    return result

def showFilenameList():
    chooseWorkDir()
    extensions = ['.jpg','.jpeg','.png','.gif', '.jfif']
    files = os.listdir(workdir)
    files = filter(files, extensions)
    apr.clear()
    apr.addItems(files)
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Easy Editor')
main_win.resize(700,500)
apr = QListWidget()
winner = QLabel('Картинка')
button = QPushButton('Папка')
button1 = QPushButton('Лево')
button2 = QPushButton('Право')
button3 = QPushButton('Зеркало')
button4 = QPushButton('резкость')
button5 = QPushButton('Ч/Б')
h_line = QHBoxLayout()
h_line1 = QHBoxLayout()
v_line = QVBoxLayout()
v_line1 = QVBoxLayout()
v_line1.addWidget(
    button
    )
# h_line.addWidget(button)
v_line1.addWidget(apr)

h_line.addWidget(button1)
h_line.addWidget(button2)
h_line.addWidget(button3)
h_line.addWidget(button4)
h_line.addWidget(button5)
h_line1.addLayout(v_line1)
h_line1.addLayout(v_line)
v_line.addWidget(winner)
v_line.addLayout(h_line)
main_win.setLayout(h_line1)

button4.clicked.connect(workimage.do_sharpen)
button3.clicked.connect(workimage.do_mirror)
button2.clicked.connect(workimage.do_right)
button1.clicked.connect(workimage.do_left)
button5.clicked.connect(workimage.do_bw)
button.clicked.connect(showFilenameList)
apr.currentRowChanged.connect(showChosenImage)
main_win.show()
app.exec_()
