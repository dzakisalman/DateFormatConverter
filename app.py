from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

def format_tanggal(tanggal_list):
    hasil = []
    for tanggal in tanggal_list:
        try:
            dt = datetime.strptime(tanggal.strip(), "%Y-%m-%d %H:%M:%S")
            hasil.append(dt.strftime("%d/%m/%Y"))
        except ValueError:
            hasil.append(f"❌ Format salah: {tanggal}")
    return hasil

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = []
    if request.method == "POST":
        tanggal_text = request.form["tanggal"]
        tanggal_list = tanggal_text.split("\n")
        hasil = format_tanggal(tanggal_list)
    return render_template("index.html", hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)
