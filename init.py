#!/usr/bin/env python
import argparse
import logging
import os
import random
import sys
import shutil

parser = argparse.ArgumentParser(usage="""%(prog)s [options] args...
Copies base celery configuration (celery.py, celeryconfig.py) to your project directory, specified using --path=X
""")
parser.add_argument("-v", action="append_const", const=1, dest="verbosity", default=[],
                    help="Be more verbose. Can be specified multiple times to increase verbosity further")
parser.add_argument("--path", required=True, help="Target path for files")

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

def main(args):
    """
    Copy celery files to project from templates/
    """
    print("Initializing ansible-celery configuration into %s"%args.path)
    fr = lambda x: os.path.join(ROOT_DIR, 'templates/sample', x)
    to = lambda x: os.path.join(args.path, x)
    for target_file in ['celery.py', 'celeryconfig.py']:
        if not os.path.isfile(to(target_file)):
            print('%s copied to %s -- check configuration!'%(fr(target_file), to(target_file)))
            shutil.copyfile(fr(target_file), to(target_file))
        else:
            print('%s already exists'%to(target_file))
    print("Done.")
    return 0

def _configure_logging(args):
    verbosity_level = len(args.verbosity)
    if verbosity_level == 0:
        level = "WARNING"
    elif verbosity_level == 1:
        level = "INFO"
    else:
        level = "DEBUG"
    logging.basicConfig(
        stream=sys.stderr,
        level=level,
        format="%(asctime)s -- %(message)s"
        )

def main_entry_point():
    args = parser.parse_args()
    _configure_logging(args)
    sys.exit(main(args))

if __name__ == "__main__":
    main_entry_point()
