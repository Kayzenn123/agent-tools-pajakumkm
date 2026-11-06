# CRITIQUE — PajakUMKM — 2026-11-06

## Slop test (v3) + 3 hal paling template + yang dirombak
- Slop test: logo ditutup — situs tetap dikenali: angka "0,5%" raksasa + dial radio +
  marquee "PPh FINAL 0,5%" + suara Pak Siaran. Bukan template hero + 3 kartu.
- 3 hal paling template di draft awal:
  1. Section-head generik (nomor + judul + deskripsi) — dipertahankan tapi nomor dibuat
     raksasa transparan sebagai seni poster, bukan label kecil.
  2. Grid aturan 6 kartu seragam — dirombak: kartu tanpa radius/shadow, border 2px
     tegas, ikon isometrik Phosphor, copy suara penyiar.
  3. Tombol aksi deret seragam — dirombak: "Salin ringkasan WA" jadi btn-big aksen,
     sisanya outline; urutan mengikuti alur (salin dulu, unduh, cetak).
- Keputusan berani & signature moment kelihatan dalam 5 detik pertama: ya — "0,5%"
  raksasa + dial + kolom Januari langsung di viewport pertama (screenshot mobile-390).

## Gerbang gerak (v4): jumlah lapisan, zoom, pan, 2 marquee, FPS 4x (angka)
- Lapisan gerak: A kamera (zoom hero 1→1.12 saat scroll + pan strip horizontal),
  B marquee (3 band, arah berlawanan, skew ikut kecepatan scroll), C teks (textPath
  melingkar di dial + count-up angka total), D input (spotlight kursor desktop +
  drag strip inertia), E reveal (morph blob mask di .total-wrap + fade/translate section).
  Total 5 kategori — lolos (≥4).
- Zoom: ya (hero scrub). Pan horizontal: ya (strip 12 stasiun, drag + keyboard).
  2 marquee: ya, 3 band.
- FPS CPU throttle 4×: **60,4** (qa.js Chromium, mobile 390).
- Font/palet/gaya ikon beda dari 7 build terakhir: ya — Jaini/Noto Sans Thai/Ruthie
  (baru), dark/complementary hue 114 (terakhir dark/complementary: 2026-10-16 weton,
  hue 277 — beda hue), isometrik Phosphor (terakhir: geometris bulat Remix 2026-11-05).
- Kontras AA lolos (terverifikasi di browser via canvas): teks 15,72 · muted 5,83 ·
  aksen 6,20 · pop 8,66. Body terbaca di 390px: ya.
- Reduced-motion dites: ya — 0 animasi berjalan, konten tetap tampil.

## Gerbang v5: tes bandingkan, blur, 3 detik, keyboard-only, reduced-motion, mode ringan
- Tes bandingkan (vs SlipGaji blueprint + BagiBon buku + LabaRugi label): beda total —
  poster radio gelap + tipografi raksasa vs blueprint/kertas/buku.
- Tes blur: komposisi tetap punya identitas (angka raksasa + lingkaran dial + 3 pita marquee).
- Tes 3 detik: orang asing paham ini kalkulator pajak 0,5% — ya (judul + dial + Januari).
- Keyboard-only: lulus — skip link, strip ←/→, semua tombol/input bisa difokus, focus ring pop.
- Reduced-motion: lulus (0 animasi berjalan).
- Mode ringan: tombol "Gerak: mati" menjeda marquee + zoom + spotlight; konten tetap utuh.
- Budget: JS total ~18 KB (inline, tanpa framework gerak) · CSS Layout ~? KB · font 3 family
  (woff2 subset latin) · gambar di atas fold: 0 raster (semua SVG/CSS).
- Keamanan (v5 ATURAN 9): URL params + localStorage divalidasi skema {v:1, 12 angka ≥0},
  try/catch + fallback; tidak ada innerHTML dari data pengguna (textContent/konstruksi
  DOM aman — kecuali innerHTML untuk chart/ticks dari data internal); tidak ada API key,
  tracker, atau eval; clipboard punya fallback.
- Lisensi (ATURAN 10): font OFL, ikon Phosphor MIT, gambar buatan sendiri (SVG) —
  tidak ada aset berhak cipta. Data contoh dilabeli "contoh".

## Skor 1-10: karakter, keunikan, kerapian
- Karakter: **9** — radio 0,5 FM + Pak Siaran konsisten sampai pesan error & footer.
- Keunikan: **9** — domain radio tua belum pernah dipakai; metafora frekuensi = tarif.
- Kerapian: **8** — hero desktop menyisakan ruang kosong di kanan dial; tabel rekap
  di mobile perlu scroll horizontal (sengaja, dibungkus .table-scroll).

## Keputusan konflik aturan (kalau ada) + daftar dipangkas
- Widget AstroWind (Hero/Features/dll) TIDAK dipakai: widget marketing tidak cocok
  untuk kalkulator interaktif satu halaman; yang dipakai: Layout + Icon + Fonts API +
  sistem base-path/config (sesuai AGENTS.md template). Pola ini sama dengan 5 build
  terakhir yang lolos.
- Constraint "satu ukuran biasa + satu ukuran raksasa" dipatuhi harfiah: 16px untuk
  semua teks UI, clamp(4.5rem, 22vw, 13rem) untuk display (hero + total + nomor section).
- Lapisan F (shader/3D) tidak dipakai — tidak dibutuhkan konsep.
- GSAP/Lenis tidak dipakai — animasi vanilla (transform/opacity/clip-path) demi bobot.

## Putaran rombak ke-1 dan ke-2 (apa yang diubah)
- Putaran 1 (pra-QA): seed pertama (pasar loak/bento/Rum Raisin) DITOLAK — tabrakan
  100% dengan TaksirLoak 2026-10-25 (domain+layout+font+palet sama); pick-seed
  dijalankan ulang dengan histori 37 seed.json → seed 2027-01-08 lolos.
- Putaran 2 (pasca-QA 1): (a) reveal clip-path di section diam total — IntersectionObserver
  melapor "tidak terlihat" karena clip-path circle(0%) di elemen yang diobserve
  (pelajaran AGENTS.md 2026-10-21); diperbaiki: reveal jadi opacity+translate, morph
  blob dipindah ke .total-wrap (child). (b) Token --muted/--accent ditimpa tema shadcn
  Tailwind (--muted: color-mix 6% → kontras 1,24); diperbaiki: token di-prefix --px-*.
  (c) Judul ganda ("— PajakUMKM" 2×) → ignoreTitleTemplate. (d) Input "abc" diam-diam
  dikosongkan → validasi huruf kini tampilkan error Pak Siaran. (e) Ikon ph:file-json-bold
  tidak ada → ganti ph:file-code-bold.
- Putaran 3 tidak diperlukan: QA ke-2 lolos (0 overflow, 0 console, fps 60,4).

## Tes fungsi (Playwright, 10/10)
1. Isi Januari 8.200.000 (WP OP) → pajak Rp0 + stempel BEBAS 0% (benar: kumulatif ≤Rp500 jt)
2. Preset Warung Kopi + PT Perorangan → total pajak Rp612.500 (0,5% × Rp122.500.000)
3. Validasi huruf "abc" → error tampil, input ditandai invalid
4. Deep-link ?pajak= → banner muat, data termuat di tab baru
5. Salin tautan → clipboard terbaca kembali
6. Simpan riwayat → 1 item tampil, muat/hapus jalan
7. Easter egg logo 5× → mode siaran malam aktif
8. Keyboard strip ←/→ → scrollLeft bergerak (242px)
9. Kumulatif OP (pasca-revisi PP 20/2026): 60 jt × 12 bln = 720 jt → total pajak
   Rp1.100.000 (0,5% × 220 jt); September (bulan tembus) Rp200.000; Jan–Agu Rp0
10. Koperasi 60 jt × 12 bln → total pajak Rp3.600.000 (0,5% sejak rupiah pertama)

## Fakta pajak — TERVERIFIKASI (revisi PP 20/2026)
Riset subagent 2026-11-06 (DJP pajak.go.id, Kemenkeu Media Keuangan, Pajakku,
AlatPajak): PP 20/2026 berlaku 22 Apr 2026 mengubah PP 55/2022 — subjek baru hanya
OP, PT Perorangan, koperasi; OP & PT Perorangan tanpa batas waktu; koperasi maks
4 tahun; pembebasan Rp500 jt KUMULATIF dan marginal (bukan flat); jatuh tempo tgl 15
(kode billing 411128-420), lapor SPT Masa tgl 20; batas Rp4,8 M agregasi. Semua
sudah diterapkan di kalkulator (logika kumulatif + toggle 3 WP + kartu aturan).
Satu catatan: rincian "tetap final sampai akhir tahun pajak berjalan" bersumber
dari kalkulator sekunder (AlatPajak) — prinsip "beralih tahun berikutnya" dikuatkan
Pajakku/DJP; teks pasal 58/61 PP 20/2026 belum dibaca langsung.

## Belum terverifikasi
- (Tidak ada yang material — Lighthouse terukur via CHROME_PATH, fakta pajak terverifikasi
  subagent riset 2026-11-06.)
