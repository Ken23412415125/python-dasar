from lesson10part2 import OperasiMatematika

print('=' * 25)
print('Operasi Matematika')
print(' 1. Jumlah \t [+]')
print(' 2. Kurang \t [-]')
print(' 3. Kali \t [*]')
print(' 4. Bagi \t [/]')

operasi = input('Pilih operasi(1/2/3/4):')
bilangan_1 = eval(input('Masukkan bilangan pertama '))
bilangan_2 = eval(input('Masukkan bilangan kedua '))

hasil=OperasiMatematika

if operasi == '1':
    hasil.penjumlahan(bilangan_1,bilangan_2)
elif operasi == '2':
    hasil.pengurangan(bilangan_1,bilangan_2)
elif operasi == '3':
    hasil.perkalian(bilangan_1,bilangan_2)
elif operasi == '4':
    hasil.pembagian(bilangan_1, bilangan_2)
else:
    print('Tidak valid')