from flask import Blueprint
from flask import render_template
from models import Post, Tag
from flask import request
from .forms import PostForm
from app import db
from flask import redirect
from flask import url_for

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/create', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except Exception as e:
            print(f'ERROR! {e}')
        return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/')
def index():
    q = request.args.get('q')
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    if q:
        posts = Post.query.filter(Post.title.contains(q)|Post.body.contains(q)) #.all()
    else:
        posts = Post.query.order_by(Post.created.desc())

    pages = posts.paginate(page=page, per_page=3)

    return render_template('posts/index.html', posts=posts, pages=pages)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag=tag, posts=posts)