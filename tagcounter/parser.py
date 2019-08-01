from bs4 import BeautifulSoup
import requests
import logging
from datetime import datetime

from tagcounter.statistic import Statistic


class Parser():
    def __init__(self):
        pass

    # todo make static??
    def parse_content(self, link_resource, protocol):
        url = protocol + link_resource
        response = requests.get(url)
        if response.status_code == 200:
            self.make_log_record(url)
            response.encoding = 'utf-8'
            tags = {}
            soup = BeautifulSoup(response.text, 'html.parser')
            for tag in soup.findAll():
                if tag.name in tags:
                    tags[tag.name] += 1
                else:
                    tags[tag.name] = 1
            dbms = Statistic()
            dbms.add_new_record(link_resource, url, tags)

            return tags

    def make_log_record(self, url):
        """Creating record in log file with date and tim """
        logging.basicConfig(filename='app.log', filemode='a', format='%(message)s')
        logging.warning(str(datetime.now()) + " - " + url)

# if __name__ == '__main__':
#     parser = Parser()
