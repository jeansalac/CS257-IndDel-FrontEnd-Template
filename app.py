import ProductionCode.core as core
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title=core.example(), name=core.example())

if __name__ == '__main__':
    app.run()