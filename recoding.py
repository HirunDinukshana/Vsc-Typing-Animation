import pygetwindow as gw
import mss
import numpy as np
import cv2
import threading
import time
from datetime import datetime

class Recorder:
    def __init__(self, window_title, output_file=None, fps=60):
        self.window_title = window_title
        if output_file:
            self.output_file = output_file
        else:
            now = datetime.now().strftime("%Y%m%d_%H%M%S")
            self.output_file = f"recording_{now}.avi"
        self.fps = fps
        self.recording = False
        self.thread = None

    def _get_window_region(self):
        windows = gw.getWindowsWithTitle(self.window_title)
        if not windows:
            raise Exception(f"Window '{self.window_title}' not found")
        win = windows[0]
        return {"top": win.top, "left": win.left, "width": win.width, "height": win.height}

    def _record(self):
        with mss.mss() as sct:
            out = None
            while self.recording:
                try:
                    region = self._get_window_region()
                    img = np.array(sct.grab(region))
                    frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

                    if out is None:
                        out = cv2.VideoWriter(
                            self.output_file,
                            cv2.VideoWriter_fourcc(*"MJPG"),
                            self.fps,
                            (region["width"], region["height"])
                        )

                    out.write(frame)
                except Exception as e:
                    print("Recording error:", e)
                time.sleep(1 / self.fps)
            if out:
                out.release()

    def start(self):
        if self.recording:
            print("Already recording")
            return
        self.recording = True
        self.thread = threading.Thread(target=self._record, daemon=True)
        self.thread.start()
        print(f"Recording started -> {self.output_file}")

    def stop(self):
        if not self.recording:
            print("Not recording")
            return
        self.recording = False
        self.thread.join()
        print(f"Recording stopped -> {self.output_file}")


_recorder = None

def Start_recoding(window_title="VsC Typing Animation", output_file=None, fps=60):
    global _recorder
    if _recorder and _recorder.recording:
        print("Already recording")
        return
    _recorder = Recorder(window_title, output_file, fps)
    _recorder.start()

def Stop_recoding():
    global _recorder
    if _recorder:
        _recorder.stop()
        _recorder = None
