#!/usr/bin/python3

from sys import argv
import subprocess


def prepare_data():
    global args
    global container
    global state
    if argv[0].find("python") == -1:
        args = argv[1:]
    else:
        args = argv[2:]
    state = {
        "browser": False,
        "prefix": "",
        "buffer": False,
        "server": "localhost",
        "delimiter": "-",
        "container": ""
    }
    try:
        if len(args) == 0 or args[0][0] == '-':
            raise Exception("Enter name of container!")
        container = args.pop(0)

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
port = subprocess.Popen("docker port " + container, shell=True, stdout=subprocess.PIPE)\
    .stdout.read().decode("utf-8").strip()

print(port)
