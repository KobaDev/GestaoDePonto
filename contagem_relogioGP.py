################################################################
## IMPORT DE RECURSO PARA INTERAÇÃO COM THREADING
################################################################
from PyQt5.QtCore import pyqtSignal, QObject
from acessoGP import Win
import threading
import time

################################################################
## RECURSO INTERNOS CRIADOS PELOS ALUNOS
################################################################
import pega_horarioGP
import acessoGP

class Worker(QObject, acessoGP(Win)):
    updateDate = pyqtSignal()
    trigger = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(Worker, self).__init__(*args, **kwargs)

    def attData(self):
        Win.pontoT.txtTime.setText(pega_horarioGP.curlHoraStr())

    def relogio(self):
        self.updateDate.connect(self.attData)
        while(True):
            time.sleep(1)
            self.updateDate.emit()