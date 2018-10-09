import webbrowser

from threading import Timer

from app import app
from appconfig import Configuration

def openBrowserSlowly():
    webbrowser.open_new_tab("http://127.0.0.1:5000")

if __name__ == '__main__':
    
    # Open Browser after 5 seconds
    #t=Timer(2.0, openBrowserSlowly)
    #t.start()

    # Start flask app
    app.run(debug=True)
