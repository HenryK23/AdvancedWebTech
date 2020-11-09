from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)


@app.route('/')
def base():
    return redirect(url_for("home"))

@app.route('/flashycards/')
def root():
    return render_template('MasterPage.html'), 200

@app.route('/flashycards/home/')
def home():
    return render_template('homePage.html'), 200

@app.route('/flashycards/home/about/')
def about():
    return render_template('aboutPage.html'), 200

@app.route('/flashycards/home/createset/')
def createset():
    return render_template('createSet.html')

@app.route('/flashycards/home/openset/')
def openset():
    return render_template('openSet.html')

@app.route('/flashycards/home/openset/flashcard/')
def flashcard():
    return render_template('flashCard.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    
