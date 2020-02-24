import logging

import json
import requests

from bs4 import BeautifulSoup


logger = logging.getLogger(__name__)


class AbstractIndustry(object):

    def __init__(self, title, children):
        logger.info("Creating industry ({title})".format(title=title))
        self.title = title
        self.children = children

    @property
    def level(self):
        raise NotImplementedError

    def add_child(self, child):
        self.children.append(child)

    def to_dict(self):
        return {
            "title": self.title,
            "children": [
                child.to_dict() for child in self.children
            ]
        }

    @staticmethod
    def from_dict(**kwargs):
        raise NotImplementedError

    def jsonify(self):
        return json.dumps(self.to_dict())


class Division(AbstractIndustry):
    level = "SIC Division"

    @staticmethod
    def from_dict(**kwargs):
        return Division(
            title=kwargs["title"],
            children=[
                MajorGroup.from_dict(**k)
                for k in kwargs.get("children", [])
            ]
        )


class MajorGroup(AbstractIndustry):
    level = "SIC Major Group"

    @staticmethod
    def from_dict(**kwargs):
        pass


class Group(AbstractIndustry):
    level = "SIC Industry Group"

    @staticmethod
    def from_dict(**kwargs):
        pass


class Single(AbstractIndustry):
    level = "SIC Industry"

    @staticmethod
    def from_dict(**kwargs):
        pass


class SIC(AbstractIndustry):
    level = "Standard Industry Classification"

    @staticmethod
    def from_dict(**kwargs):
        pass
