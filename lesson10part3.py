class OperasiMath:
    global bil1,bil2,hasil

    def penjumlahan(self):
        self.hasil = self.bil1 + self.bil2
        print('Hasil penjumlahan',self.bil1,'dan',self.bil2,'adalah',self.hasil)

    def pengurangan(self):
        self.hasil = self.bil1 - self.bil2
        print('Hasil pengurang',self.bil1,'dan',self.bil2,'adalah',self.hasil)

    def perkalian(self):
        self.hasil = self.bil1 * self.bil2
        print('Hasil perkalian', self.bil1, 'dan', self.bil2, 'adalah', self.hasil)

    def pembagian(self):
        self.hasil = self.bil1 / self.bil2
        print('Hasil penmbagian', self.bil1, 'dan', self.bil2, 'adalah', self.hasil)