# pip installs packages other people wrote. You run it in the terminal, not in Python:
#
#   pip install requests          <- install
#   pip install -U requests       <- upgrade
#   pip uninstall requests        <- remove
#   pip show requests             <- info about it
#
# Then you just import it like any module.

try:
    import requests
    print("requests is installed! version:", requests.__version__)
except ImportError:
    print("requests isn't installed yet. Run: pip install requests")
