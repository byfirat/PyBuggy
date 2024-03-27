from flask import Flask, render_template

uygulama = Flask(__name__)

@uygulama.route("/")
def anasayfa():
    return "Merhaba, dünya!"

@uygulama.route("/iletisim")
def iletisim():
    return render_template("iletisim.html")

if __name__ == "__main__":
    uygulama.run(debug=12)