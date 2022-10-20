from tkinter import *
from quiz_brain import QuizBrain

FONT = ('Arial', 20, 'italic')
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        #Canvas
        self.create_canvas()
        self.create_button()
        self.create_label()

        self.get_next_question()
        self.window.mainloop()

    def create_canvas(self):
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.config(bg='white')
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)


    def create_button(self):
        self.right_image = PhotoImage(file='images/true.png')
        self.right_button = Button(image=self.right_image, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(row=2, column=0)

        self.false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

    def create_label(self):
        self.score = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.question_text = self.canvas.create_text(150, 125, width=200, text='text', fill=THEME_COLOR, font=FONT)

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score.config(text=f'Score {self.quiz.score}')
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.right_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feddback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feddback(is_right)

    def give_feddback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)