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
        self.title("Antivirus")
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

        if sha256_hash in KNOWN_THREATS:
            self.scan_result.set(f"Threat detected: {self.file_path}")
            messagebox.showwarning("MESET Antivirus- Threat detected", "This file has been identified as a known threat.")
        else:
            self.scan_result.set(f"File is safe: {self.file_path}")
            messagebox.showinfo("MESET Antivirus- Safe file", "This file has been identified as safe.")


if __name__ == '__main__':
    # List of known threat hashes
    KNOWN_THREATS = [
        "11b48eb87a0f7c12085b14d2a8f23c5b0a9e9dbb3476d0b59dd5c18aad30e1c3",
        "e029c467d77a5dacff64a8a4b6af5a2aa33199eb8cf35c79f5563345fe3c307f",
        "5f2a3e3c3e5b80f70a18a7a93bce06dfd2b2a1a8820acb17e9f33e7afb63eb12",
        "24f33c4f7b11a6558e6c0a6ccdc062c28f0d8b2c3e0e3dd6c0b16276785a7a24",
    ]

    app = AntivirusGUI()
    app.mainloop()
