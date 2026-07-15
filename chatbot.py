# chatbot.py

from responses import responses
from datetime import datetime


def get_response(user_input):

    # Convert user input to lowercase
    user_input = user_input.lower().strip()

    # Dynamic responses
    if user_input == "date":
        return datetime.now().strftime("Today's Date: %d-%m-%Y")

    elif user_input == "time":
        return datetime.now().strftime("Current Time: %I:%M:%S %p")

    # Static responses
    elif user_input in responses:
        return responses[user_input]

    # Unknown command
    else:
        return "Sorry, I don't understand that command. Type 'help' or check the sidebar."