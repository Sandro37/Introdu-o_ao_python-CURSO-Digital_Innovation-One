#construindo métodos, funções e classes em python
class Televisao:
    def __init__(self):
        self.ligada  = False
        self.canal = 5
    def power(self):
        self.ligada = not self.ligada

    def aumentar_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1


if __name__ == '__main__':
    tv = Televisao()
    print('Televisão ligada: {}'.format(tv.ligada))
    tv.power()
    print('Televisão ligada: {}'.format(tv.ligada))
    tv.power()
    print('Televisão ligada: {}'.format(tv.ligada))
    tv.power()
    print('Televisão ligada: {}'.format(tv.ligada))
    print('Canal: {}'.format(tv.canal))
    tv.aumentar_canal()
    tv.aumentar_canal()
    print('Canal: {}'.format(tv.canal))
    tv.diminui_canal()
    print('Canal: {}'.format(tv.canal))