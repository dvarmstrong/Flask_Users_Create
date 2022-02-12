from flask_app import app   
from flask import render_template, request, redirect
from flask_app.models.user import User


@app.route('/')
def create():
    # call the get_all classmethod to get all users
    users = User.get_all()
    print(users)
    return render_template('read.html', all_users = users)

@app.route('/add_user')
def add_user():
    return render_template('create.html')



@app.route('/create_user', methods=['POST'])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }

    User.save(data)

    return redirect('/')


@app.route('/users/<int:num>')
def show_user(num):
    data ={
        "id" : num
    }

    this_user =User.get_one(data)
    return render_template('readOne.html', user = this_user)


@app.route('/edit_user/<int:num>')
def edit_user(num):
    data ={
        "id" : num
    }
    this_user =User.get_one(data)
    return render_template('user_edit.html', user = this_user)

@app.route('/update_user')
def update_user():
    data ={
        "id" : request.form['id'],
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }

    id = User.update(data)
    return redirect(f'/users/{id}')