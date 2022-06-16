from tkinter import Button, Label, Entry


def clear_window(tk):
    for widget in tk.winfo_children():
        widget.destroy()


def render_main_screen(tk):
    Button(tk, text="Login", bg="green", fg="black"
           ).grid(row=0, column=0)
    Button(tk, text="Register", bg="yellow", fg="black",
           command=lambda: render_register_screen(tk)
           ).grid(row=0, column=1)


def render_register_screen(tk):
    clear_window(tk)

    Label(tk, text="Email").grid(row=0, column=0)
    email_entry = Entry(tk)
    email_entry.grid(row=0, column=1)

    Label(tk, text="Password",).grid(row=1, column=0)
    password_entry = Entry(tk, show="*")
    password_entry.grid(row=1, column=1)

    Label(tk, text="Confirm Password").grid(row=2, column=0)
    confirm_password_entry = Entry(tk, show="*")
    confirm_password_entry.grid(row=2, column=1)

    def on_register():
        email = email_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        print(email, password, confirm_password)

    Button(tk, text="Register", bg="green", fg="black",
           command=lambda: on_register()
           ).grid(row=3, column=0)














