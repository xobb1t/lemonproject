import sys
from optparse import OptionParser
from lemonproject import templates


available_templates = {}
for name in dir(templates):
    if name.startswith('_'):
        continue
    attr = getattr(templates, name)
    try:
        is_template = issubclass(attr, templates.Base)
    except TypeError:
        continue
    if is_template and attr is not templates.Base:
        available_templates[name.lower()] = attr


def print_list(option, opt, value, parser):
    for name in available_templates:
        print(' - %s' % name)
    sys.exit(0)


def run():
    parser = OptionParser(usage='%prog [options] template [options] dst_dir')
    parser.add_option('-l', '--list', action='callback', callback=print_list,
                      help='show available templates and exit')
    parser.disable_interspersed_args()
    options, args = parser.parse_args()
    if not args:
        parser.error("project template wasn't specified")
    name = args.pop(0)
    if name not in available_templates:
        parser.error("template %s wasn't found" % name)
    template = available_templates[name]
    template.cmd(args)
