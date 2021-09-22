from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizaholic")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # buttons
        false_button_image = PhotoImage(file="images/false.png")
        true_button_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_image, command=self.check_answer_true)
        self.true_button.grid(row=3, column=1)
        self.false_button = Button(image=false_button_image, command=self.check_answer_false)
        self.false_button.grid(row=3, column=2)
        # canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=2, column=1, columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Quiz question", font=FONT)
        self.score = Canvas(width=100, height=40, bg=THEME_COLOR, highlightthickness=0)
        self.counter = self.score.create_text(25, 10, text=f"Score: {self.quiz.score}", font=("Ariel", 10, "bold"),
                                              fill="white")
        self.score.grid(row=1, column=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.itemconfig(self.counter, text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score.itemconfig(self.counter, text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz\n{self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_answer_true(self):
        self.get_feedback(self.quiz.check_answer("true"))

    def check_answer_false(self):
        self.get_feedback(self.quiz.check_answer("false"))

    def get_feedback(self, answer: bool):
        if answer:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
