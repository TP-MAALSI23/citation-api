from flask import Flask
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# Check the value of APP_ENV to enable or disable debugging
if os.getenv('APP_ENV') == 'dev':
    app.debug = True

# Get the port number from the APP_PORT environment variable or use 5000 as a default
port = int(os.getenv('APP_PORT', 3000))

# Define your API routes and functions here
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Add more routes and functions as needed

if __name__ == '__main__':
    # Run the application on the specified port
    app.run(host='0.0.0.0', port=port)
