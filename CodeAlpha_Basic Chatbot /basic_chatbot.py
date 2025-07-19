from tkinter import *
from PIL import Image, ImageTk
import random

# Rule-based replies
def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there! 🌟"
    elif "how are you" in user_input:
        return "I'm floating through the stars! ✨"
    elif "bye" in user_input:
        return "Goodbye! See you among the stars! 🚀"
    else:
        return random.choice([
            "I'm just a basic bot! 🌌",
            "Say something like 'hello', 'how are you', or 'bye'.",
            "Still learning the ways of the galaxy! 🛸"
        ])

# GUI Setup
def launch_chatbot():
    def send_message():
        user_msg = entry_box.get()
        if user_msg.strip() == "":
            return
        chat_log.config(state=NORMAL)
        chat_log.insert(END, "You: " + user_msg + "\n", "user")
        bot_reply = get_bot_response(user_msg)
        chat_log.insert(END, "Bot: " + bot_reply + "\n\n", "bot")
        chat_log.config(state=DISABLED)
        chat_log.yview(END)
        entry_box.delete(0, END)

    root = Tk()
    root.title("Basic Chatbot")
    root.geometry("600x500")
    root.resizable(False, False)

    # Background image
    bg_image = Image.open("galaxy_background.jpg")
    bg_image = bg_image.resize((600, 500))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
#Bhaskae Raj
    frame = Frame(root, bg="#000000", bd=0)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=500, height=400)

    chat_log = Text(frame, bg="#000", fg="white", font=("Consolas", 12), wrap=WORD)
    chat_log.tag_configure("user", foreground="#00ffcc")
    chat_log.tag_configure("bot", foreground="#ffcc00")
    chat_log.insert(END, "🚀 Welcome to Basic Chatbot! Say something!\n\n", "bot")
    chat_log.config(state=DISABLED)
    chat_log.pack(padx=10, pady=10, fill=BOTH, expand=True)

    entry_box = Entry(root, font=("Consolas", 12), bg="#222", fg="white")
    entry_box.place(relx=0.5, y=460, anchor=CENTER, width=400)
    entry_box.bind("<Return>", lambda e: send_message())
#Bhaskar Raj
    send_btn = Button(root, text="Send", command=send_message, bg="#1e90ff", fg="white", font=("Arial", 10, "bold"))
    send_btn.place(x=500, y=455, width=70, height=30)

    root.mainloop()

# Launch app
launch_chatbot()
