import sys, os
import webview  # Displays local HTML/CSS/JS inside a desktop app window
from pathlib import Path  # Handles file paths safely across systems


### Makes onefile mode work in pyinstaller
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


### Loads an SQL query
def load_query(queryFile):
    queryPath = resource_path(f"database/queries/{queryFile}")

    with open(queryPath, "r", encoding="utf-8") as sqlFile:
        return sqlFile.read()
    

### Launches an HTML file using pywebview
def launch_webview_page(
    html_path,
    title="New Page",
    app_icon=None,
    width=1100,
    height=700,
    pause_on_close=False
):
    """Launches a local HTML file inside a pywebview window."""

    # Converts the provided path into a full absolute path
    html_file = Path(html_path).resolve()

    # Stops the program early if the HTML file does not exist
    if not html_file.exists():
        raise FileNotFoundError(f"HTML file not found: {html_file}")

    # Runs when the pywebview window is closed
    def on_window_closed():
        from database.database import close_database
        close_database()

        # Keeps the terminal open so closing messages/errors can be read
        if pause_on_close:
            input("Press Enter to exit...")

    # Creates the desktop window that will display the HTML page
    window = webview.create_window(
        title,
        html_file.as_uri(),
        width=width,
        height=height
    )

    # Connects the close event to the custom close function
    window.events.closed += on_window_closed

    # Starts the pywebview event loop
    webview.start(icon=app_icon)