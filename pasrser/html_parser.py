import requests

from bs4 import BeautifulSoup

from pasrser.parser import Parser


class HtmlParser(Parser):
    def __init__(self):
        self._html_parser = BeautifulSoup()

    def parse_content(self, url) -> dict:
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError("Data is not available")

        if response.encoding != "UTF-8":
            response.encoding = "utf-8"
        tags = {}

        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup.findAll():
            if tag.name in tags:
                tags[tag.name] += 1
            else:
                tags[tag.name] = 1

        return tags
