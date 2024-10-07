# Đây là file chính của flask để khởi dộng app

from flask import Flask, render_template, request, redirect, url_for
from posts import get_posts, add_post

#Bắt Đầu
app = Flask(__name__)

@app.route('/')
def index():
    posts = get_posts()
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    content = request.form['content']
    add_post(title, content)
    return redirect(url_for('index'))
    
# Kết thúc
if __name__ == '__main__':
    app.run(debug=True)
