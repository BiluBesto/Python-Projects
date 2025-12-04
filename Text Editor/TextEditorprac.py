import tkinter as tk
from tkinter.filedialog import askopenfilename,asksaveasfilename

filepath = ""

def openfile(window,textedit):
    global filepath
    filepath = askopenfilename(filetypes=[("Text","*.txt")])
    if not filepath:
        return
    textedit.delete(1.0,tk.END)
    with open(filepath,"r") as f:
        content = f.read()
        textedit.insert(tk.END,content)
    window.title(filepath)

def savefile(window,textedit):
    global filepath
    filepath = asksaveasfilename(filetypes=[("Text","*.txt")])
    if not filepath:
        return
    window.title(filepath)
    with open(filepath,"w") as f:
        content = textedit.get(1.0,tk.END)
        f.write(content)

def savefilecur(window,textedit):
    global filepath
    if not filepath:
        return
    window.title(filepath)
    with open(filepath,"w") as f:
        content = textedit.get(1.0,tk.END)
        f.write(content)

def main():
    window = tk.Tk()
    window.rowconfigure(0,minsize=300)
    window.columnconfigure(1,minsize=300)
    window.title("Text Editor made by Besto")
    textedit = tk.Text(window,font = "Rubik 12 bold")
    textedit.grid(row=0,column=1)
    frame = tk.Frame(window,relief = "raised", bd = 2)
    openbut = tk.Button(frame,text = "Open",command = lambda:openfile(window,textedit))
    savebut = tk.Button(frame, text="Save", command=lambda: savefile(window, textedit))
    savecurbut = tk.Button(frame, text="Save Current",command = lambda:savefilecur(window,textedit))
    openbut.grid(row=0,column=0,padx=10)
    savebut.grid(row=1,column=0,padx=10)
    savecurbut.grid(row=2,column=0)
    frame.grid(row=0,column=0,sticky = "ns")
    window.bind("<Control-Shift-S>",lambda x: savefile(window, textedit))
    window.bind("<Control-s>",lambda x:savefilecur(window,textedit))
    window.bind("<Control-o>",lambda x:openfile(window,textedit))
    window.mainloop()
main()