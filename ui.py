from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="QUESTIONS APPEAR HERE",
                                                     font=FONT,
                                                     width=280,
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, sticky="EW", pady=50)

        self.score = Label(text="Score: 0", font=FONT, bg=THEME_COLOR, fg="white")
        self.score.config(pady=5)
        self.score.grid(row=0, column=1, sticky="EW")

        self.right_img = PhotoImage(file="images/true.png")
        self.true = Button(image=self.right_img, highlightthickness=0, command=self.is_right)
        self.true.grid(row=2, column=0)

        self.false_img = PhotoImage(file="images/false.png")
        self.false = Button(image=self.false_img, highlightthickness=0, command=self.is_wrong)
        self.false.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of this quiz 😇", fill=THEME_COLOR)
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def is_right(self):
        right = self.quiz.check_answer("True")
        self.feedback(right)


    def is_wrong(self):
        wrong = self.quiz.check_answer("False")
        self.feedback(wrong)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")

        self.window.after(1000, self.get_next_question)
