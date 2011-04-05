import os
from random import choice
from skeleton import Skeleton, Var
from .variables import ProjectName, TimeZone, LanguageCode


class Base(Skeleton):

    def configure_parser(self):
        parser = super(Base, self).configure_parser()
        parser.usage = '%%prog [options] %s [options] dst_dir'
        parser.usage %= self.__class__.__name__.lower()
        return parser

    def run(self, dst_dir, run_dry=False):
        self['project_name'] = self.get_project_name(dst_dir)
        self['secret_key'] = self.generate_secret_key()
        return super(Base, self).run(dst_dir, run_dry)

    def get_project_name(self, dst_dir):
        return os.path.basename(os.path.abspath(dst_dir))

    def generate_secret_key(self):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        return ''.join(choice(chars) for i in range(50))


class Default(Base):

    src = 'templates/default'
    variables = [ProjectName(), TimeZone(), LanguageCode()]
