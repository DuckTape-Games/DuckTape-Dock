import webview  # Displays local HTML/CSS/JS inside a desktop app window
from utils.helpers import launch_webview_page, resource_path
from utils import theme

launch_webview_page(resource_path("ui/index.html"), "DuckTape Dock", theme.APP_ICON)