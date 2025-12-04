📝 Simple Python Text Editor (Tkinter)

A lightweight and beginner-friendly text editor built using Python Tkinter.
This project demonstrates how to create a functional GUI-based text editing application with file operations such as Open, Save, and Save Current.

🚀 Features
✔️ Open Text Files

Opens .txt files using a file dialog

Loads content directly into the editor

Updates window title with the file path

✔️ Save As

Saves current text to a new .txt file

Uses Ctrl + Shift + S as a shortcut

Updates window title with the saved file path

✔️ Save Current File

Saves content to the currently opened file

Uses Ctrl + S

✔️ Keyboard Shortcuts
Action	Shortcut
Open File	Ctrl + O
Save As	Ctrl + Shift + S
Save Current File	Ctrl + S
✔️ Clean UI

Sidebar with buttons: Open, Save, Save Current

Main text area with custom font

Resizable layout using Tkinter’s grid configuration

📦 Requirements

Python 3.x

Tkinter (built-in with most Python installations)

No external libraries required.

▶️ How to Run

Clone or download the repository.

Save the Python script as text_editor.py (or any name you prefer).

Run:

python text_editor.py


The text editor window will open immediately.

🧩 Code Overview
Main Components

openfile()
Opens a file and loads its content into the editor.

savefile()
“Save As” – lets you choose a file path before saving.

savefilecur()
Saves content to the current file (if one is open).

main()
Builds the UI, binds shortcuts, and starts the Tkinter event loop.

📁 File Types Supported

.txt
