#!/usr/bin/env python3
import argparse
import subprocess

parser = argparse.ArgumentParser()

sub_parsers = parser.add_subparsers(dest="cmd", required=True)
_build_parser = sub_parsers.add_parser("build")
_publisher_parser = sub_parsers.add_parser("publish")

args = parser.parse_args()
if args.cmd == "build":
    subprocess.run(["python3", "setup.py", "sdist", "bdist_wheel"], check=True)
elif args.cmd == "publish":
    subprocess.run("twine upload dist/*", shell=True, check=True)
