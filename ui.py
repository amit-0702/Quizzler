from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg='white', font=('Arial', 10, "normal"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question Text",
            fill=THEME_COLOR,
            font=('Arial', 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true = PhotoImage(file='./images/true.png')
        self.right_button = Button(image=true, highlightthickness=0, command=self.right_button_clicked)
        self.right_button.grid(column=0, row=2)

        false = PhotoImage(file='./images/false.png')
        self.wrong_button = Button(image=false, highlightthickness=0, command=self.wrong_button_clicked)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the game")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_button_clicked(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def wrong_button_clicked(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
