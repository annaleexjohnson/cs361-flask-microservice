from flask import Flask, render_template, request, redirect
app = Flask(__name__)

from password_dictionary import login_info

# render index.html
@app.route("/")
def index():
    return render_template('index.html', password="")

# get user password
@app.route("/forgot-password", methods= ["POST"])
def get_pass():
    username = request.form["username"]
    unique_id = request.form["unique_id"]
    print(username, unique_id, type(unique_id))

    for user in login_info:
        if user["unique_id"] == unique_id and user["username"] == username:
            user_pass = user['password']
            return render_template('index.html', password=f'Your password is: "{user_pass}"') # return password
        
    return render_template('index.html', password="We couldn't find your password. Try again.")    # handles error

if __name__ == '__main__':
    app.run(debug=True)