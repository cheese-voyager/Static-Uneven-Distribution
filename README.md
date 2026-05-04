# Static-Uneven-Distribution

## Explanation

**Initializing Static Uneven Distribution**: Kode dimulai dengan mendeklarasikan sebuah array `static_uneven_distribution = [120.0, 10.0, 30.0, 80.0, 10.0]`. Ini mensimulasikan kondisi di mana sistem telah diberikan alokasi data secara statis, namun bebannya timpang (ada yang kelebihan beban, ada yang menganggur).

**Calculating Target Ideal Distribution**: Kode menghitung total beban dan membaginya dengan jumlah node. Hasil perhitungan ini (50.0) menjadi patokan/target (Ideal Distribution) di mana sistem dianggap seimbang secara optimal.

**Iterative Diffusion Process**: Memasuki blok `while True`, program melakukan iterasi pergerakan beban. Jika sebuah node memiliki beban lebih besar dari tetangganya, sebagian bebannya (`alpha = 0.2`) ditransfer ke tetangga tersebut. Ini mewakili mekanisme redistribusi bottleneck.

**Reaching Ideal Distribution (Stopping Condition)**: Pada setiap akhir iterasi, program melakukan pengecekan `all(abs(load - ideal_distribution) < 0.5)`. Baris ini bertugas secara spesifik untuk "show when the code reach the ideal distribution". Ketika selisih beban semua node sudah di bawah margin toleransi 0.5 dari target ideal, loop berhenti dan mencetak iterasi ke berapa keseimbangan tersebut berhasil dicapai.