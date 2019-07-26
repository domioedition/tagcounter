import pkg_resources
from argparse import ArgumentParser
from bs4 import BeautifulSoup


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
    parser.add_argument("-f", "--file", dest="filename", help="parse the specified FILE", metavar="FILE")
    parser.add_argument("-t", "--test", dest="test", action="store_true", default=False, help="Test mode")
    # parser.add_argument("-x", "--xray",
    #                     help="specify xray strength factor")
    # parser.add_argument("-q", "--quiet",
    #                     action="store_false", dest="verbose", default=True,
    #                     help="don't print status messages to stdout")
    args = parser.parse_args()
    html_doc = None
    if (args.filename is not None):
        print("Start file parser")
        print(args.filename)
        html_doc = args.filename
    else:
        print("Start GUI tkinter")

    if html_doc is not None:
        html_content = read_file(html_doc)
        # html_content = read_stream(html_doc)
        all_tags = parse_content(html_content)
        print(all_tags)

    # path = "example.txt"
    # filepath = pkg_resources.resource_filename(__name__, path)
    # print("I am main!!!!!!!!!")
    # print("\n\ntest\n\n")
    # for l in open(filepath, 'r'):
    #     print(l)


if __name__ == '__main__':
    main()
