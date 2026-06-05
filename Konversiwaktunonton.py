def koversi_menit(jumlah_episode, durasi_per_episode):
    total_menit = jumlah_episode * durasi_per_episode
    jam = total_menit // 60
    menit = total_menit % 60
    return jam, menit
jam, menit = koversi_menit (5, 45)
print("jam:", jam)
print("menit:", menit)
    
