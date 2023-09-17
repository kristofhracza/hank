import requests,sys,time,json
from optparse import OptionParser

# Help
def usage():
    print("""
        Usage: bino.py  -u [username] -f [file name]
        
        REQUIRED:
        -u or --username
        
        OPTIONAL:
        -f or --file:\tOutput file
        -v or --verbose:\tVerbose output
    """)
    sys.exit()

def make():
    parser = OptionParser()
    parser.set_conflict_handler("resolve")
    parser.add_option("-u", "--username",dest="uname")
    parser.add_option("-h", "--help", dest="help", action="store_true")
    parser.add_option("-v", "--verbose", dest="verbose", action="store_true")
    parser.add_option("-f", "--file", dest="fileName")
    (options, args) = parser.parse_args()

    if options.uname == None or options.help:
        usage()
    if options.uname:
        options.help = None

    with open("sites.json") as config:
        sites = json.load(config)
    return sites,options