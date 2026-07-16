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


### Resizes an image
def resize_image(image, new_width=None, new_height=None):
    """
    If neither dimensions are given, original image will be returned
    If both width AND height are given, image will be stetched to fit the new dimensions
    If only width OR height is given, image will be resized with the same ratio
    """
    original_width, original_height = image.size

    #Just image is given
    if not new_width and not new_height:
        return image #Skips the rest of the function by returning the original image
    
    #Just width is given
    if new_width and not new_height:
        ratio = new_width / original_width
        new_height = int(original_height * ratio)

    #Just height is given
    elif new_height and not new_width:
        ratio = new_height / original_height
        new_width = int(original_width * ratio)

    #Returns the resized image with the new ratios
    return image.resize((new_width, new_height))


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
    on_close_message="The Page Was Closed",
    pause_on_close=True
):
    """Launches a local HTML file inside a pywebview window."""

    # Converts the provided path into a full absolute path
    html_file = Path(html_path).resolve()

    # Stops the program early if the HTML file does not exist
    if not html_file.exists():
        raise FileNotFoundError(f"HTML file not found: {html_file}")

    # Runs when the pywebview window is closed
    def on_window_closed():
        print(on_close_message)

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