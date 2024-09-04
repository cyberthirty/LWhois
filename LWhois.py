#!/bin/python3

import whois
import argparse
import sys
from pprint import pprint

def whoisLookup(domain):
    try:
        hostInfo = whois.whois(domain)
        pprint(hostInfo)
    except Exception as e:
        print(f"Error: {e}")

def runWhois():
    parser = argparse.ArgumentParser(description="WHOIS lookup.")
    parser.add_argument('-d', '--domain', type=str, required=True, help="The domain to lookup")

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    whoisLookup(args.domain)

if __name__ == "__main__":
    runWhois()
