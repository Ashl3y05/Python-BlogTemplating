from flask import Flask, render_template, request
from post import Post

app = Flask(__name__)
post = Post()

@app.route('/')
def home():
    return render_template("index.html", posts=post.get_all_blog_post(), page_name="Home")

@app.route('/post/<blog_num>')
def blog(blog_num):
    return render_template("post.html", blog=post.get_specific_post(blog_num), page_name="Blog")

@app.route('/contact')
def contact():
    return render_template("contact.html", page_name="Contact Me")

@app.route('/about')
def about():
    return render_template("about.html", page_name="About Me")

@app.route('/submit', methods=["POST"])
def send_message():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]
    post.send_message(user_name=name, user_email=email, user_number=phone, user_message=message)
    return "<h1>Message sent successfully</h2>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=5000)
