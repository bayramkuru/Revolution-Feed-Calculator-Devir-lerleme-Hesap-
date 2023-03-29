
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QLineEdit, QLabel
from rev import Ui_ekran

pi = 3.14159265

class pencere(QMainWindow):
    def __init__(self):
        super(pencere, self).__init__()
        self.ui = Ui_ekran()
        self.ui.setupUi(self)
        self.ui.btn_hesapla.clicked.connect(self.hesapla)
        self.ui.btn_kopy.clicked.connect(self.hesapla)
        self.ui.btn_feed.clicked.connect(self.hesapla)
        
    
    def hesapla(self):
        sender = self.sender().text()

        if sender == "Deviri Hesapla":
            V_f = self.ui.txt_kesme.text()
            V_f = V_f.replace(',','.')
            d = self.ui.txt_cap.text()
            d = d.replace(',','.')
            dxpi = float(d) * pi
            V_fxbin = float(V_f)*1000
            n = V_fxbin/dxpi
            n = int(n)
            self.ui.txt_devir.setText(f"{n}")
            self.ui.label_7.setText(f"Sonuç: Kesme Hızı {V_f} m/dk olan elmasla çapı {d} mm olan\n parça {n} dev/dk işlenebilir. ")
        

        if sender =="Kullan":
            N = self.ui.txt_devir.text()
            N = N.replace(',','.')
            self.ui.txt_rev.setText(f"{N}")
        if sender == "İlerleme Hesapla":
            N = self.ui.txt_rev.text()
            N = N.replace(',','.')
            z = self.ui.txt_teeth.text()
            z = z.replace(',','.')
            fz =self.ui.txt_feed_teeth.text()
            fz = fz.replace(',','.')
            F=float(z)*float(N)*float(fz)
            F = int(F)
            self.ui.txt_feed.setText(f"{F}")
    

     
        
        

           
def app():
    app = QApplication(sys.argv)
    win = pencere()
    win.show()
    sys.exit(app.exec())

app()


