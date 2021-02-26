import sys
import requests
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow


class API_MAP(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design_map.ui', self)
        self.show_button.clicked.connect(self.treatment)

    def treatment(self):
        coor_x_y, scale_x_y = self.coor_x_y.text().split(), self.scale_x_y.text().split()
        cor_y, cor_x = coor_x_y[0].replace(',', ''), coor_x_y[-1]
        scale_x, scale_y = scale_x_y[0].replace(',', ''), scale_x_y[-1]
        map_request = "https://static-maps.yandex.ru" \
                      "/1.x/?ll={},{}&spn={},{}&l=sat".format(cor_x, cor_y, scale_x, scale_y)
        response = requests.get(map_request)
        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        self.pixmap = QPixmap(map_file)
        self.show_map.setPixmap(self.pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = API_MAP()
    ex.setWindowIcon(QIcon('icon.png'))
    ex.setWindowTitle('Большая задача по Maps API')
    ex.show()
    sys.exit(app.exec_())