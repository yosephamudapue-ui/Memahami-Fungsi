def hitung_gaji_lembur( gaji_pokok, total_jam_kerja):
    if total_jam_kerja > 40:
        jam_lembur = total_jam_kerja - 40
        upah_lembur = jam_lembur * 50000
        total_gaji = gaji_pokok + upah_lembur
    else:
        total_gaji = gaji_pokok
        
    return total_gaji

print(hitung_gaji_lembur( 4000000, 45))
