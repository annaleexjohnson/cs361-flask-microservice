from flask import Flask, render_template, request, redirect
app = Flask(__name__)

from password_dictionary import login_info      #pull username/password data from dictionary file

# render index.html file for testing purposes
@app.route("/")
def index():
    return render_template('index.html', password="")

# get user password after recieving POST request
@app.route("/forgot-password", methods= ["POST"])
def get_pass():
    username = request.form["username"]         # gets username from frontend form
    unique_id = request.form["unique_id"]       # gets unique ID from frontend form

    # iterates through password dictionary 
    for user in login_info:
        # compares username/unique id with each object in dictionary
        if user["unique_id"] == unique_id and user["username"] == username:
            user_pass = user['password']
            # if there's match, render index.html with the correcy password
            return render_template('index.html', password=f'Your password is: "{user_pass}"')
        
    # renders index.html with error message if password wasn't found.
    return render_template('index.html', password="We couldn't find your password. Try again.")



if __name__ == '__main__':
    app.run(debug=True)