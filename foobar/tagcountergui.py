from tkinter import *
from tkinter import ttk

import pkg_resources
import requests

from foobar.parser import Parser


class TagcounterGUI(Tk):
    def __init__(self):
        super(TagcounterGUI, self).__init__()
        self.title("Tkinter combobx")
        self.minsize(640, 400)
        self.main()

    def onclick(self):
        # todo put it in a separate function in Parser class
        response = requests.get('http://' + self.myfruit.get())
        if response.status_code == 200:
            response.encoding = 'utf-8'
            parser = Parser()
            tags_list = parser.parse_content(response.text)
            self.label.configure(text=tags_list)

    def main(self):
        print("class init")
        self.myfruit = StringVar()

        self.combo = ttk.Combobox(self, width=15, textvariable=self.myfruit)

        path = "config.yaml"
        filepath = pkg_resources.resource_filename(__name__, path)
        urls_list = []
        with open(filepath) as f:
            for line in f:
                (key, val) = line.split(':')
                urls_list.append(val.strip())
        # print(urls_list)

        self.combo['values'] = urls_list
        self.combo.grid(column=1, row=0)

        self.label = ttk.Label(self, text="Select address to parse:")
        self.label.grid(column=0, row=0)

        self.button = ttk.Button(self, text="Get tags", command=self.onclick)
        self.button.grid(column=1, row=1)


if __name__ == '__main__':
    root = TagcounterGUI()
    root.mainloop()
