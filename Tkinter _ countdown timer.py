import tkinter as tk
from time import strftime

# Create the main application window
tick = tk.Tk()
tick.title("Countdown Timer")
tick.geometry("300x150")
tick["background"] = "#FFFFFF" #white background

#function Counting down from a specified number of seconds
def countdown(count):

    # Update the label text with the current count and current date
    label.config(text=f"Time left: {count} seconds" + "\n\n" + "Current time: " + "\n" + strftime("%b.%d.%Y") + " " + strftime("%H:%M:%S %p"))

    if count > 0:
        # Schedule the countdown function to be called again after 1000ms (1 second)
        # The next count value (count - 1) is passed as an argument
        tick.after(1000, countdown, count - 1)
    else:
        # Display a message when the countdown is finished
        label.config(text="Time's up!" +"\n\n" + "Stopped at: " + strftime("%H:%M:%S %p"))


# Create a label to display the timer
label = tk.Label(tick, text="", font=("Arial", 16), background="#FFFFFF",foreground="blue")
label.pack(pady=20)

user_input = input("Please enter a time (in seconds) to count down: ")
if user_input.isdigit():
    user_input_int = int(user_input)
    countdown(user_input_int)
else:
    print("Invalid input! Please enter a whole number.")


# Run the application loop
tick.mainloop()




