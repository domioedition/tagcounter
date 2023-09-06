from bs4 import BeautifulSoup

from src.pasrser.parser import Parser


class HtmlParser(Parser):
    def __init__(self):
        self._html_parser = BeautifulSoup()

    def parse_content(self, content) -> dict:
        tags = {}

        soup = BeautifulSoup(content, "html.parser")
        for tag in soup.findAll():
            if tag.name in tags:
                tags[tag.name] += 1
            else:
                tags[tag.name] = 1

        return tags
