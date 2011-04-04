import os
import skeleton


class Var(skeleton.Var):

    default = None
    intro = None

    def __init__(self):
        pass


class ProjectName(Var):

    name = 'project_name'
    display_name = 'project name'
    description = 'if not set, destination directory name will be used'


class TimeZone(Var):

    name = 'time_zone'
    display_name = 'time zone'
    full_description = 'local time zone for this installation'
    default = os.environ.get('LEMONPROJECT_TIME_ZONE', 'America/Chicago')
    prompt = 'Enter time zone [%s]: ' % default


class LanguageCode(Var):

    name = 'language_code'
    display_name = 'language code'
    full_description = 'language code for this installation'
    default = os.environ.get('LEMONPROJECT_LANGUAGE_CODE', 'en-us')
    prompt = 'Enter language code [%s]: ' % default
