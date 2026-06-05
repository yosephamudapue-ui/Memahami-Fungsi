def cek_diskon(total_harga, jumlah_tiket, kode_kupon):
    if kode_kupon == "NONTONSERU" and jumlah_tiket >=2:
        total_harga = total_harga - 15000
    return total_harga
hasil = cek_diskon(100000, 2, "NONTONSERU")
print(hasil)
