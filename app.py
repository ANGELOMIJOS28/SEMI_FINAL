import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return ("Angelo S. Mijos<br>"
            "BSIT 3A<br>"
            "SYSTEM INTEGRATION<br>"
            "SEMI FINAL EXAM")

if __name__ == "__main__":
    app.run(debug=True)
    port = int(os.inviron.get("PORT", 5000))
    app.run(host='0.0.0.0',port=port)