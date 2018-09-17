from flask import render_template, redirect, url_for, abort, request
from flask_login import login_required, current_user

from . import MAIN
from .. import DB, PHOTOS

from .forms import UpdateProfile, BlogForm, CommentForm
from ..models import User, Blog, Comment


@MAIN.route('/')
def index():

    '''
    View root function that returns the index page
    '''

    title = 'Personal-Blog - Homepage'

    return render_template('index.html', title=title)


@MAIN.route('/user/<uname>')
def profile(uname):

    '''
    Function that returns the user's profile page
    '''

    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user=user)


@MAIN.route('/user/<uname>/update', methods=['GET','POST'])
@login_required
def update_profile(uname):

    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        DB.session.add(user)
        DB.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@MAIN.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_picture(uname):

    user = User.query.filter_by(username=uname).first()

    if 'photo' in request.files:
        filename = PHOTOS.save(request.files['photo'])
        path = f'photo/{filename}'
        user.profile_pic_path = path

        DB.session.commit()

    return redirect(url_for('main.profile', uname=uname))


@MAIN.route('/blog/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_blog():

    '''
    Function to render a form and get data from that form
    '''

    return render_template('new_pitch.html')


@MAIN.route('/blogs')
def blogs():

    '''
    Function to display all the pitches added
    '''

    return render_template('pitches.html')


@MAIN.route('/blogs/comments/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):

    '''
    Function to render a form and get data from that form
    '''

    return render_template('new_comment.html')


@MAIN.route('/blogs/comments/<int:id>')
def comments(id):

    '''
    Function that displays all comments for a pitch
    '''

    return render_template('comments.html')


@MAIN.route('/delete/blog/<int:id>', methods=["GET", "POST"])
@login_required
def delete_blog(id):

    return redirect(url_for('.index'))


@MAIN.route('/delete/comment/<int:id>', methods=["GET", "POST"])
@login_required
def delete_comment(id):

    return redirect(url_for('.index'))