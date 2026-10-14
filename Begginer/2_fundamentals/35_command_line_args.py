# You can pass values when running a script from the terminal, like:
#   python 35_command_line_args.py Roger
# sys.argv is a list of what was typed. argv[0] is the file name itself.

import sys

if len(sys.argv) > 1:
    print("Hello " + sys.argv[1])
else:
    print("No name given. Try: python 35_command_line_args.py Roger")

# For anything fancier, the argparse module is the friendlier option.
