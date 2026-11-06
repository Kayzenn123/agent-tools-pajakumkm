# PajakUMKM — Radio Pajak 0,5 FM

Kalkulator PPh final 0,5% buat UMKM, dibungkus stasiun radio tua: isi omzet 12 bulan,
pajak per bulan + total setahun langsung keluar. 100% di browser, tanpa server, tanpa daftar.

**Live:** https://kayzenn123.github.io/agent-tools-pajakumkm/
**Repo:** https://github.com/Kayzenn123/agent-tools-pajakumkm

## Fitur

- 12 input omzet bulanan (format ribuan otomatis) + hitung live 0,5% per bulan
- Toggle wajib pajak: orang pribadi / PT Perorangan / koperasi
  - Orang pribadi: bagian omzet s.d. Rp500 jt/tahun (kumulatif) tidak dipungut PPh final;
    0,5% hanya atas bagian di atas Rp500 jt; tanpa batas waktu (PP 20/2026)
  - PT Perorangan: 0,5% sejak rupiah pertama, tanpa batas waktu
  - Koperasi: 0,5% sejak rupiah pertama, maksimal 4 tahun sejak terdaftar
  - Di atas Rp4,8 M/tahun: stempel LEWAT BATAS — tetap final 0,5% sampai akhir tahun pajak ini, tahun depan tarif umum
- Dial radio raksasa: jarum bergerak mengikuti total omzet vs batas Rp4,8 M
- Peta frekuensi: strip 12 stasiun bulan, bisa diseret (drag + inertia) & keyboard ←/→
- Rekap: total pajak (count-up), grafik batang SVG 12 bulan, tabel + naik/turun %,
  jatuh tempo bayar (tanggal 15 bulan berikutnya)
- 3 preset usaha contoh: Warung Kopi, Toko Kelontong, Laundry Kiloan
- Deep-link `?pajak=` (snapshot base64) + banner muat/abaikan
- Ekspor CSV/JSON, impor JSON, cetak rekap, salin ringkasan WA, salin tautan
- Riwayat perhitungan di localStorage (simpan/muat/hapus, maks 10)
- Easter egg: ketuk logo 5× → mode "siaran malam"

## Aturan pajak yang dipakai (sumber: PP 55/2022 jo. PP 20/2026, berlaku 22 Apr 2026)

- Tarif PPh final 0,5% dari omzet bruto (bukan laba) tiap bulan
- Batas omzet Rp4,8 miliar/tahun, diuji agregasi seluruh usaha + keluarga
- Pembebasan s.d. Rp500 juta/tahun (kumulatif) hanya untuk wajib pajak orang pribadi;
  0,5% hanya atas bagian omzet di atas Rp500 jt
- Bayar paling lambat tanggal 15 bulan berikutnya (kode billing 411128-420);
  lapor SPT Masa paling lambat tanggal 20
- Masa pakai tarif: orang pribadi & PT Perorangan tanpa batas waktu; koperasi maks 4 tahun
- Subjek baru: hanya orang pribadi, PT Perorangan, koperasi (CV/PT biasa bukan penerima baru)
- Alat hitung contoh, bukan saran pajak — cek https://www.pajak.go.id

## Tech

Astro 7 + Tailwind CSS v4 (template AstroWind) · vanilla JS (tanpa framework gerak —
GSAP dibuang demi bobot; animasi transform/opacity/clip-path murni) · font Jaini /
Noto Sans Thai / Ruthie via Astro Fonts API (Fontsource, self-host) · ikon Phosphor Bold
(isometrik) · deploy GitHub Pages (branch `gh-pages`, base `/agent-tools-pajakumkm`).

## Skor

- `tools/qa.js` (Chromium): 4 viewport, 0 overflow, 0 console error, 1 small tap target
  (tautan teks inline `pajak.go.id` — pengecualian target inline WCAG 2.5.8)
- FPS CPU throttle 4×: **60,4**
- Lighthouse (CHROME_PATH=playwright-chromium, terukur di VM): mobile **97/100/100/100**,
  desktop **100/100/100/100** (performance/accessibility/best-practices/SEO)
- Kontras AA terverifikasi di browser: teks 15,72 · muted 5,83 · aksen 6,20 · pop 8,66
- Tes fungsi Playwright: 10/10 lulus (hitung PT Rp612.500, bebas OP kumulatif, validasi huruf,
  deep-link, clipboard, riwayat, easter egg, keyboard strip, kumulatif tembus Rp500 jt,
  koperasi tanpa pembebasan)

## Cara jalanin

```bash
npm install
npm run build   # output ke dist/
```

## Kredit

- Font: Jaini, Noto Sans Thai, Ruthie (OFL, Google Fonts / Fontsource)
- Ikon: Phosphor Icons (MIT)
- Data contoh omzet: contoh fiktif, dilabeli "contoh" di situs
