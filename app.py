from flask import Flask, render_template,url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template ('gg.html')

@app.route('/access/')
def show():
    return render_template('show.html')

if __name__ == '__main__':
    app.run(debug=True)