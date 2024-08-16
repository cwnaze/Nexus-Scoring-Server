import tkinter as tk
import requests

def submit_flag():
    challenge_name = "test challenge"  # Replace with your actual challenge name
    flag = entry.get()

    # Define your API endpoint
    url = 'http://127.0.0.1:8000/check'  # Replace with your actual API URL

    # Define the parameters to send with the request
    params = {
        "challenge": challenge_name,
        "flag": flag
    }

    # Send a GET request to the API
    response = requests.get(url, params=params)
    result = response.text
    if result == "0":
        result = "Incorrect flag"
    else:
        result = f"Flag accepted! You earned {result} points."
    
    result_label.config(text=result, fg="red" if result == "Incorrect flag" else "green")

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