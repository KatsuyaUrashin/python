import tkinter
from tkinter.constants import *

TK = None
def main():
    global TK
    tk = tkinter.Tk()
    TK = tk
    frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
    frame.pack(fill=BOTH, expand=1)
    label = tkinter.Label(frame, text="******** Hello, World ********")
    label.pack(fill=X, expand=1)
    label2 = tkinter.Label(frame, text="******** Hello, World ********")
    label2.pack(fill=X, expand=1)
    button = tkinter.Button(frame, text="Exit", command=eFunc)
    button.pack(side=BOTTOM)
    tk.mainloop()

def eFunc():
    print("Exit!")
    TK.destroy()
    # exit()

if __name__ == '__main__':
    #print('hello!')
    main()
