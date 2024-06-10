from flask import Blueprint, request, render_template, redirect, url_for
from app.models.post import Post as PostModel
from app.extensions import db

bp = Blueprint("post",__name__)


@bp.route("/post/")
def index():
    posts= PostModel.query.all()
    return render_template('blog/index.html', posts=posts)


@bp.route("/post/",methods=["POST"])
def store():
    newPost = PostModel(
         title = request.form["title"],
         category = request.form["category"],
         content = request.form["content"],
    )
    db.session.add(newPost)
    db.session.commit()
    return redirect(url_for('post.index'))


@bp.route("/post/<int:post_id>/", methods=["DELETE"])
def delete(post_id):
    if request.method=="DELETE":
        post= PostModel.query.get(post_id)
        db.session.delete(post)
        db.session.commit()
        return "Delete"


@bp.route("/post/edit/<int:post_id>/", methods=["PUT"])
def update(post_id):
    return  "Update logic will be here"
     

@bp.route("/post/edit/<int:post_id>/")
def edit(post_id):
    post= PostModel.query.get(post_id)
    return render_template('blog/edit-post.html', post=post)
     

@bp.route("/post/create/")
def create():
    return render_template("blog/create-post.html")


@bp.route("/post/<int:post_id>/")
def single(post_id):
        post= PostModel.query.get(post_id)
        return render_template('blog/show-post.html', post=post)
    