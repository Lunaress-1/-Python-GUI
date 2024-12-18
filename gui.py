import tkinter as tk

from tkinter import messagebox

import pyttsx3



def play_text():

    """Reads the text from the entry field and converts it to speech."""

    text = entry.get()

    if text.strip():

        engine.say(text)

        engine.runAndWait()

    else:

        messagebox.showwarning("Warning", "Please enter some text!")



def clear_text():

    """Clears the text from the entry field."""

    entry.delete(0, tk.END)



def exit_program():

    """Closes the program."""

    root.destroy()



# Initialize the Text-to-Speech engine

engine = pyttsx3.init()



# Create the main GUI window

root = tk.Tk()

root.config(bg="SkyBlue")

root.title("Text to Speech")

##! root.iconbitmap("اضف مسار الايقون ") ده لو عايزتغير الايقون 



# Create a label

label = tk.Label(root, text="Enter your text 👇🏻", font=("Arial", 20),bg="Navy",fg="white")

label.grid(row=0, column=0, columnspan=3, pady=10)



# Create an entry field

entry = tk.Entry(root, width=40, font=("Arial", 12),justify="center")

entry.grid(row=1, column=0, columnspan=3, pady=10)



# Create buttons

play_button = tk.Button(root, text="Play", font=("Arial", 12), command=play_text,bg="lightgreen",fg="black")

play_button.grid(row=2, column=0, padx=10, pady=5)



exit_button = tk.Button(root, text="Exit", font=("Arial", 12),  fg="black",bg="light coral", command=exit_program)

exit_button.grid(row=2, column=1, padx=10, pady=5)



set_button = tk.Button(root, text="Set", font=("Arial", 12), command=clear_text,bg="tan",fg="black")

set_button.grid(row=2, column=2, padx=10, pady=5)



# Run the Tkinter event loop

root.mainloop()


