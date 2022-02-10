from flask import Flask, render_template, request, redirect
from user import User


app = Flask(__name__)

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



if __name__=='__main__':
    app.run(debug=True)