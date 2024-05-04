import tkinter as tk
from tkinter import filedialog, messagebox
import requests

class InkPad:
    def __init__(self, root):
        self.root = root
        self.root.title('InkPad')
        self.root.geometry('600x400')
        self.create_widgets()

    def create_widgets(self):
        headline = tk.Label(self.root, text='InkPad', font=('Helvetica', 24))
        headline.pack()

        self.text_area = tk.Text(self.root, undo=True)
        self.text_area.pack(expand=True, fill='both')

        button_frame = tk.Frame(self.root)
        button_frame.pack()

        import_button = tk.Button(button_frame, text='Import File', bg='blue', fg='white', command=self.import_file)
        import_button.pack(side=tk.LEFT)

        save_button = tk.Button(button_frame, text='Save File', bg='light blue', fg='white', command=self.save_file)
        save_button.pack(side=tk.LEFT)

    def import_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt')
        if file_path:
            with open(file_path, 'w') as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)

    def download_file(self):
        url = filedialog.askstring('Download File', 'Enter the URL of the file:')
        if url:
            try:
                response = requests.get(url)
                response.raise_for_status()  # Check for request errors
                file_path = filedialog.asksaveasfilename(defaultextension='.txt')
                if file_path:
                    with open(file_path, 'wb') as file:
                        file.write(response.content)
                    messagebox.showinfo('Success', 'File downloaded successfully!')
            except requests.exceptions.RequestException as e:
                messagebox.showerror('Error', f'Failed to download file: {e}')

root = tk.Tk()
app = InkPad(root)
root.mainloop()