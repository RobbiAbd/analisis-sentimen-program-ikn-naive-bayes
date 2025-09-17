# Analisis Sentimen Masyarakat pada Platform TikTok

Proyek ini bertujuan untuk menganalisis sentimen masyarakat terhadap isu tertentu (misal proggram ikn) berdasarkan komentar atau teks dari platform TikTok. Dataset sudah diproses menjadi CSV dan dianalisis menggunakan Python, Sastrawi, dan Naive Bayes. Hasil analisis ditampilkan melalui visualisasi.

---

## Fitur

- Preprocessing teks: lowercase, hapus URL, hashtag, mention, simbol, stemming bahasa Indonesia.
- Handling missing values (NaN) di kolom `text` dan `label`.
- Normalisasi label sentimen.
- Analisis sentimen menggunakan Naive Bayes (bisa diperluas dengan algoritma lain).
- Visualisasi hasil analisis (matplotlib & seaborn).
- Diintegrasikan dengan web app menggunakan Flask.

## Instalasi

1. Clone repository:
```bash
git clone <repository-url>
cd <project-folder>
```