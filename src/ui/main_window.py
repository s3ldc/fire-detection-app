# main_window.py
import tkinter as tk
from tkinter import ttk

def launch_main_window(start_callback):
    window = tk.Tk()
    window.title("Fire Detection System")
    window.geometry("500x400")
    window.configure(bg="#1e1e1e")  # Dark background

    # Title
    title = tk.Label(
        window,
        text="Fire Detection System",
        font=("Segoe UI", 22, "bold"),
        fg="white",
        bg="#1e1e1e"
    )
    title.pack(pady=40)

    # Subtitle
    subtitle = tk.Label(
        window,
        text="Real-time fire detection using YOLO",
        font=("Segoe UI", 12),
        fg="#bbbbbb",
        bg="#1e1e1e"
    )
    subtitle.pack(pady=10)

    # Start Button (styled)
    style = ttk.Style()
    style.configure(
        "TButton",
        font=("Segoe UI", 14, "bold"),
        padding=10
    )

    start_btn = ttk.Button(
        window,
        text="Start Detection",
        command=start_callback,
        style="TButton"
    )
    start_btn.pack(pady=40)

    window.mainloop()
