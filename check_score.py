import tkinter as tk
import requests
import socket

def submit_flag():
    challenge_name = ""  # Replace with your actual challenge name
    flag = entry.get()
    ip = socket.gethostbyname(socket.gethostname())

    # Define your API endpoint
    url = 'http://127.0.0.1:8000/check'  # Replace with your actual API URL

    # Define the parameters to send with the request
    params = {
        "challenge": challenge_name,
        "flag": flag,
        "ip": str(ip)
    }

    # Send a GET request to the API
    response = requests.get(url, params=params)
    result = response.json()
    print(result.get("points"))
    if result.get("points") == 0:
        result = "Incorrect flag"
    elif result.get("points") == -1:
        result = "Flag already submitted"
    else:
        points = result.get("points")
        team = result.get("team_name")
        result = f"Flag accepted! You earned {points} points. Team: {team}"
    
    result_label.config(text=result, fg="red" if result == "Incorrect flag" or result == "Flag already submitted" else "green")

# Create the main application window
root = tk.Tk()
root.title("Flag Submission")
root.geometry("400x200")

# Create a label for instructions
label = tk.Label(root, text="Enter the flag:")
label.pack(pady=10)

# Create an entry widget for the flag input
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Create a submit button that triggers the submit_flag function
submit_button = tk.Button(root, text="Submit", command=submit_flag)
submit_button.pack(pady=10)

# Create a label to display the result of the API call
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the main loop
root.mainloop()


# # Define the API endpoint URL
# 

# # Make a GET request to the API endpoint using requests.get()
# response = requests.get(url)
# print(response.text)