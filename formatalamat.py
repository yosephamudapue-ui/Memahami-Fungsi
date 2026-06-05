def format_alamat(jalan, kota, provinsi, kode_pos):
    alamat = f"jalan: {jalan}, kota: {kota}, {provinsi} ({kode_pos})"
    return alamat
print(format_alamat("Jl. Merdeka No. 10", "Bandung", "Jawa Barat", "40123"))
