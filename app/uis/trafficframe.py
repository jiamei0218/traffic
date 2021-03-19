from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.Qt import Qt
from app.uis.trafficui import Ui_Dialog
import cv2 as cv
from app.uis.Video import Video

class TrafficFrame(QDialog):
    def __init__(self):
        super(TrafficFrame,self).__init__() 
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #线程
        self.th = Video()
        #信号指定接受者
        #接受者指定槽函数（数据处理函数）
        self.th.sing_show.connect(self.show_video)

        #启动线程
        self.th.start()
    #定义槽函数
    def show_video(self,h,w,c,data):
        image = QImage(data,w,h,w*c,QImage.Format_BGR888)
        pix = QPixmap.fromImage(image)
        #width = self.ui.label_9.width()
        #height = self.ui.label_9.height()
        #scale_pix = pix.scaled(width,height,Qt.KeepAspectRatio)
        #self.ui.label_9.setPixmap(scale_pix)不缩放
        self.ui.label_9.setPixmap(pix)
        self.ui.label_9.setScaledContents(True)

