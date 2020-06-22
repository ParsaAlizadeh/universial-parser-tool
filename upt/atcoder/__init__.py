from upt.utils import Utils, Driver
from configparser import ConfigParser
import getpass
import re


class Parser:
    def __init__(self):
        self.driver = Driver()

    def parse(self, args: list):
        if args[0] == "init":
            return self.initialize()

        url = f"http://atcoder.jp/contests/{args[0]}/tasks/{args[0]}_{args[1]}"
        Utils.load_url(self.driver, url)

        pattern = re.compile(r"pre\-sample\d")
        elements = self.driver.find_elements_by_css_selector("pre")
        sample = []
        for elem in elements:
            if pattern.match(elem.get_attribute("id")) and len(elem.text) > 0:
                sample.append(elem.text)

        result = Utils.even_odd(sample)
        Utils.write_samples(result)

    @staticmethod
    def initialize():
        print("Authentication for atcoder.jp")
        user = getpass.getuser("Username: ")
        pwd = getpass.getpass("Password: ")

        configparser = ConfigParser()
        configparser.read("config.ini")
        configparser["atcoder"]["user"] = user
        configparser["atcoder"]["pass"] = pwd
        configparser.write("config.ini")

