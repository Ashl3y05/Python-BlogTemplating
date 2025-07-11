from flask import Flask, render_template
from post import Post

app = Flask(__name__)
post = Post()

@app.route('/')
def home():
    return render_template("index.html", posts = post.get_all_blog_post())

@app.route('/post/<blog_num>')
def blog(blog_num):
    return render_template("post.html", blog=post.get_specific_post(blog_num))

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
