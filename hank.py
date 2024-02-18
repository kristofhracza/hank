from optparse import OptionParser
from libs.search_engine import Search_Engine,banner,usage
from libs.sites import Binoculars

# Get terminal arguments
def resolve_options():
    parser = OptionParser()
    parser.set_conflict_handler("resolve")
    parser.add_option("-u", "--username",dest="user_name")
    parser.add_option("-r", "--real-name",dest="real_name")
    parser.add_option("-c", "--count",dest="count")

    parser.add_option("-h", "--help", dest="help", action="store_true")
    (options, args) = parser.parse_args()

    # Check for parameter presence
    if options.user_name and options.real_name:
        return options
    else:
        usage()


# Entry of program
if __name__ == "__main__":
    print(banner)

    OPTIONS = resolve_options()

    # Username lookup
    bino = Binoculars(OPTIONS)
    bino.run()

    # Search engine looup
    se = Search_Engine(OPTIONS)
    se.clean_and_run()