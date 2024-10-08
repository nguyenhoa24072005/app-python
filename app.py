import os
from flask import Flask, render_template, request, redirect, url_for
from posts import get_posts, add_post
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

# Load biến môi trường từ .env
load_dotenv()

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Kết nối Firebase bằng thông tin từ biến môi trường
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": os.getenv('FIREBASE_PROJECT_ID'),
    "private_key_id": os.getenv('FIREBASE_PRIVATE_KEY_ID'),
    "private_key": os.getenv('FIREBASE_PRIVATE_KEY').replace('\\n', '\n'),
    "client_email": os.getenv('FIREBASE_CLIENT_EMAIL'),
    "client_id": os.getenv('FIREBASE_CLIENT_ID'),
    "auth_uri": os.getenv('FIREBASE_AUTH_URI'),
    "token_uri": os.getenv('FIREBASE_TOKEN_URI'),
    "auth_provider_x509_cert_url": os.getenv('FIREBASE_AUTH_PROVIDER_CERT_URL'),
    "client_x509_cert_url": os.getenv('FIREBASE_CLIENT_CERT_URL')
})
firebase_admin.initialize_app(cred)

# Kết nối tới Firestore
db = firestore.client()

# Các route Flask
@app.route('/')
def index():
    posts = get_posts(db)  # Truyền đối tượng db vào hàm get_posts
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    content = request.form['content']
    add_post(db, title, content)  # Truyền đối tượng db vào hàm add_post
    return redirect(url_for('index'))

# Chạy ứng dụng Flask
if __name__ == '__main__':
    app.run(debug=True)
