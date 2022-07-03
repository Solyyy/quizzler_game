import requests
import tkinter as tk
from tkinter import ttk, IntVar, Radiobutton

THEME_COLOR = "#375362"


class QuizSetup:

    def __init__(self):
        self.amount = 0
        self.category = 0
        self.parameters = {
            "amount": self.amount,
            "type": "boolean",
            "category": self.category
        }
        self.root = tk.Tk()
        self.root.title("Configure your Quiz")
        self.root.config(padx=50, pady=50, bg=THEME_COLOR)
        self.question_category = None

        # UI setup for Amount of Questions
        self.num_of_q_label = tk.Label(text="Number of questions:", fg="white", bg=THEME_COLOR)
        self.num_of_q_label.pack(pady=10)

        self.radio_state = IntVar()
        self.radiobutton1 = Radiobutton(text="10", value=10, variable=self.radio_state,
                                        command=self.change_question_amount, activebackground=THEME_COLOR)
        self.radiobutton2 = Radiobutton(text="25", value=25, variable=self.radio_state,
                                        command=self.change_question_amount, activebackground=THEME_COLOR)
        self.radiobutton3 = Radiobutton(text="50", value=50, variable=self.radio_state,
                                        command=self.change_question_amount, activebackground=THEME_COLOR)
        self.radiobutton1.config(bg=THEME_COLOR)
        self.radiobutton2.config(bg=THEME_COLOR)
        self.radiobutton3.config(bg=THEME_COLOR)

        self.radiobutton1.pack()
        self.radiobutton2.pack()
        self.radiobutton3.pack()

        # UI setup for categories
        self.categories_label = tk.Label(text="Categories:", fg="white", bg=THEME_COLOR)
        self.categories_label.pack(pady=10)
        # Dropbox
        self.option_var = tk.StringVar(self.root)
        self.options = ttk.OptionMenu(self.root, self.option_var, "Select your category here", "General Knowledge",
                                      "Entertainment: Film", "Entertainment: Japanese Anime & Manga",
                                      "Entertainment: Cartoon & Animations", "Entertainment: Video Games", "Science & Computers",
                                      command=self.change_question_category)
        self.options.pack()
        self.root.mainloop()

    def change_question_amount(self):
        amount_of_questions = self.radio_state.get()
        self.parameters["amount"] = int(amount_of_questions)

    def change_question_category(self, arg):
        categories = {
            "General Knowledge": 9,
            "Entertainment: Film": 11,
            "Entertainment: Japanese Anime & Manga": 31,
            "Entertainment: Cartoon & Animations": 32,
            "Entertainment: Video Games": 15,
            "Science & Computers": 18
        }
        self.question_category = self.option_var.get()
        self.parameters["category"] = categories[arg]
        self.set_up_params()
        self.root.destroy()

    def set_up_params(self):
        self.response = requests.get("https://opentdb.com/api.php", params=self.parameters)
        self.response.raise_for_status()
        self.data = self.response.json()
        self.question_data = self.data["results"]

    def get_question_amount(self):
        return self.parameters["amount"]
