import urllib.request
import re
import sys


def retrieveIP():
    url = "http://checkip.dyndns.org"
    query = urllib.request.urlopen(url).read()
    return str(query)


def parseIP(query):
    ipNumberPattern = "(25[0-4]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    ipRE = "{0}.{1}.{2}.{3}".format(ipNumberPattern,
                                    ipNumberPattern,
                                    ipNumberPattern,
                                    ipNumberPattern)
    ipPattern = re.compile(ipRE)
    ip = re.search(ipPattern, query)
    return ip.group()


def main():
    print('Finding IP address...')
    try:
        myIP = parseIP(retrieveIP())
        print(myIP)
    except:
        print('Unable to connect.')
    input()
    sys.exit()


if __name__ == "__main__":
    main()
