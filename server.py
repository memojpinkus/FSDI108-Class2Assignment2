from flask import Flask

app = Flask("Server")

@app.route("/")
def home():
    return "Hello from flask"

@app.route("/me")
def about_me():
    return "Guillermo Jimenez"

app.run(debug=True)