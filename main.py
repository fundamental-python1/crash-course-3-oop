from geometri.bangunruang import BangunRuang
from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import Segitiga

print('Menggunakan OOP')
p1 = PersegiPanjang(10, 3)  # p1 = object, PersegiPanjang = class
print(p1.info())
print(p1.hitung_luas())


s1 = Segitiga(4,2)
print(s1.info())
print(s1.hitung_luas())

print('\nMencoba membuat object dari kelas BangunRuang')
b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())

# Polymorpism : kemampuan object untuk merespon berbeda, terhadap pemanggilan method yang sama
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

print('\nPolymorpism')
for daftar_bangun_ruang in daftar_bangun_ruang:
    print(daftar_bangun_ruang.info())