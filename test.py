from flask import Flask, render_template

app = Flask(__name__)


@app.route('/soft')
def index():
    return "<h1>Softcoins. Hello world</h1>"



app.run()
