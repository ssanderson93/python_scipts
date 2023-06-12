import tkinter as tk
import tkinter.simpledialog as sd
import secrets
import string



#global vars
letter_chars = string.ascii_letters
digit_chars = string.digits
special_chars = string.punctuation
alphabet = letter_chars + digit_chars + special_chars

#tool functions
def pwd_gen():
    # input is a local variable (needs validation)
    pwd_length = sd.askinteger("Input", "Enter the password length:")

    # local vars
    pwd = ''
    complexity_met = False
    
    while not complexity_met:
        # character iteration
        pwd = ''.join(secrets.choice(alphabet) for _ in range(pwd_length))

        # complexity requirements check
        if any(char in special_chars for char in pwd) and sum(char in digit_chars for char in pwd) >= 2:
            complexity_met = True

    output_window.insert(tk.END, "Password: \n" + str(pwd))

#GUI button functions, could simplify

def function2():
    password_length()

def function3():
    output_window.insert(tk.END, "End of function!\n")

def function4():
    output_window.insert(tk.END, "End of function!\n")

# Create the main window
window = tk.Tk()
window.title("Tools for tools")

# define buttons
button1 = tk.Button(window, text="Password Generator", command=pwd_gen)
button1.pack()

button2 = tk.Button(window, text="Function 2", command=function2)
button2.pack()

button3 = tk.Button(window, text="Function 3", command=function3)
button3.pack()

button4 = tk.Button(window, text="Function 4", command=function4)
button4.pack()

# Create the output window
output_window = tk.Text(window, height=10, width=40)
output_window.pack()

# Run the main loop
window.mainloop()
