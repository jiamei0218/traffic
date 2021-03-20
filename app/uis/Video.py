#创建一个线程：执行视频流获取操作
#QThread
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
import cv2 as cv
#当场线程要有执行的方法已经定义过了是run
#继承线程类
#重写run方法：当前线程的功能实现（读取视频流:获取摄像头，循环拿到每一帧数据）
#创建实例.start（） 执行线程

#线程的数据交互
#线程数据-----传递给主窗口
#定义信号（传递的数据类型）
#发送信号（真实数据）
#信号指定接受者
#接受者指定槽函数（数据处理函数）
#定义槽函数



class Video(QThread):
    #定义信号（传递的数据类型）
    sing_show = pyqtSignal(int,int,int,bytes,int)
    def __init__(self,th_id,dev_id):
        super(Video,self).__init__()
        self.dev_id=dev_id
        self.th_id=th_id
        #获取摄像头 第0个摄像头
        #self.dev = cv.VideoCapture(0,cv.CAP_DSHOW)

        #获取本地资源
        self.dev = cv.VideoCapture(self.dev_id,cv.CAP_DSHOW)
        self.dev.open(self.dev_id)

    #重写run方法
    def run(self):
        # 循环逐帧捕获数据
        while True:
            # 一帧数据
            status, frame = self.dev.read()
            # frame opencv numpy 数组
            #数据处理
            h,w,c = frame.shape
            deta = frame.tobytes()
            #发送信号（真实数据）触发发送信号
            self.sing_show.emit(h,w,c,deta,self.th_id)
            #等若干时间 0.1秒
            # usleep(微妙)  1s=1000000微妙
            QThread.usleep(50000)




