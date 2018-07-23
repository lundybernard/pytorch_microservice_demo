from inspect import getdoc
from docopt import docopt

from compose.cli.main import TopLevelCommand, project_from_options


def default_opts(self, command):
    '''given a docker-compose command
    return its default options
    '''
    cmd_help = getdoc(getattr(TopLevelCommand, command))
    return docopt(cmd_help, [])


class DockerCompose(object):

    def __init__(self, path='./'):
        self.project = project_from_options(path, self.options)
        self.cli = TopLevelCommand(self.project)

    def up(self, **kwargs):
        self.cli.up(self.options)
