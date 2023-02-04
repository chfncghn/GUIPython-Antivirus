import hashlib
import os
import sys
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

class AntivirusGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MESET Antivirus")
        self.geometry("800x400")

        self.scan_result = tk.StringVar()
        self.scan_result.set("MESET Antivirus- No file selected for scanning.")

        self.label = tk.Label(textvariable=self.scan_result)
        self.label.pack(pady=10)

        self.file_button = tk.Button(text="Select a file", command=self.select_file)
        self.file_button.pack()

        self.scan_button = tk.Button(text="Scan the file", command=self.scan)
        self.scan_button.pack(pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename()
        self.file_path = file_path
        self.scan_result.set(f"Selected file: {file_path}")

    def scan(self):
        with open(self.file_path, 'rb') as f:
            file_contents = f.read()
            sha256_hash = hashlib.sha256(file_contents).hexdigest()
 
            known_threats = self.load_hashes() 
 
        if sha256_hash in known_threats:
            self.scan_result.set(f"Threat detected: {self.file_path}")
            messagebox.showwarning("MESET Antivirus- Virus detected!", "This file has been identified as a threat it is recommend to delete this file")
            answer = messagebox.askyesno("MESET Antivirus- Threat detected", "This file has been identified as a known threat. Do you want to delete it?")
            if answer:
                os.remove(self.file_path)
                self.scan_result.set(f"File deleted: {self.file_path}")
                messagebox.showinfo("MESET Antivirus- File deleted", "The file has been successfully deleted.")
            else:
                self.scan_result.set(f"File not deleted: {self.file_path}")
                messagebox.showinfo("MESET Antivirus- File not deleted", "The file has not been deleted.")
        else:
            self.scan_result.set(f"File is safe: {self.file_path}")
            messagebox.showinfo("MESET Antivirus- Safe file", "This file has been identified as safe.")

    def load_hashes(self):
        hashes = []
        with open("hashes.txt", "r") as f:
            for line in f:
                hashes.append(line.strip())
        return hashes

if __name__ == '__main__':
    app = AntivirusGUI()
    app.mainloop()
