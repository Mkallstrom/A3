from tasks import count_pronouns
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/count', methods=['POST'])
def count():
    pr = count_pronouns()
    return render_template('count.html', obj=pr)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
