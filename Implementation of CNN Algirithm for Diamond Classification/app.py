from flask import Flask, render_template

app = Flask(__name__)

class Rute:
    def __init__(self, nama, jarak, rutenya, gambar):
        self.nama = nama
        self.jarak = jarak
        self.rutenya = rutenya
        self.gambar = gambar

def cari_jarak_terpendek(rutes):
    rute_terpendek = None
    for rute in rutes:
        if rute_terpendek is None or rute.jarak < rute_terpendek.jarak:
            rute_terpendek = rute
    return rute_terpendek

@app.route('/')
def index():
    judul_rute = "Dari Gereja HKBP Balige ke Gereja Katolik Paroki Santo Josep Balige"
    
    rutes = [
        Rute("Rute 1", 3.6, ["Gereja HKBP Balige", "Jl.Patuan Nagari", "Jl.Dr.Sutomo", "Jl.Tarutung", "Jl.Liberty Manik", "Jl.Simanjalo", "Gereja HKBP Soposurung Balige"], "rute1.jpg"),
        Rute("Rute 2", 3.0, ["Gereja HKBP Balige", "Jl.Patuan Nagari", "Jl.Liberti Manik", "Jl.Simanjalo", "Gereja HKBP Soposurung Balige"], "rute2.jpg"),
        Rute("Rute 3", 3.7, ["Gereja HKBP Balige", "Jl. Gereja", "Jl.Somba Debata", "Jl.By pass Balige", "Jl.Simanjalo", "Gereja HKBP Soposurung Balige"], "rute3.jpg"),
        Rute("Rute 4", 3.4, ["Gereja HKBP Balige", "Jl.Patuan Nagari", "Jl.Dr.Sutomo", "Jl.Tarutung", "Jl.Malanton Siregar", "Jl.Liberty Manik", "Jl.Simanjalo", "Gereja HKBP Soposurung Balige"], "rute4.jpg"),
        Rute("Rute 5", 2.9, ["Gereja HKBP Balige", "Jl.Gereja", "Jl.Raja Bonanionan", "Jl.Sianipar", "Jl.Simanjalo", "Gereja HKBP Soposurung Balige"], "rute5.jpg"),
    ]

    return render_template('index.html', rutes=rutes, judul_rute=judul_rute)

@app.route('/tampilkan_rute_terpendek', methods=['POST'])
def tampilkan_rute_terpendek():
    judul_rute = "Dari Gereja HKBP Balige ke Gereja Katolik Paroki Santo Josep Balige"
    
    rutes = [
        Rute("Rute 1", 3.6, ["Gereja HKBP Balige", "Jl.Patuan Nagari", "Jl.Dr.Sutomo", "Jl.Tarutung", "Jl.Liberty Manik", "Jl.Simanjalo", "Gereja HKBP Soposurung Balige"], "rute1.jpg"),
        Rute("Rute 2", 3.0, ["Gereja HKBP Balige", "Jl.Patuan Nagari", "Jl.Liberti Manik", "Jl.Simanjalo", "Gereja HKBP Soposurung Balige"], "rute2.jpg"),
        Rute("Rute 3", 3.7, ["Gereja HKBP Balige", "Jl. Gereja", "Jl.Somba Debata", "Jl.By pass Balige", "Jl.Simanjalo", "Gereja HKBP Soposurung Balige"], "rute3.jpg"),
        Rute("Rute 4", 3.4, ["Gereja HKBP Balige", "Jl.Patuan Nagari", "Jl.Dr.Sutomo", "Jl.Tarutung", "Jl.Malanton Siregar", "Jl.Liberty Manik", "Jl.Simanjalo", "Gereja HKBP Soposurung Balige"], "rute4.jpg"),
        Rute("Rute 5", 2.9, ["Gereja HKBP Balige", "Jl.Gereja", "Jl.Raja Bonanionan", "Jl.Sianipar", "Jl.Simanjalo", "Gereja HKBP Soposurung Balige"], "rute5.jpg"),
    ]

    rute_terpendek = cari_jarak_terpendek(rutes)

    return render_template('index.html', rutes=rutes, rute_terpendek=rute_terpendek, judul_rute=judul_rute)

if __name__ == '__main__':
    app.run(debug=True)
