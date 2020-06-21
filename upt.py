import logging
import os
import sys

from utils import Driver

import atcoder
import codechef
import quera
import spoj

PARSERS = {"atcoder": atcoder,
           "quera": quera,
           "codechef": codechef,
           "spoj": spoj}


def excepthook(type, value, traceback):
    logging.error(value)


sys.excepthook = excepthook
logging.basicConfig(level=logging.INFO, format="== [%(levelname)s] %(message)s")

args = sys.argv[1:]

if len(args) < 2:
    raise Exception("Arguments not enough")

main_parser = PARSERS.get(args[0])
if main_parser is None:
    raise Exception(f"Parser \"{args[0]}\" not found")

main_parser = main_parser.Parser

logging.info(f"Parser \"{args[0]}\" called")
main_parser.parse(args[1:])
logging.info(f"Parser \"{args[0]}\" finished")

os.system("rm *.log")
logging.info("all logs removed")

os.system("cf gen")
