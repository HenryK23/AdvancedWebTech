from flask import Flask, render_template, redirect, url_for, request
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

@app.route('/flashycards/home/about/<text>')
def about(text):
    return render_template('aboutPage.html',text=text)

@app.route('/flashycards/home/createset/', methods=['GET', 'POST'])
def createset():
    if request.method == 'POST':
        setName = request.form['setName']
        print(setName)
        strQuestionCount="5"
        strQuestionCount = request.form['questionCount']
        intQuestionCount = int(strQuestionCount)
        return redirect(url_for("questions", intQuestionCount=intQuestionCount))
    else: 
        return render_template('createSet.html')

@app.route('/flashycards/home/openset/<text>')
def openset(text):
    return render_template('openSet.html', text=text)

@app.route('/flashycards/home/openset/flashcard/')
def flashcard():
    return render_template('flashCard.html')

@app.route('/flashycards/home/createset/questions/<intQuestionCount>')
def questions(intQuestionCount):
    return render_template('createQuestion.html', questionCount=intQuestionCount)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    
