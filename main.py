import webview
from webview.dom import DOMEventHandler
import os
import signal
import datetime
from recoding import Start_recoding,Stop_recoding
from pathlib import Path

file_list = []

handler = None
ffmpeg_p = None

def on_drag(e):
    pass

def on_drop(e):
    files = e['dataTransfer']['files']
    global file_list
    file_list = []
    if len(files) == 0:
        return

    print(f'Event: {e["type"]}. Dropped files:')

    for file in files:
        file_list.append(file.get('pywebviewFullPath'))
        
    handler.evaluate_js('request_files()')

def bind(window):
    window.dom.document.events.dragenter += DOMEventHandler(on_drag, True, True)
    window.dom.document.events.dragstart += DOMEventHandler(on_drag, True, True)
    window.dom.document.events.dragover += DOMEventHandler(on_drag, True, True, debounce=500)
    window.dom.document.events.drop += DOMEventHandler(on_drop, True, True)

def start_up(_handler):
    global handler
    handler = _handler
    bind(handler)

class js_API:
    def get_opened_file(self):
        if len(file_list) > 0:
            return file_list
    def get_data(self,file):
        print(file)
        with open(file,"r",encoding="utf-8") as f:
            return f.read()
    def app_close(self):
        print("CLOSING")
        os.kill(os.getpid(),signal.SIGTERM)
    def app_minimize(self):
        win.minimize()
    def app_maximize(self):
        if not getattr(win, 'maximized', False):
            win.maximize()
            win.maximized = True
        else:
            win.restore()
            win.maximized = False
    def start_recoding(self):
        now = datetime.datetime.now()
        file_name = f"VsC Typing Animation {now.strftime('%Y-%m-%d_%H-%M-%S')}.avi"
        file_name = os.path.join(Path.home(),"Videos",file_name)
        print(file_name)
        Start_recoding(output_file=file_name)
    def stop_recording(self):
        Stop_recoding()
   
win = webview.create_window(title="VsC Typing Animation",
                            width=1200,
                            js_api=js_API(),
                            height=800,
                            frameless=True,
                            url=os.path.join(os.path.dirname(os.path.abspath(__file__)),'index.html'))

webview.start(start_up,win,debug=True)