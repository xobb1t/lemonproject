import os
import sys
from django.utils.importlib import import_module


apps_root = os.path.join(os.path.dirname(__file__), '..', 'apps')
apps_root = os.path.normpath(os.path.abspath(apps_root))
if apps_root not in sys.path:
    sys.path.insert(0, apps_root)


environment = os.environ.get('LEMON_ENV', 'development')
try:
    settings_module = import_module('.%s' % environment, 'settings')
except ImportError:
    sys.stderr.write("Error: Can't find the file '%s.py' in the directory "
                     "containing %r.\n" % (environment, __file__))
    sys.exit(1)


for name in [n for n in dir(settings_module) if not n.startswith('_')]:
    globals()[name] = getattr(settings_module, name)
