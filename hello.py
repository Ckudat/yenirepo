from flask import Flask

ilkproje = Flask(__name__)

@ilkproje.route("/")
def anasayfa():
    mesaj = "İlk Flask Sayfam" 
    return mesaj

if __name__ == '__main__':
    ilkproje.run(debug=False)
    