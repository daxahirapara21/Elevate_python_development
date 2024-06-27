
import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz App")
        self.score = 0
        self.current_question = 0

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A. Paris", "B. Rome", "C. London", "D. Madrid"],
                "answer": "A"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A. Jupiter", "B. Mars", "C. Saturn", "D. Venus"],
                "answer": "B"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
                "answer": "D"
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["A. Vincent van Gogh", "B. Leonardo da Vinci", "C. Pablo Picasso", "D. Michelangelo"],
                "answer": "B"
            },
            {
                "question": "Which country won the FIFA World Cup in 2018?",
                "options": ["A. Brazil", "B. Germany", "C. France", "D. Argentina"],
                "answer": "C"
            }
        ]

        self.label_question = tk.Label(master, text="", wraplength=400, justify="center")
        self.label_question.pack(pady=20)

        self.radio_var = tk.StringVar()
        self.radio_var.set(None)

        self.radio_buttons = []
        for i in range(4):
            radio = tk.Radiobutton(master, text="", variable=self.radio_var, value=str(i+1))
            self.radio_buttons.append(radio)
            radio.pack()

        self.button_submit = tk.Button(master, text="Submit", command=self.submit_answer)
        self.button_submit.pack(pady=20)

        self.label_score = tk.Label(master, text="")
        self.label_score.pack()

        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.label_question.config(text=question["question"])
            for i, option in enumerate(question["options"]):
                self.radio_buttons[i].config(text=option)
        else:
            self.show_result()

    def submit_answer(self):
        if self.radio_var.get() is None:
            messagebox.showwarning("Warning", "Please select an answer!")
            return

        user_answer_index = int(self.radio_var.get()) - 1
        correct_answer = self.questions[self.current_question]["answer"]

        if self.questions[self.current_question]["options"][user_answer_index][0] == correct_answer:
            self.score += 1

        self.current_question += 1
        self.radio_var.set(None)
        self.load_question()

    def show_result(self):
        self.label_question.config(text="")
        for radio in self.radio_buttons:
            radio.pack_forget()
        self.button_submit.pack_forget()
        self.label_score.config(text=f"Quiz complete! You scored {self.score} out of {len(self.questions)}.")
        self.label_score.pack(pady=20)

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
