#!/usr/bin/env python3

from lef import Extension, EventType

client = None

def handler(event):
    print(event)

def main():
    extension = Extension()
    extension.register([EventType.INVOKE], handler)

if __name__ == "__main__":
    main()
