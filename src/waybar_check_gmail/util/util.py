import os
import pathlib
import stat
import sys
import textwrap


def msgfmt(msg, prefix=""):
    lines = []
    for line in msg.splitlines():
        lines += textwrap.wrap(line, 80 - len(prefix))
    return "\n".join([prefix + line for line in lines])


def warn(msg):
    print(msgfmt(msg, "warning: "))


def die(msg):
    sys.exit(msgfmt(msg, "error: "))


def mkdir_p(dir):
    try:
        pathlib.Path(dir).mkdir(parents=True, exist_ok=True)
    except FileExistsError:
        die("{} is not a directory".format(dir))


def is_group_or_other_writable(f):
    st = os.stat(f)
    return bool(st.st_mode & (stat.S_IWGRP | stat.S_IWOTH))


def is_group_or_other_readable(f):
    st = os.stat(f)
    return bool(st.st_mode & (stat.S_IRGRP | stat.S_IROTH))


def check_runtime_dir(dir):
    try:
        pathlib.Path(dir)
    except FileExistsError:
        die("{} is not a directory".format(dir))
