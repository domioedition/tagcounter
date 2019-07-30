from tkinter import *
from tkinter import ttk


class Combobox(Tk):
    def __init__(self) -> object:
        super(Combobox, self).__init__()
        self.title("Tkinter combobx")
        self.minsize(640, 400)
        # self.wm_iconbitmap('icon.ico')
        self.InitUI()

    def clickme(self):
        self.label.configure(text="You have selected " + self.myfruit.get())

    def InitUI(self):
        self.myfruit = StringVar()

        self.combo = ttk.Combobox(self, width=15, textvariable=self.myfruit)
        self.combo['values'] = ('Apple', 'Pear', 'Melon', 'Banana')
        self.combo.grid(column=1, row=0)

        self.label = ttk.Label(self, text="Select address to parse:")
        self.label.grid(column=0, row=0)

        self.button = ttk.Button(self, text="Click", command=self.clickme)
        self.button.grid(column=1, row=1)


if __name__ == '__main__':
    root = Combobox()
    root.mainloop()
