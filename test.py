from flask import Flask, render_template

app = Flask(__name__)


@app.route('/softcoin')
def index():
    return render_template('softcoin.html')



app.run()