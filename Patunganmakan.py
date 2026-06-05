def hitung_patungan(total_nota, jumlah_orang, persen_tips):
    tips = total_nota * persen_tips / 100
    total = total_nota + tips
    bayar_per_orang = total / jumlah_orang
    return bayar_per_orang
hasil = hitung_patungan(400000, 4, 10)
print(hasil)
