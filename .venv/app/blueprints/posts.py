from flask import Blueprint, request, render_template, redirect, url_for
from app.models.post import Post as PostModel

bp = Blueprint("post",__name__)


@bp.route("/post/",methods=["GET", "POST"])
def posts():
    if request.method=="POST":
        # return "<h2>Store Blog</h2>"
        # return request.form
        return redirect(url_for('post.posts'))

    else :
        posts= PostModel.query.all()
        return render_template('blog/index.html', posts=posts)


@bp.route("/post/create/")
def create():
    return render_template("blog/create-post.html")


@bp.route("/post/<int:post_id>/", methods=["GET","PUT", "DELETE"])
def posts_id(post_id):
    if request.method=="PUT":
        return "<h2>Update Blog</h2>"
    elif request.method=="DELETE":
        return "<h2>Delete Blog</h2>"
    else:
        return render_template('blog/show-post.html', id=post_id)