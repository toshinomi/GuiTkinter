import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.title(u"Hello World")
root.geometry("400x300")

def OnMessageBox(event):
    messagebox.showinfo('確認', 'Hello World')

Button = tkinter.Button(text=u'メッセージボックスを表示します', width=50)
Button.bind("<Button>", OnMessageBox) 
Button.pack()

root.mainloop()