# DuckTape Dock

DuckTape Dock is a customizable desktop application launcher built with Python, CustomTkinter, and SQLite. It is designed to give users one clean place to organize, sort, and launch their programs.

## Project Status

DuckTape Dock is currently in development.

Version 0.1 established the base project structure, interface, branding, theme, and SQLite database system.

## Planned Features

- Add programs, files, folders, scripts, and links
- Launch saved items directly from the dock
- Organize apps into custom groups
- Allow one app to belong to multiple groups
- Sort apps independently on the home screen and inside groups
- Reorder groups
- Add custom names, commands, icons, and app types
- Edit and remove saved apps
- Create, edit, and remove groups
- Store user data locally with SQLite
- Clean dark-mode interface
- Package the program as a standalone Windows application

## How It Works

DuckTape Dock stores its data in three SQLite tables:

- `Apps` stores application information
- `Groups` stores user-created groups
- `AppGroups` connects apps and groups through a junction table

Apps have a home-screen sort position, while apps inside groups use their own group-specific sort position.

## Built With

- Python
- SQL
- CustomTkinter
- SQLite
- Pillow
- PyInstaller

Goal:

The goal of DuckTape Dock is to provide a simple launcher that can replace scattered desktop shortcuts with a cleaner and more customizable interface.

Author

Created by Chris Herriman Jr.
