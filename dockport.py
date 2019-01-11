#!/usr/bin/python3
# port = os.system("docker port intracar-nginx")

from sys import argv
import os


def prepare_data():
    global args
    global container
    global state
    args = argv[1:]
    state = {
        "browser": False,
        "prefix": "",
        "buffer": False,
        "delimiter": "-",
        "container": ""
    }
    try:
        container = args.pop(0)
        if container[0] == '-':
            raise Exception("Enter name of container!")

        if len(args) > 0:
            i = 0
            while i < len(args):
                if args[i] == '-p':
                    i += 1
                    if args[i - 1] == args[len(args) - 1] or args[i][0] == '-':
                        raise Exception("Wrong prefix name!")
                    state["prefix"] = args[i]
                if args[i] == '-b':
                    state["buffer"] = True
                if args[i] == '-o':
                    state["browser"] = True
                i += 1
        state["container"] = container
        container = state["prefix"] + state["delimiter"] + container
    except Exception as e:
        print(e)
        exit()


prepare_data()

print(container)
