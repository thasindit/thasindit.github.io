import cgi
import cgitb
# Store a list of valid usernames and passwords
valid_credentials = {
    "user@gmail.com": "password",
    "user2": "password2",
    "user3": "password3"
}

# Get the user's credentials from the form submission
form = cgi.FieldStorage()
username = form.getvalue("email")
password = form.getvalue("password")

# Check if the entered credentials are valid
if (username in valid_credentials) and (valid_credentials[username] == password):
    print("Login successful!")
else:
    print("Invalid username or password")
