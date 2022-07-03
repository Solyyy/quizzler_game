from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain, total_questions):
        self.total_question_amount = total_questions
        self.quiz = quiz_brain
        self.root = Tk()
        self.root.title("Quizzlet")
        self.root.config(padx=20, pady=20, bg=THEME_COLOR)
        # Labels
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.question_label = Label(text="Question 1/10", fg="white", bg=THEME_COLOR)
        self.question_label.grid(column=0, row=0)
        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Testing", fill=THEME_COLOR, font=FONT, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # Buttons
        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, bg=THEME_COLOR, highlightthickness=0, command=self.true_press)
        self.true_button.grid(column=0, row=2, pady=40)
        # Images
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, bg=THEME_COLOR, highlightthickness=0, command=self.false_press)
        self.false_button.grid(column=1, row=2, pady=40)
        self.get_next_question()
        self.root.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.question_label.config(text=f"Questions: {self.quiz.current_question_number} / {self.total_question_amount}")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.buttons_state(ACTIVE)
        else:
            self.buttons_state(DISABLED)
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.question_label.config(
                text=f"Questions: {self.quiz.current_question_number - 1} / {self.total_question_amount}")

    def true_press(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_press(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.root.after(1000, self.get_next_question)

    def buttons_state(self, state: str):
        self.true_button.config(state=state)
        self.false_button.config(state=state)
