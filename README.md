# Universal Problem Parser Tool

## Install

Simple and straight. Make sure you have Python3 and pip. Then install using this command.

`pip install universal-parser-tool`

This script needs selenium to run. The python library will be added by default if you use the above command. 
The below link has explained how to install selenium drivers.
Firefox is the default driver for this code, so install Firefox and it's driver as in the link below.

https://selenium-python.readthedocs.io/installation.html

The main idea is based on [this repository](https://github.com/xalanq/cf-tool).
So you must add `cf` to your PATH.

After installing, `upt` command will be added to your PATH.

## Parse

You can use `upt` like this script:

`upt <PARSER> <PARSER COMMANDS>`


## Supported Parser

In this time, these judges have parsers. You can find more info about them
in their directory.

- AtCoder (Added login feature!)
- Codechef
- Spoj
- Quera

**NOTE**: You may use the parser for practice problems. During a contest, some judges need to log in.
For now, this feature is supported by atcoder parser. Universal Problem Parser Tool
