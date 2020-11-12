from flask import Flask, render_template, redirect, url_for, request, jsonify
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
        strQuestionCount="1"
        strQuestionCount = request.form['questionCount']
        intQuestionCount = int(strQuestionCount)
        return redirect(url_for("questions", intQuestionCount=intQuestionCount,setName=setName))
    else: 
        return render_template('createSet.html')

@app.route('/flashycards/home/openset/<text>')
def openset(text):
    return render_template('openSet.html', text=text)

@app.route('/flashycards/home/openset/flashcard/<questionlist><answerlist>')
def flashcard(questionlist, answerlist):
    return render_template('flashCard.html', questionlist=questionlist, answerlist=answerlist)
    #return jsonify(questionlist, answerlist)

@app.route('/flashycards/home/createset/questions/<int:intQuestionCount><setName>', methods=['GET', 'POST'])
def questions(intQuestionCount,setName):
    if request.method == 'POST':
        #questionlist=[]
        questionlist = request.form.getlist('question[]')
        answerlist = request.form.getlist('answer[]')
        #for question in questionlist:
         #   print(question)
        return redirect(url_for("flashcard", questionlist=questionlist, answerlist=answerlist))
        
        #return jsonify(questionlist, answerlist)

    else:
        return render_template('createQuestion.html', questionCount=intQuestionCount,Name=setName)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    
