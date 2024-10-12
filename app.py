"""Blogly application."""

from flask import Flask, render_template, request, redirect
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'ihaveasecret'

with app.app_context():
    connect_db(app)
    db.create_all()

@app.route('/')
def list_users():
    """shows list of all users in db"""

    users = User.query.all()
    return render_template('list.html', users=users)


@app.route('/user_form')
def create_user():
    return render_template('user_form.html')


@app.route('/user_form', methods=["POST"])
def create_user_form():
    """create a user form"""

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"]

    user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(user)
    db.session.commit()

    return redirect(f"/{user.id}")


@app.route('/<int:user_id>')
def show_details(user_id):
    """shows details of user"""

    user = User.query.get_or_404(user_id)
    return render_template("details.html", user=user)


@app.route('/<int:user_id>/edit')
def edit_user(user_id):
    """edit a user"""

    user = User.query.get_or_404(user_id)
    return render_template('edit_user.html', user=user)

@app.route('/<int:user_id>/edit', methods=["POST"])
def edit_user_form(user_id):
    """edit a user form redirecting to user"""

    user = User.query.get_or_404(user_id)

    user.first_name = request.form["first_name"]
    user.last_name = request.form["last_name"]
    user.image_url = request.form["image_url"]

    db.session.add(user)
    db.session.commit()

    return redirect(f"/{user.id}")


@app.route('/<int:user_id>/delete', methods=["GET", "POST"])
def delete_user(user_id):
    """delete a user redirect"""

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)