# import pkg_resources
# from argparse import ArgumentParser
#
# import statistic
# import parser
# from tagcounter.ui import UI


class TagCounterHandler:
    def __init__(self, parser, logger):
        self._parser = parser
        self._logger = logger

    def please_count_tags(self, url):
        return self._parser.parse_content(url)

    def please_count_tags_using_ui(self):
        pass


#
# def main():
#     parser = ArgumentParser()
#     parser.add_argument("-g", "--get", dest="config", help="parse the specified from config file",
#                         metavar="CONFIG FILE")
#     parser.add_argument("-r", "--resource", dest="resource", help="parse the specified RESOURCE",
#                         metavar="RESOURCE")
#     parser.add_argument("-t", "--test", dest="test", action="store_true", default=False, help="Test mode")
#     parser.add_argument("-v", "--view", dest="view", help="Check address in DB")
#     args = parser.parse_args()
#
#     url = None
#     if (args.resource is not None):
#         """Parse from resource"""
#         url = args.resource
#     elif (args.view is not None):
#         dbms = statistic.Statistic()
#         dbms.get_record(args.view)
#     elif (args.config is not None):
#         """Parse config.yaml file"""
#         path = "config.yaml"
#         filepath = pkg_resources.resource_filename(__name__, path)
#         d = {}
#         with open(filepath) as f:
#             for line in f:
#                 (key, val) = line.split(':')
#                 d[key] = val.strip()
#                 if args.config == val.strip() or args.config == key:
#                     url = val.strip()
#     else:
#         print("Start GUI tkinter")
#         x = UI()
#         x.main()
#         # start.main()
#         # def close_window():
#         #     root.destroy()
#         #
#         # def onclick(args):
#         #     if args == 1:
#         #         T.delete('1.0', END)
#         #         import requests
#         #         response = requests.get('http://ua.fm')
#         #         if response.status_code == 200:
#         #             response.encoding = 'utf-8'
#         #             # print(response.text)
#         #             all_tags = parse_content(response.text)
#         #             T.insert(tkinter.END, all_tags)
#         #             print(all_tags)
#         #     if args == 2:
#         #         print(2)
#         #     if args == 3:
#         #         print(3)
#         #
#         # all_tags = ""
#         # root = tkinter.Tk()
#         # root.title("Tagcounter")
#         # root.geometry("500x300")
#         #
#         # btn1 = tkinter.Button(root, text="Button1", command=lambda: onclick(1))
#         # btn2 = tkinter.Button(root, text="Button2", command=lambda: onclick(2))
#         # btn3 = tkinter.Button(root, text="Close", command=lambda: close_window())
#         # btn1.pack()
#         # btn2.pack()
#         # btn3.pack()
#         #
#         # T = tkinter.Text(root, height=50, width=200)
#         # T.pack()
#         #
#         # root.mainloop()
#
#         # path = "config.yaml"
#         # filepath = pkg_resources.resource_filename(__name__, path)
#         # checkbox_list = {}
#         # top = Tk()
#         # with open(filepath) as f:
#         #     for line in f:
#         #         (key, val) = line.split(':')
#         #         # checkbox_list[key] = val.strip()
#         #         # CheckVar
#         #         key = Checkbutton(top, text=val.strip(), variable=key, \
#         #                           onvalue=1, offvalue=0, height=5, \
#         #                           width=20, )
#         #         key.pack()
#         #     top.mainloop()
#         # # print(checkbox_list)
#
#         # todo implemt save statistic to db
#         # dbms = statistic.Statistic()
#         # dbms.add_new_record(name=name_of_resource, url=url, tags=all_tags)
#
#         # todo implement logger
#         # todo implement unittests
#
#     # import tagcounter.Logger as t
#     # t.testlogger()
#
#     if url is not None:
#         parser = Parser()
#         tags_list = parser.parse_content(url, "http://")
#         print(tags_list)


"""Logging"""
# import logging
# from datetime import datetime, date, time
# print(datetime.now())
# # logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(filename='app.log', filemode='a', format='%(message)s')
# logging.warning(str(datetime.now()) + " - " + args.resource)  # todo we need correct args.resource


# print(args.resource)
# logging.error('This will get logged to a file')
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')
# logging.warning('This will get logged to a file')

# """loguru logger"""
# from loguru import logger
#
# logger.debug("That's it, beautiful and simple logging!")
# logger.add("file.log")

# import logging
# logging.basicConfig(level=logging.INFO)
# import sys
# # logging.basicConfig(stream=sys.stdout, level=logging.INFO)
# # logging.basicConfig(filename="info.log", level=logging.INFO)
# # logging.info("My message")
#
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# logger.info('I told you info')
# logger.error('I told you error')

# path = "example.txt"
# filepath = pkg_resources.resource_filename(__name__, path)
# print("I am main!!!!!!!!!")
# print("\n\ntest\n\n")
# for l in open(filepath, 'response'):
#     print(l)
#
#
# if __name__ == '__main__':
#     main()
