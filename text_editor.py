import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Text Editor")
        self.master.geometry("600x400")

        self.text_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=60, height=20)
        self.text_area.pack(pady=10, expand=True, fill=tk.BOTH)

        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(1.0, file.read())
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {e}")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    text_content = self.text_area.get(1.0, tk.END)
                    file.write(text_content)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    text_content = self.text_area.get(1.0, tk.END)
                    file.write(text_content)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

    def exit_app(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
