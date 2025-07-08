from flask import Flask, render_template
from post import Post

app = Flask(__name__)
post = Post()

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
