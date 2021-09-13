from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return (render_template("index.html"))

@app.route("/home/<string:name>/posts/<int:id>")
def hello(name, id):
    return "Hello, " + name + ", your post ID is " + str(id)

@app.route("/onlyget", methods = ["POST"])
def get_req():
    return "You can only get this!"

if __name__ == "__main__":
    app.run(debug=True)
