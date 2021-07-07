class PersegiPanjang():
    def __init__(self, p,l):
        #init adalah fungsi yang dipanggil pertama kali saat object diciptakan
        self.p = p
        self.l = l

    def info(self): #fungsi/method
        return f'Ini adalah object dari Persegi Panjang dengan panjang = {self.p} dan lebar = {self.l}'

    def hitung_luas(self):
        return self.p * self.l
