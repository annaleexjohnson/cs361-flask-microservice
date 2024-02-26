The primary microservice is stored in the app.py file.

For the sake of testing, this respository has an index.html file in the templates folder, as well as a sample data dictionary which is imported into the app.py file. These can be changed to suit the project's needs.

The microservice works by pulling a user's username and unique identifier from a frontend form using Flask's built-in request object. It then iterates through the data dictionary until it finds a match with the username and unique identifier. Finally, it returns the correct password to the frontend, or an error message if the password wasn't found. 
