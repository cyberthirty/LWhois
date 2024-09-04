#!/bin/python3

import whois
import argparse
import sys
from pprint import pprint
import os

def clear():
 
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

def banner():
    blink = "\033[5m"
    blue = "\033[34m"
    reset ="\033[0m"

    banner = r"""
                     _ __        ___           _
                    | |\ \      / / |__   ___ (_)___   _ __  _   _
                    | | \ \ /\ / /| '_ \ / _ \| / __| | '_ \| | | |
                    | |__\ V  V / | | | | (_) | \__ \_| |_) | |_| |
                    |_____\_/\_/  |_| |_|\___/|_|___(_) .__/ \__, |
                                                      |_|    |___/
                                   by cyberthirty
    """
    print(f"{blue}{blink}{banner}{reset}")


def whoisLookup(domain):
    try:
        hostInfo = whois.whois(domain)
        pprint(hostInfo)
    except Exception as e:
        print(f"Error: {e}")

def runWhois():
    clear()
    banner()
    parser = argparse.ArgumentParser(description="WHOIS lookup.")
    parser.add_argument('-d', '--domain', type=str, required=True, help="The domain to lookup")

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    whoisLookup(args.domain)

if __name__ == "__main__":
    runWhois()
