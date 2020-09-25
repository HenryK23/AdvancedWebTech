from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
    return "The default, 'root' route"

@app.route("/hello/")
def hello():
    return "Why does this not work" 

@app.route("/goodbye/")
def goodbye():
    return "Goodbye cruel world :^("

@app.route("/Jeff/")
def jeff():
    return "My name is jeff"



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = true)

