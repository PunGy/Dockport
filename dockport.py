#!/usr/bin/python3

from sys import argv
import subprocess
import pyperclip

# CONFIG
keys = {
    "browser": False,
    "buffer": False
}
abbreviations = {
    "pma": "phpmyadmin",
    "serve": "nginx"
}
config = {
    "server": "localhost",
    "delimiter": "-",
    "envFileName": ".env",
    "envNameContainer": "COMPOSE_PROJECT_NAME",
    "env": False,

    # USE BY PROGRAM
    "container": "",
    "prefix": ""
}
NOT_FOUND = -1
# CONFIG/


# FUNCTIONS
def exec_keys():
    global keys
    if keys["browser"]:
        subprocess.call("google-chrome http://" + url, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if keys["buffer"]:
        pyperclip.copy(url)


def get_env():
    try:
        env = open(config["envFileName"])
        prefix = False
    except FileNotFoundError:
        return False
    for line in env:
        if line.find(config["envNameContainer"]) != NOT_FOUND:
            prefix = line.split('=')[1].strip('\n')
    return prefix


def prepare_data():
    global args
    global container
    global config
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
                    i += 1
                    if get_env() is not False:
                        config["prefix"] = prefix
                        continue

                    if args[i - 1] == args[len(args) - 1] or args[i][0] == '-':
                        raise Exception("Wrong prefix name!")
                    config["prefix"] = args[i]
                    continue

                if args[i] == '-b':
                    keys["buffer"] = True
                if args[i] == '-o':
                    keys["browser"] = True
                i += 1

        config["prefix"] = config["prefix"] + config["delimiter"] if len(config["prefix"]) != 0 else ""
        config["container"] = container
        container = config["prefix"] + container
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
    url = config["server"] + ":" + port
    exec_keys()
    print(url)
except Exception as msg:
    print(msg)
    exit()
