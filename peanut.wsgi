import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/peanutbutteroneverything.com/public_html')

from peanut import app as application
