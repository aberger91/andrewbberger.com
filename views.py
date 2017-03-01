from flask import (render_template,
                   flash,
                   request,
                   url_for,
                   redirect,
                   session
                   )
from MySQLdb import escape_string as thwart
from passlib.hash import sha256_crypt
from functools import wraps
import random
import gc
from .util.dbconnect import (db_connection, 
                             db_execute, 
                             db_log
                             )
from .util.config import *
from .util.models import *
from andrewbberger import app

app.config['TEMPLATES_AUTO_RELOAD'] = True


def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session.get('username') != 'admin':
            return render_template('404.html')
        else:
            return f(*args, **kwargs)
    return wrap

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first!')
            return redirect(url_for('login'))
    return wrap

@app.route('/logout/', methods=['GET'])
@login_required
def logout():
    session.clear()
    flash('You have been logged out!')
    gc.collect()
    return redirect(url_for('home'))

@app.route('/')
@enable_logging('home')
def home():
    return redirect(url_for('subject_home', subject='home'))

@app.route('/<subject>', methods=['GET'])
def subject_home(subject):
    blog_posts = get_all_blog_posts(BLOG_POSTS)  # returns dict
    subject_posts = blog_posts.get(subject)
    picture = random.choice(PICTURES)
    log(subject)
    if subject_posts:
        subject_posts[-1]._title = subject_posts[-1].title.replace(' ', '_').lower()
        featured_post = subject_posts[-1]
    else:
        featured_post = None
    return render_template('home.html', subject_posts=subject_posts, featured_post=featured_post,
                           header_title=subject, subject=subject, picture=picture)

@app.route('/blog/<_type>/<path>/<action>', methods=['GET', 'POST'])
@app.route('/blog/<_type>/<path>/', methods=['GET', 'POST'])
def blog_post(_type, path, action='', comments=''):
    '''
    '''
    return blog_post_handler(_type, path, action=action, comments=comments)
    
@app.route('/blog-publisher/', methods=['GET', 'POST'])
@admin_required
def blog_publisher():
    blog_posts = get_all_blog_posts(BLOG_POSTS)
    if request.method == 'POST':
        if session.get('username') == 'admin':
            return blog_publisher_handler(blog_posts)
    return render_template('blog_publisher.html')

@app.route('/register/', methods=["GET","POST"])
def register():
    register_user()
        
@app.route('/login/', methods=['GET', 'POST'])
def login():
    login_user()

@app.route('/resume/', methods=['GET', 'POST'])
def resume():
    return redirect(url_for('blog_post', _type='about', path='resume'))

@app.errorhandler(404)
def page_not_found(e):
    flash(e)
    return render_template('404.html', header_title="Page not Found!")
