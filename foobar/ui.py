from tkinter import *
from tkinter import ttk

import pkg_resources

from foobar.parser import Parser


class UI(Tk):
    def __init__(self):
        super(UI, self).__init__()
        self.title("Tag counter application")
        self.minsize(640, 400)
        self.main()

    def onclick(self):
        parser = Parser()
        tags_list = parser.parse_content(self.mychoice.get(), "http://")
        self.label.configure(text=tags_list)

    def main(self):
        print("class init")
        self.mychoice = StringVar()

        self.combo = ttk.Combobox(self, width=15, textvariable=self.mychoice)

        path = "config.yaml"
        filepath = pkg_resources.resource_filename(__name__, path)
        urls_list = []
        with open(filepath) as f:
            for line in f:
                (key, val) = line.split(':')
                urls_list.append(val.strip())

        self.combo['values'] = urls_list
        self.combo.grid(column=1, row=0)

        self.label = ttk.Label(self, text="Select address to parse:")
        self.label.grid(column=0, row=0)

        self.button = ttk.Button(self, text="Get tags", command=self.onclick)
        self.button.grid(column=1, row=5)


if __name__ == '__main__':
    root = UI()
    root.mainloop()
