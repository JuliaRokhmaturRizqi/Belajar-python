class ATM:
    def __init__(self, saldo_awal):
        self.saldo = saldo_awal

    def cek_saldo(self):
        print(f"Saldo Anda saat ini: {self.saldo}")

    def tarik_tunai(self, jumlah):
        if jumlah > 0 and jumlah <= self.saldo:
            self.saldo -= jumlah
            print(f"Anda berhasil menarik tunai sebesar {jumlah}")
        else:
            print("Maaf, saldo tidak mencukupi atau jumlah penarikan tidak valid")

    def setor_tunai(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            print(f"Anda berhasil setor tunai sebesar {jumlah}")
        else:
            print("Maaf, jumlah setoran tidak valid")

def main():
    # Inisialisasi ATM dengan saldo awal
    atm = ATM(10000)

    while True:
        print("\n=== Menu ATM ===")
        print("1. Cek Saldo")
        print("2. Tarik Tunai")
        print("3. Setor Tunai")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1-4): ")

        if pilihan == '1':
            atm.cek_saldo()
        elif pilihan == '2':
            jumlah_tarik = int(input("Masukkan jumlah yang ingin ditarik: "))
            atm.tarik_tunai(jumlah_tarik)
        elif pilihan == '3':
            jumlah_setor = int(input("Masukkan jumlah yang ingin disetor: "))
            atm.setor_tunai(jumlah_setor)
        elif pilihan == '4':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1-4.")

if __name__ == "__main__":
    main()
