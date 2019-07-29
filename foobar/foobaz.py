import pkg_resources
from argparse import ArgumentParser
from bs4 import BeautifulSoup
from tkinter import *
import tkinter

from foobar.database import statistic


def read_file(filename):
    with open(filename) as input_file:
        text = input_file.read()
    return text


def read_stream(stream):
    return stream


def parse_content(content):
    tags = {}
    soup = BeautifulSoup(content, 'html.parser')
    for tag in soup.findAll():
        if tag.name in tags:
            tags[tag.name] += 1
        else:
            tags[tag.name] = 1
    return tags


def main():
    parser = ArgumentParser()
    # parser.add_argument("indent", type=int, help="indent for report")
    # parser.add_argument("input_file", help="read data from this file")
    parser.add_argument("-g", "--get", dest="config", help="parse the specified from config file",
                        metavar="CONFIG FILE")
    parser.add_argument("-f", "--file", dest="filename", help="parse the specified FILE", metavar="FILE")
    parser.add_argument("-r", "--resource", dest="resource", help="parse the specified RESOURCE",
                        metavar="RESOURCE")
    parser.add_argument("-t", "--test", dest="test", action="store_true", default=False, help="Test mode")
    parser.add_argument("-v", "--view", dest="view", help="Check address in DB")
    # parser.add_argument("-x", "--xray",
    #                     help="specify xray strength factor")
    # parser.add_argument("-q", "--quiet",
    #                     action="store_false", dest="verbose", default=True,
    #                     help="don't print status messages to stdout")
    args = parser.parse_args()
    html_doc = None
    name_of_resource = None
    url = None
    if (args.resource is not None):
        """Parse from resource"""
        import requests
        response = requests.get(args.resource)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            # print(response.text)
            html_doc = response.text
        else:
            print('An error has occurred.')

    elif (args.filename is not None):
        """Parse file"""
        html_doc = args.filename
    elif (args.view is not None):
        dbms = statistic.Statistic()
        dbms.get_all()
        # dbms.get_record(args.view)
    elif (args.config is not None):
        """Parse config.yaml file"""
        path = "config.yaml"
        filepath = pkg_resources.resource_filename(__name__, path)
        d = {}
        with open(filepath) as f:
            for line in f:
                (key, val) = line.split(':')
                d[key] = val.strip()
                if args.config == val.strip() or args.config == key:
                    # print(args.config)
                    import requests
                    name_of_resource = val.strip()
                    url = "http://" + val.strip()
                    response = requests.get(url)
                    if response.status_code == 200:
                        response.encoding = 'utf-8'
                        html_doc = response.text
                    else:
                        print('An error has occurred.')
    else:
        print("Start GUI tkinter")
        path = "config.yaml"
        filepath = pkg_resources.resource_filename(__name__, path)
        checkbox_list = {}
        top = Tk()
        with open(filepath) as f:
            for line in f:
                (key, val) = line.split(':')
                # checkbox_list[key] = val.strip()
                # CheckVar
                key = Checkbutton(top, text=val.strip(), variable=key, \
                                  onvalue=1, offvalue=0, height=5, \
                                  width=20, )
                key.pack()
            top.mainloop()
        # print(checkbox_list)


    if html_doc is not None:
        all_tags = parse_content(html_doc)
        print(all_tags)
        dbms = statistic.Statistic()
        dbms.add_new_record(name=name_of_resource, url=url, tags=all_tags)

    # #todo import my own logger
    # import foobar.Logger as t
    # t.testlogger()


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


if __name__ == '__main__':
    main()
