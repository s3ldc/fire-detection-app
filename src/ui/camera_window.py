# camera_window.py
import tkinter as tk
from tkinter import Label
import cv2
from PIL import Image, ImageTk

from detection.fire_detector import detect_fire_on_frame
from utils.sound_player import play_alert_sound


class CameraWindow:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Live Fire Detection")
        self.window.geometry("1000x750")
        self.window.configure(bg="#1e1e1e")

        # Header
        header = tk.Label(
            self.window,
            text="Live Fire Detection",
            font=("Segoe UI", 20, "bold"),
            fg="white",
            bg="#1e1e1e"
        )
        header.pack(pady=10)

        # Video frame display
        self.video_label = Label(self.window, bg="#1e1e1e")
        self.video_label.pack(pady=10)

        # Status label
        self.status_label = Label(
            self.window,
            text="Initializing...",
            font=("Segoe UI", 14),
            fg="#bbbbbb",
            bg="#1e1e1e"
        )
        self.status_label.pack(pady=20)

        # Stop Button
        stop_btn = tk.Button(
            self.window,
            text="Stop Camera",
            font=("Segoe UI", 12, "bold"),
            bg="#c92f2f",
            fg="white",
            relief="flat",
            padx=20,
            pady=10,
            command=self.close
        )
        stop_btn.pack(pady=10)

        # Camera
        self.cap = cv2.VideoCapture(0)

        self.alert_triggered = False

        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()

        if ret:
            annotated_bgr, fire_detected, max_conf = detect_fire_on_frame(frame)

            rgb = cv2.cvtColor(annotated_bgr, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(Image.fromarray(rgb))

            self.video_label.config(image=img)
            self.video_label.image = img

            if fire_detected:
                self.status_label.config(
                    text=f"FIRE DETECTED! Confidence: {max_conf:.2f}",
                    fg="#ff5050"
                )
                play_alert_sound()

            else:
                if max_conf > 0:
                    self.status_label.config(
                        text=f"No fire. Confidence: {max_conf:.2f}",
                        fg="#4caf50"
                    )
                else:
                    self.status_label.config(
                        text="No fire detected.",
                        fg="#bbbbbb"
                    )
                self.alert_triggered = False

        self.window.after(50, self.update_frame)

    def close(self):
        if self.cap.isOpened():
            self.cap.release()
        self.window.destroy()
