import sys
from PySide.QtCore import *
from functools import partial
import scipy.misc
from Steganography import *
from PySide.QtGui import *
from SteganographyGUI import *


class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Consumer, self).__init__(parent)
        self.payload1_filename = ''
        self.carrier1_filename = ''
        self.payloadFound = 0
        self.carrierFound = 0
        self.setupUi(self)
        self.chkApplyCompression.stateChanged.connect(lambda :self.compEdit())
        self.slideCompression.valueChanged.connect(lambda:self.slideBar())
        self.chkOverride.stateChanged.connect(lambda:self.override())
        self.btnSave.clicked.connect(lambda:self.save())
        self.btnClean.clicked.connect(lambda:self.clean())
        self.btnExtract.clicked.connect(lambda:self.extract())

        views = [self.viewCarrier1, self.viewPayload1, self.viewCarrier2] # no payload2

        for view in views:
            view.dragEnterEvent = lambda e: e.accept()
            view.dragMoveEvent = lambda e: e.accept()
            view.dragLeaveEvent = lambda e: e.accept()
            view.dropEvent = partial(self.DropEvent, view)

    def DropEvent(self, view, event):
            mime = event.mimeData()
            if not mime.hasUrls():
                return

            filePath = mime.text()[7:-2]
            file_type = filePath[-4:]
            if not file_type == ".png":
                return

            self.filePath = filePath
            imageArray = self.pullImage(filePath)
            try:
                if view == self.viewPayload1:
                    self.payload1 = Payload(imageArray, 0, None)
                elif view == self.viewCarrier1:
                    self.carrier1 = Carrier(imageArray)
                else:
                    self.carrier2 = Carrier(imageArray)
            except:
                return

            self.showImage(view,filePath)

            if view == self.viewPayload1:
                self.payload1_filename = filePath
                self.txtPayloadSize.setText(str(len(self.payload1.json)))
                self.chkApplyCompression.setChecked(False)
                self.slideCompression.setValue(0)
                self.slideCompression.setDisabled(True)
                self.txtCompression.setText('0')
                self.txtCompression.setDisabled(True)
                self.payloadFound = 1

            elif view == self.viewCarrier1:
                self.carrier1_filename = filePath
                self.txtCarrierSize.setText(str(self.carrier1.dimensions[0] * self.carrier1.dimensions[1]))
                if self.carrier1.payloadExists():
                    self.chkOverride.setEnabled(True)
                    self.lblPayloadFound.setText(">>>> Payload Found <<<<")
                else:
                    self.chkOverride.setEnabled(False)
                    self.lblPayloadFound.clear()

                self.carrierFound = 1

            else:

                self.carr2_filename = filePath
                self.viewPayload2.setScene(None)
                # self.showImage(self.viewPayload2, "")
                if not self.carrier2.payloadExists():
                    self.lblCarrierEmpty.setText(">>>> Carrier Empty <<<<")
                    self.btnExtract.setDisabled(True)
                    self.btnClean.setDisabled(True)
                else:
                    self.lblCarrierEmpty.clear()
                    self.btnExtract.setDisabled(False)
                    self.btnClean.setDisabled(False)

            if self.carrierFound == 1 and self.payloadFound == 1:
                carrier_size = int(self.txtCarrierSize.text())
                payload_size = int(self.txtPayloadSize.text())
                if (not self.carrier1.payloadExists() or self.chkOverride.isChecked()) and (carrier_size >= payload_size):
                    self.btnSave.setEnabled(True)
                else:
                    self.btnSave.setEnabled(False)
    
    def compEdit(self):
        if self.chkApplyCompression.isChecked():
            self.slideCompression.setEnabled(True)
            self.txtCompression.setEnabled(True)
            imageArray = self.pullImage(self.payload1_filename)
            self.payload1 = Payload(imageArray, self.slideCompression.value(), None)
            self.txtPayloadSize.setText(str(len(self.payload1.json)))
        else:
            self.slideCompression.setEnabled(False)
            self.txtCompression.setEnabled(False)
            imageArray = self.pullImage(self.payload1_filename)
            self.payload1 = Payload(imageArray, -1, None)
            self.txtPayloadSize.setText(str(len(self.payload1.json)))

    def slideBar(self):
        self.txtCompression.setText(str(self.slideCompression.value()))
        imageArray = self.pullImage(self.payload1_filename)
        self.payload1 = Payload(imageArray, self.slideCompression.value(), None)
        self.txtPayloadSize.setText(str(len(self.payload1.json)))
        self.compression = self.slideCompression.value()
        
    def extract(self):
        payload2 = self.carrier2.extractPayload()
        scipy.misc.imsave("temp_extractedImg.png",payload2.rawData)
        self.showImage(self.viewPayload2,'temp_extractedImg.png')
        
    def clean(self):
        cleaned_image = self.carrier2.clean()
        scipy.misc.imsave(self.carr2_filename,cleaned_image)
        self.showImage(self.viewCarrier2,self.carr2_filename)
        # self.showImage(self.viewPayload2, None)
        self.lblCarrierEmpty.setText(">>>> Carrier Empty <<<<")
        self.btnClean.setDisabled(True)
        self.btnExtract.setDisabled(True)

        self.viewPayload2.setScene(None)
        
    def override(self):
        if self.chkOverride.isChecked():
            self.btnSave.setEnabled(True)
        else:
            self.btnSave.setDisabled(True)

    def save(self):
        filename, temp = QFileDialog.getSaveFileName(self, caption='Embed Payload into Carrier', filter="PNG files (*.png)")
        image = self.carrier1.embedPayload(self.payload1,self.chkOverride.isChecked())
        scipy.misc.imsave(filename,image)

    ############# Functions to assist with steg tasks
    
    def pullImage(self, file):
        im = np.asarray(Image.open(file))
        return im # numpy array        

    def showImage(self,view,filePath):
        frame = QGraphicsScene()
        img = QPixmap(filePath)
        img = img.scaled(355,280, Qt.KeepAspectRatio)
        frame.addPixmap(img)
        view.setScene(frame)
        view.show()


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()