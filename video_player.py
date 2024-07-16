import tkinter as tk
from tkinter import messagebox, filedialog
import cv2
from PIL import Image, ImageTk
import os

class VideoPlayer:
    def __init__(self, window, video_source=0):
        self.window = window
        self.window.title("Video Player")

        # Video capture from camera or file
        self.cap = cv2.VideoCapture(video_source)
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Canvas for displaying video frames
        self.canvas = tk.Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()

        # Buttons for control
        self.record_btn = tk.Button(window, text="Record", command=self.record)
        self.record_btn.pack(side=tk.LEFT, padx=5, pady=10)

        self.pause_btn = tk.Button(window, text="Pause", command=self.pause)
        self.pause_btn.pack(side=tk.LEFT, padx=5, pady=10)

        self.stop_btn = tk.Button(window, text="Stop", command=self.stop)
        self.stop_btn.pack(side=tk.LEFT, padx=5, pady=10)

        self.save_btn = tk.Button(window, text="Save", command=self.save)
        self.save_btn.pack(side=tk.LEFT, padx=5, pady=10)

        self.select_location_btn = tk.Button(window, text="Select Location", command=self.select_location)
        self.select_location_btn.pack(side=tk.LEFT, padx=5, pady=10)

        # Save location
        self.save_location = None
        self.output_file = None
        self.is_recording = False

        # Video playback control
        self.is_playing = True
        self.delay = 15  # milliseconds
        self.update()

        self.window.mainloop()

    def update(self):
        if self.is_playing:
            ret, frame = self.cap.read()
            if ret:
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
                if self.is_recording:
                    if self.output_file is None:
                        messagebox.showwarning("Warning", "Recording output file is not set.")
                        self.is_recording = False
                    else:
                        self.output_file.write(frame)

        self.window.after(self.delay, self.update)

    def record(self):
        if not self.save_location:
            messagebox.showwarning("Warning", "Please select a save location first.")
            return

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.output_file = cv2.VideoWriter(os.path.join(self.save_location, 'output.avi'), fourcc, 20.0, (self.width, self.height))

        self.is_recording = True
        messagebox.showinfo("Recording", "Recording started. Click 'Stop' to end recording.")

    def pause(self):
        self.is_playing = False

    def stop(self):
        self.is_recording = False
        messagebox.showinfo("Recording Stopped", "Recording stopped successfully.")
        if self.output_file is not None:
            self.output_file.release()
            self.output_file = None

    def save(self):
        if not self.save_location:
            messagebox.showwarning("Warning", "Please select a save location first.")
            return

        # Implement saving functionality here (e.g., saving frames or video to self.save_location)

    def select_location(self):
        self.save_location = filedialog.askdirectory()
        if self.save_location:
            messagebox.showinfo("Location Selected", f"Save location set to:\n{self.save_location}")

# Create a window and pass it to the video player class
root = tk.Tk()
app = VideoPlayer(root)
