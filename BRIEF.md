# BRIEF — PajakUMKM — 2026-11-06

## Masalah/usecase (1 kalimat + siapa yang kena)
Pemilik warung/toko/UMKM tidak tahu berapa PPh final 0,5% yang harus dibayar tiap bulan dari omzetnya — PajakUMKM menghitungnya dari 12 bulan omzet, lengkap dengan cek batas omzet dan pengingat jatuh tempo.

## Konsep visual (1 kalimat)
Situs = satu stasiun radio tua "RADIO PAJAK 0,5 FM": angka 0,5% raksasa jadi pintu poster, 12 bulan omzet = 12 stasiun di peta frekuensi yang bisa digeser, penyiar (Pak Siaran) yang membacakan hasil hitung dengan suara loket radio.

## Hasil seed (builds/2026-11-06/seed.json, seed 2027-01-08)
- domain: radio tua · layout: poster tipografi raksasa · referensi: peta transit
- constraint: satu ukuran biasa + satu ukuran raksasa
- gerak: kamera canvas drag + zoom scroll · marquee ikon SVG + teks (3 band) · teks di path melengkung · cursor senter/spotlight mask · reveal morph SVG blob mask
- ikon: isometrik, sumber Phosphor · font: Jaini (display) / Noto Sans Thai (body) / Ruthie (aksen)
- palet: dark/complementary hue 114 — bg oklch(0.18 0.056 114) hijau malam, text oklch(0.94 0.020 114), accent oklch(0.72 0.253 294) ungu siaran, accent2 oklch(0.62 0.226 294), pop oklch(0.82 0.247 291)
- kontras AA terverifikasi (skrip node): text/bg 15.74, muted/bg 5.82, accent/bg 6.21, pop/bg 8.70 — semua ≥ 4.5. Catatan: JANGAN teks terang di atas accent (2.54); teks di atas accent pakai warna bg (6.21).

## 3 arah desain (2 kalimat masing-masing) + arah terpilih dan alasannya
1. **Kantor pajak 1987**: formulir kertas + stempel + meja petugas; rapi tapi mirip SlipGaji (blueprint) dan KarcisParkir (karcis) — terlalu dekat dengan 2 build terakhir.
2. **Radio tua 0,5 FM (TERPILIH)**: poster tipografi raksasa "0,5%" + dial radio yang diputar + peta frekuensi 12 stasiun bulan; domain radio belum pernah dipakai, layout poster raksasa terakhir 2026-10-28 (BidKit, 9 hari lalu, font/palet/gerak beda semua).
3. **Peta transit omzet**: jalur kereta 12 stasiun; kuat tapi layout horizontal-scroll sudah dipakai REL80 (2026-10-29) dan GOWES — tabrakan sumbu layout.
Alasan pilih #2: domain + layout + font + palet + gerak semuanya beda dari 14 build terakhir (cek LOG.md); metafora frekuensi 0,5 FM = tarif 0,5% bikin konsep nempel di kepala.

## Keputusan berani
Tanpa navbar dan tanpa hero marketing — pengunjung langsung di depan radio: dial raksasa "0,5%" + satu kolom omzet Januari yang sudah terisi contoh, tombol HITUNG langsung kelihatan dalam 3 detik. Seluruh situs hanya memakai 2 ukuran font (biasa 16px + raksasa clamp 18–30vw) sesuai constraint seed.

## Persona/suara
Pak Siaran — penyiar radio tua yang ramah, ngomong pakai bahasa loket: "Selamat pagi, pendengar setia 0,5 FM", "Omzetnya kosong, Mas — isi dulu satu bulan", "Pajak bulan ini: Rp25.000. Lunas sebelum tanggal 15, ya."

## Palet (harmoni, kenapa, psikologi warna, token oklch final, hasil cek kontras AA)
- Harmoni complementary hue 114 (hijau malam) vs 294 (ungu siaran) — hijau = uang/tenang, ungu = siaran/malam radio; pop 291 dipakai <5% area (stempel LUNAS).
- Token: --bg oklch(0.18 0.056 114) · --surface oklch(0.21 0.040 114) · --text oklch(0.94 0.020 114) · --muted oklch(0.65 0.030 114) · --accent oklch(0.72 0.253 294) · --accent-2 oklch(0.62 0.226 294) · --pop oklch(0.82 0.247 291)
- Kontras AA: text 15.74, muted 5.82, accent 6.21, pop 8.70 (semua lolos ≥4.5).

## Font (display/body/aksen, alasan, id Fontsource, variable atau bukan)
- Display: Jaini (id: jaini) — display dekoratif tegas, cocok untuk angka raksasa "0,5%".
- Body: Noto Sans Thai (id: noto-sans-thai) — sans bersih, weight 400+700 tersedia, terbaca di 390px.
- Aksen: Ruthie (id: ruthie) — tulisan tangan untuk suara penyiar ("selamat pagi…").
- Bukan variable font → axis wght TIDAK dianimasikan; ganti dengan scramble/flip huruf.

## Ikon (gaya, sumber, daftar 12+ ikon, 3+ custom)
- Gaya: isometrik, sumber Phosphor (ph:*-bold). 12+ ikon: radio, calculator, calendar, coins, receipt, alarm/bell, download, upload, copy/link, printer, trash, check, warning, chart-bar, wallet, storefront, arrow.
- Custom SVG (3+): dial radio bundar dengan jarum, stempel LUNAS, gelombang frekuensi (peta 12 stasiun), antena radio.

## Gerak (kategori A-F yang dipakai, narasi yang menyatukan, MODE RINGAN apa yang dimatikan)
Narasi: scroll = memutar dial radio masuk ke dalam siaran; marquee = suara siaran berjalan; kursor = senter studio.
- A kamera: zoom-in saat scroll lalu pan kanan (hero → peta frekuensi → rekap).
- B marquee: 3 band beda kecepatan (teks + ikon SVG), arah berlawanan, skew saat scroll cepat, tombol jeda.
- C teks: judul di path melengkung (SVG textPath "RADIO PAJAK 0,5 FM"), scramble saat angka berubah.
- D input: cursor senter/spotlight mask di hero (desktop saja).
- E reveal: morph SVG blob mask saat kartu hasil muncul; garis draw-on lalu isi di peta frekuensi.
- F: tidak dipakai.
- MODE RINGAN: matikan spotlight + marquee jadi statis + zoom diganti fade singkat.

## Storyboard hero moment (tabel scroll 0/25/50/75/100%)
| Scroll | Yang terlihat | Kamera (zoom/pan) | Marquee | Teks | Interaksi |
| --- | --- | --- | --- | --- | --- |
| 0% | dial radio + "0,5%" raksasa + kolom Januari | zoom 1.0, hero penuh | band 1 jalan | "0,5%" scale-in | ketik omzet → angka pajak live |
| 25% | peta frekuensi 12 stasiun bulan | zoom 1.15, pan kanan | band 1+2 berlawanan | textPath melengkung muncul | klik stasiun bulan → isi omzet |
| 50% | tabel rekap 12 bulan + total tahunan | pan kanan, zoom 1.0 | band 2+3 | angka total count-up | tombol HITUNG → hasil morph |
| 75% | cek batas omzet + pengingat jatuh tempo | zoom-out 0.9 | band 3 | stempel LUNAS/WASPADA | toggle WP orang pribadi/badan |
| 100% | ekspor/salin/cetak + riwayat tersimpan | zoom-out penuh, footer | semua band pelan | Ruthie: "sampai jumpa di siaran berikut" | salin WA / unduh CSV |

Pertunjukan utama: dial raksasa "0,5%" yang jarumnya bergerak mengikuti total omzet saat pengguna mengetik (0% → penuh). Pengunjung dalam 5 detik pertama paham: ini radio pajak, masukkan omzet, pajak langsung keluar.

## Konten (15+ item nyata, easter egg)
- 12 bulan contoh (omzet warung kopi nyata-rasa, dilabeli contoh): Jan 8,2jt … Des 14,5jt.
- 3 preset usaha contoh: Warung Kopi (omzet 8–15jt/bln), Toko Kelontong (12–20jt), Laundry Kiloan (6–10jt).
- Aturan pajak tampil sebagai "jadwal siaran" (terverifikasi 2026-11-06, sumber DJP pajak.go.id + Kemenkeu Media Keuangan + Pajakku): tarif 0,5% dari omzet bruto (PP 55/2022 jo. PP 20/2026, berlaku 22 Apr 2026), batas omzet Rp4,8 M/tahun (agregasi seluruh usaha + keluarga; lewat batas → tetap final sampai akhir tahun pajak, tahun depan tarif umum), pembebasan Rp500 jt/tahun KUMULATIF hanya untuk orang pribadi (0,5% hanya atas bagian di atas Rp500 jt; PT Perorangan & koperasi kena sejak rupiah pertama), jatuh tempo bayar tanggal 15 bulan berikutnya (kode billing 411128-420; lapor SPT Masa tanggal 20), masa pakai tarif: OP & PT Perorangan tanpa batas waktu, koperasi maks 4 tahun; subjek baru hanya OP, PT Perorangan, koperasi (CV/PT biasa tidak lagi).
- Easter egg: ketik "siniar" di kolom pencarian/preset → dial berputar + pesan penyiar; klik logo radio 5× → mode "siaran malam" (pop ungu penuh).

## Teknik visual orisinal (2+)
1. SVG filter feTurbulence pada stempel LUNAS + dial radio (goyang hand-drawn).
2. Pola gelombang frekuensi CSS/SVG berulang sebagai divider antar-section; tipografi raksasa sebagai ilustrasi (angka 0,5% = gambar utama, tanpa foto).

## Suara
Tidak (tanpa audio; radio divisualkan saja).

## Fungsi (v2 FASE 1 — checklist)
- 12 input omzet bulanan (Rp, format ribuan otomatis) + toggle WP 3 jenis (orang pribadi / PT Perorangan / koperasi).
- Hitung live: pajak 0,5% per bulan + total tahunan + status batas (di bawah/di atas Rp4,8 M) + pembebasan Rp500 jt KUMULATIF untuk WP OP (0,5% hanya atas bagian di atas Rp500 jt; bulan tembus dihitung marginal).
- Validasi: input bukan angka / negatif → pesan spesifik suara Pak Siaran; empty state: "belum ada siaran — isi satu bulan dulu".
- Persistence: localStorage versi key `pajakumkm:v1`, validasi skema + fallback default; riwayat perhitungan simpan/muat/hapus.
- Deep-link `?pajak=` snapshot terkompresi (base64 JSON) + banner muat/abaikan.
- Ekspor CSV/JSON, impor JSON, cetak rekap (print stylesheet), salin ringkasan WA per bulan + total.
- Preset 3 usaha contoh; grafik batang 12 bulan SVG murni; perbandingan bulan-ke-bulan (naik/turun %).
- Pengingat jatuh tempo: tanggal 15 bulan berikutnya per bulan terisi, tampil di rekap.
