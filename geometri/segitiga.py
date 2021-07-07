class Segitiga():

    def __init__(self, alas, tinggi):
        self.a = alas
        self.t = tinggi

    def info(self):
        return f'Ini adalah object dari Segitiga dengan alas = {self.a} dan tinggi = {self.t}'

    def hitung_luas(self):
        return self.a * self.t /2