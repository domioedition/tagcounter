from bs4 import BeautifulSoup


class Parser():
    def __init__(self):
        pass
    # todo make static??
    def parse_content(self, content):
        tags = {}
        soup = BeautifulSoup(content, 'html.parser')
        for tag in soup.findAll():
            if tag.name in tags:
                tags[tag.name] += 1
            else:
                tags[tag.name] = 1
        return tags

# if __name__ == '__main__':
#     parser = Parser()
