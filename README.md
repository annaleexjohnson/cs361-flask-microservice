To start, type flask run in the command line. The primary microservice is stored in the app.py file.

For the sake of testing, this respository has an index.html file in the templates folder, as well as a sample data dictionary which is imported into the app.py file. These can be changed to suit the project's needs, as long as the data structure is iterable. 

To request data, the frontend should send a POST request after a user enters their username and unique identifier. In this example, the POST request is sent to the "/forgot-password" endpoint, which can be changed depending on the project. Once the microservice recieves the post request, it pulls the user's username and unique identifier from the frontend form using Flask's built-in request object. It will iterate through the data dictionary until it finds a match with the username and unique identifier. 

To recieve data, it sets the user_pass variable to the correct password, or returns an error message. In this example, the microservice renders the index.html file along with the correct password/error message. However, the user_pass variable may also be passed to the frontend in the POST's return body, and then used in another microservice (for example, it could be passed to another microservice that emails the user their password). 

UML Diagram:

<img width="821" alt="Screenshot 2024-02-26 at 11 35 55 PM" src="https://github.com/annaleexjohnson/cs361-flask-microservice/assets/87035551/ade0c438-a316-4b03-a407-caa42dc6e6fe">
