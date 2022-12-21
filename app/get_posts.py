from app import db
from models import Post, Tag

posts = Post.query.all()
print(posts)
p2 = Post.query.filter(Post.title.contains('first')).all()
print(p2)
p3 = Post.query.filter(Post.title=='First post5').first().tags
print(p3)
t = Tag.query.first().posts.first()
print(t)

