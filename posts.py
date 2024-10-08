from firebase_admin import firestore

def get_posts(db):
    """
    Lấy danh sách bài viết từ Firestore.
    db: đối tượng Firestore đã được khởi tạo.
    """
    posts_ref = db.collection('posts')
    docs = posts_ref.stream()
    posts = []
    for doc in docs:
        post = doc.to_dict()
        post['id'] = doc.id  # Thêm ID bài viết
        posts.append(post)
    return posts

def add_post(db, title, content):
    """
    Thêm bài viết vào Firestore.
    db: đối tượng Firestore đã được khởi tạo.
    title: tiêu đề bài viết.
    content: nội dung bài viết.
    """
    posts_ref = db.collection('posts')
    posts_ref.add({
        'title': title,
        'content': content
    })
