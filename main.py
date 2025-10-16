import sys
import threading
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PySide6.QtCore import Qt, Signal, QObject
from PySide6.QtGui import QColor
from qt import Ui_MainWindow
from reply import callapi

class WorkerSignals(QObject):
    """Worker thread için sinyaller"""
    finished = Signal(str)  # AI cevabı
    error = Signal(str)  # Hata mesajı

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # ListWidget stil ayarları
        self.ui.listWidget.setWordWrap(True)
        self.ui.listWidget.setSpacing(5)
        
        # sendButton'a bağlan
        self.ui.sendButton.clicked.connect(self.on_send_button_clicked)
        
        # Enter tuşuna basıldığında butonu tetikle
        self.ui.lineEdit.returnPressed.connect(self.on_send_button_clicked)
    
    def add_message(self, text, is_user=True):
        """Mesajı stillendirilmiş balon olarak ekle"""
        item = QListWidgetItem(text)
        
        if is_user:
            # Kullanıcı mesajı - Sağda beyaz balon
            item.setTextAlignment(Qt.AlignRight)
            item.setBackground(QColor(255, 255, 255))  # Beyaz
            item.setForeground(QColor(0, 0, 0))  # Siyah yazı
        else:
            # AI mesajı - Solda koyu yeşil balon
            item.setTextAlignment(Qt.AlignLeft)
            item.setBackground(QColor(34, 139, 34))  # Koyu yeşil
            item.setForeground(QColor(255, 255, 255))  # Beyaz yazı
        
        self.ui.listWidget.addItem(item)
        self.ui.listWidget.scrollToBottom()
    
    def get_ai_response(self, text, signals):
        """Arka planda API çağrısı yap"""
        try:
            response = callapi(text)
            signals.finished.emit(response.text)
            print(f"AI Cevabı: {response.text}")
        except Exception as e:
            signals.error.emit(str(e))
            print(f"Hata: {e}")
    
    def on_send_button_clicked(self):
        """Butona tıklandığında çalışacak fonksiyon"""
        text = self.ui.lineEdit.text()
        
        if text:
            # Kullanıcı mesajını HEMEN ekle
            self.add_message(f"You: {text}", is_user=True)
            self.ui.lineEdit.clear()
            print(f"Gönderilen mesaj: {text}")
            
            # Sinyalleri oluştur
            signals = WorkerSignals()
            signals.finished.connect(lambda msg: self.add_message(f"AI: {msg}", is_user=False))
            signals.error.connect(lambda err: self.add_message(f"Hata: {err}", is_user=False))
            
            # AI cevabını arka planda al
            thread = threading.Thread(target=self.get_ai_response, args=(text, signals))
            thread.daemon = True
            thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
