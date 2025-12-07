from ui.main_window import launch_main_window
from ui.camera_window import CameraWindow

def on_start_click():
    CameraWindow()

def main():
    launch_main_window(on_start_click)

if __name__ == "__main__":
    main()
