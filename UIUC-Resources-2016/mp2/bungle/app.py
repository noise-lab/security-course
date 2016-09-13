import sys, os

# Change working directory so relative paths (and template lookup) work again
sys.path = ['/home/cs461/mp2/bungle/'] + sys.path
os.chdir(os.path.dirname(__file__))

import bottle

import project2

application = bottle.default_app()
