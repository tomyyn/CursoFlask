from flask import Flask, render_template

app = Flask(__name__)

all_posts = [
    {
        "title":"Post 1",
        "content":"Contenido del post 1",
        "author":"Aaron"
    },
    {
        "title":"Post 2",
        "content":"Contenido del post 2"
    },
]

@app.route("/")
def index():
    return (render_template("index.html"))

@app.route("/home/<string:name>/posts/<int:id>")
def hello(name, id):
    return "Hello, " + name + ", your post ID is " + str(id)

@app.route("/onlyget", methods = ["POST"])
def get_req():
    return "You can only get this!"

@app.route("/post")
def posts():
    return (render_template("posts.html", posts = all_posts))

if __name__ == "__main__":
    app.run(debug=True)
