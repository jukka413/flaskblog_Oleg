from app import db
from models import Post, Tag

def create_post():
    db.create_all()
    p = Post(title='First post5', body='some words')
    db.session.add(p)
    db.session.commit()
    print(p)


def create_tag():
    db.create_all()
    t = Tag(name='python')
    db.session.add(t)
    db.session.commit()
    print(t)


def create_posttag():
    post = Post.query.filter(Post.title == 'First post5').first()
    tag = Tag.query.first()
    post.tags.append(tag)
    print(post, tag)
    db.session.add(post)
    db.session.commit()


create_posttag()
