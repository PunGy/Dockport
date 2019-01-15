#!/usr/bin/python3

from sys import argv
import subprocess

# CONFIG
state = {
    "browser": False,
    "prefix": "",
    "buffer": False,
    "server": "localhost",
    "delimiter": "-",
    "container": "",
    "envFileName": ".env",
    "envNameContainer": "PROJECT_NAME",
    "env": False
}
abbreviations = {
    "pma": "phpmyadmin",
    "serve": "nginx"
}
NOT_FOUND = -1
# CONFIG/


# FUNCTIONS
def get_env():
    try:
        env = open(state["envFileName"])
        prefix = False
    except FileNotFoundError:
        return False
    for line in env:
        if line.find(state["envNameContainer"]) != NOT_FOUND:
            prefix = line.split('=')[1].strip('\n')
    return prefix


def prepare_data():
    global args
    global container
    global state
    global abbreviations

    if argv[0].find("python") == NOT_FOUND:
        args = argv[1:]
    else:
        args = argv[2:]

    try:
        if len(args) == 0 or args[0][0] == '-':
            raise Exception("Enter name of container!")
        container = args.pop(0)
        container = container if abbreviations.get(container) is None else abbreviations.get(container)
        prefix = get_env()
        if len(args) > 0:
            i = 0
            while i < len(args):
                if args[i] == '-p':
                    if get_env() is not False:
                        i += 1
                        state["prefix"] = prefix
                        continue

                    if args[i - 1] == args[len(args) - 1] or args[i][0] == '-':
                        i += 1
                        raise Exception("Wrong prefix name!")
                    state["prefix"] = args[i]

                if args[i] == '-b':
                    state["buffer"] = True
                if args[i] == '-o':
                    state["browser"] = True
                i += 1

        state["prefix"] = state["prefix"] = state["prefix"] + state["delimiter"] if len(state["prefix"]) != 0 else ""
        state["container"] = container
        container = state["prefix"] + container
    except Exception as e:
        print(e)
        exit()
    except IndexError:
        print("out")


# START OF PROGRAM
prepare_data()
try:
    port = subprocess.Popen("docker port " + container, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)\
        .stdout.read().decode("utf-8").strip()

    port = port[port.find(':') + 1:]
    url = state["server"] + ":" + port
    print(url)
except Exception as msg:
    print(msg)
    exit()
