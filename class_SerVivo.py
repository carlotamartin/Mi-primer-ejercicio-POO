class SerVivo:
    def __init__(self):
        self._vivo = True
    def is_vivo(self):
        return self._vivo
    def morir(self):
        self._vivo= False
#Se pone _ porque es una clase abstracta y solo se puede usar en esta clase