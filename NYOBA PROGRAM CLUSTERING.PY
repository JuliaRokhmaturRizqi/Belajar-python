import math
import pandas as pd

# Data yang diberikan
# Format: (lebar, tinggi)
data = [
    (1.0, 2.0),
    (1.0, 2.25),
    (0.5, 2.0),
    (1.5, 1.0),
    (2.0, 1.8),
    (2.25, 2.0),
    (2.5, 2.5),
    (0.5, 1.0),
    (2.0, 2.5),
    (1.0, 2.5)
]

def kmeans_iteration(x1, y1, x2, y2):
    # Menyimpan centroid berdasarkan input user
    centroid1 = (x1, y1)  # Centroid Cluster 1
    centroid2 = (x2, y2)  # Centroid Cluster 2

    results = []
    decisions = []

    for idx, (x, y) in enumerate(data, start=1):
        # Hitung jarak Euclidean ke masing-masing centroid
        d_c1 = math.sqrt((x - x1)**2 + (y - y1)**2)
        d_c2 = math.sqrt((x - x2)**2 + (y - y2)**2)

        # Menentukan cluster berdasarkan jarak terdekat
        if d_c1 < d_c2:
            cluster = 'C1'
        else:
            cluster = 'C2'

        results.append([idx, (x, y), round(d_c1, 2), round(d_c2, 2)])
        decisions.append([idx, round(d_c1, 2), round(d_c2, 2), cluster])

    # Membuat dataframe untuk tabel hasil jarak
    df_jarak = pd.DataFrame(results, columns=["Data ke", "(x,y)", "Jarak ke C1", "Jarak ke C2"])
    print(df_jarak.to_string(index=False))
    # Membuat dataframe untuk tabel keputusan
    df_keputusan = pd.DataFrame(decisions, columns=["Data ke", "Jarak ke C1", "Jarak ke C2", "Masuk Cluster"])
    print("pilihan favorit prodi informatika")
    print(df_keputusan.to_string(index=False))
    # Menampilkan anggota masing-masing cluster
    cluster1 = df_keputusan[df_keputusan['Masuk Cluster'] == 'C1']['Data ke'].tolist()
    cluster2 = df_keputusan[df_keputusan['Masuk Cluster'] == 'C2']['Data ke'].tolist()

    print("\nHasil Cluster:")
    print(f"Cluster 1: {cluster1}")
    print(f"Cluster 2: {cluster2}")

if __name__ == "__main__":
    print("Masukkan koordinat untuk Centroid 1 (Cluster 1):")
    x1 = float(input("  Masukkan nilai x1: "))
    y1 = float(input("  Masukkan nilai y1: "))

    print("Masukkan koordinat untuk Centroid 2 (Cluster 2):")
    x2 = float(input("  Masukkan nilai x2: "))
    y2 = float(input("  Masukkan nilai y2: "))

    kmeans_iteration(x1, y1, x2, y2)
