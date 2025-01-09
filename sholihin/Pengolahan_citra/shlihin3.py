# Input tanggal lahir
tanggal_lahir = "11-12-2002"  # Format: DD-MM-YYYY

# Pecah tanggal, bulan, dan tahun
tanggal, bulan, tahun = map(int, tanggal_lahir.split('-'))

# Ambil nilai sesuai kebutuhan
tanggal_lahir_value = tanggal  # Tanggal
bulan_lahir_value = bulan      # Bulan
angka_terakhir_tahun = int(str(tahun)[-1])  # Angka terakhir tahun

# Cetak hasil
print("Tanggal_Lahir:", tanggal_lahir_value)
print("Bulan_Lahir:", bulan_lahir_value)
print("Angka Terakhir Tahun:", angka_terakhir_tahun)