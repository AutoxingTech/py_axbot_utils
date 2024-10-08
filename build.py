#!/usr/bin/env python3
import argparse
import subprocess
import shutil
import os

FOLDER = "py_axbot_utils"

parser = argparse.ArgumentParser()

sub_parsers = parser.add_subparsers(dest="cmd", required=True)
_build_parser = sub_parsers.add_parser("build")
_build_parser = sub_parsers.add_parser("clean")
_publisher_parser = sub_parsers.add_parser("publish")
_translate_parser = sub_parsers.add_parser("i18n")

args = parser.parse_args()
if args.cmd == "clean":
    for folder in ["build", "dist", f"{FOLDER}.egg-info"]:
        if os.path.isdir(folder):
            shutil.rmtree(folder)
elif args.cmd == "build":
    subprocess.run(["python3", "setup.py", "sdist", "bdist_wheel"], check=True)
elif args.cmd == "publish":
    subprocess.run("twine upload dist/*", shell=True, check=True)
elif args.cmd == "i18n":
    subprocess.run(
        f'xgettext --from-code=UTF-8 -o messages.pot $(find {FOLDER} -name "*.py")',
        shell=True,
        check=True,
    )
