import argparse

from logger.logger_handler import LoggerHandler
from pasrser.html_parser import HtmlParser
from pasrser.xml_parser import XmlParser
from statstic.statistic_handler import StatisticHandler
from tagcounter.tagcounterhandler import TagCounterHandler


def main():
    parser = HtmlParser()
    logger = LoggerHandler()

    url = "http://example.com"  # todo check error handling and logging

    argument_parser = argparse.ArgumentParser(description="Ping script")
    argument_parser.add_argument(
        "-r",
        "--resource",
        dest="resource",
        help="parse the specified RESOURCE",
        metavar="RESOURCE",
    )
    args = argument_parser.parse_args()

    if args.resource:
        url = args.resource

    try:
        logger.info("Initialized")
        tag_counter = TagCounterHandler(parser, logger)
        tags = tag_counter.please_count_tags(url)
        print(tags)

        # todo implement saving to the database SQLAlchemy
        # dbms = StatisticHandler()
        # dbms.add_new_record("link_resource", url, tags)

    except ValueError as e:
        print(e.args[0])
        logger.error(e.args[0])
    except Exception as e:
        print(e.args)
        print(e)
        print("An exception occurred")
    finally:
        print("Finally done")


if __name__ == "__main__":
    main()
