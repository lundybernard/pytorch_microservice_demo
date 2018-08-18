import argparse
import logging
from logging.config import dictConfig

from .services import cuda_is_available


# === LOGGING === #
logging_config = dict(
    version=1,
    formatters={
        'f': {'format':
              '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'},
        'thread_formatter': {
            'format':
            '%(asctime)s %(threadName)-12s %(levelname)-8s %(message)s'
        }
    },
    handlers={
        'h': {
            'class': 'logging.StreamHandler',
            'formatter': 'f'
        },
        'thread_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'thread_formatter'
        }
    },
    loggers={
        'root': {
            'handlers': ['h'],
            'level': logging.DEBUG
        },
        'mod': {
            'handlers': ['h'],
            'level': logging.DEBUG
        },
        'thread': {
            'handlers': ['thread_handler'],
            'level': logging.DEBUG
        }
    }
)


dictConfig(logging_config)
log = logging.getLogger('root')


class PytorchCLI(object):

    def __init__(self):
        p = argparse.ArgumentParser(
            description='Utility for executing various IPcenter tasks',
            usage='ipcenterutil.py [<args>] <command>'
        )

        p.add_argument(
            '-v', '--verbose',
            help='enable INFO output',
            action='store_const',
            dest='loglevel',
            const=logging.INFO
        )
        p.add_argument(
            '--debug',
            help='enable DEBUG output',
            action='store_const',
            dest='loglevel',
            const=logging.DEBUG,
        )

        # Add a subparser to handle sub-commands
        commands = p.add_subparsers(
            dest='command',
            title='commands',
            description='valid commands',
        )
        # hello args
        hello = commands.add_parser(
            'hello',
            description='execute command hello',
            help='for details use hello --help',
        )
        hello.set_defaults(func=self.hello)

        # cuda_is_available args
        cuda_is_available = commands.add_parser(
            'cuda_is_available',
            description='execute command cuda_is_available',
            help='for details use cuda_is_available --help'
        )
        cuda_is_available.set_defaults(func=self.cuda_is_available)

        # start args
        start = commands.add_parser(
            'start',
            description='start the web server',
            help='for details use start --help',
        )
        start.set_defaults(func=self.start)
        start.add_argument(
            '-H', '--host', dest='host',
            default='0.0.0.0',
            #required=True,
            help='host ip on which the service will be made available',
        )
        start.add_argument(
            '-P', '--port', dest='port',
            default='5000',
            help='port on which the service will be made available'
        )
        start.add_argument(
            '-d', '--debug', dest='debug',
            default=True,
            help='run web service with debug level output'
        )

        # test args
        test = commands.add_parser(
            'test',
            description='run functional tests',
            help='for details use test --help'
        )
        test.set_defaults(func=self.test)
        test.add_argument(
            '-H', '--host', dest='host',
            default='0.0.0.0',
            help='host ip on which the service is running',
        )
        test.add_argument(
            '-P', '--port', dest='port',
            default='5000',
            help='port on which the service is running'
        )

        sub1 = commands.add_parser(
            'sub1',
            description='execute command sub1',
            help='for details use sub1 --help'
        )
        sub1.set_defaults(func=self.sub1)

        sub1.add_argument(
            '-a', '--argument',
            dest='argument',
            default=None,
            help='tell me what arg1 does',
        )

        # get only the first command in args
        args = p.parse_args()
        self.set_log_level(args)
        # execute function set for parsed command
        args.func(args)

    def set_log_level(self, args):
        if args.loglevel:
            log.setLevel(args.loglevel)
        else:
            log.setLevel(logging.ERROR)

    def start(self, args):
        from .pytorch_server import app
        #app.run(host="0.0.0.0", debug=True)
        app.run(host=args.host, port=args.port, debug=args.debug)

    def test(self, args):
        import unittest
        loader = unittest.TestLoader()
        suite = loader.discover('./pytorch_server/tests')
        runner = unittest.TextTestRunner()
        runner.run(suite)

    def cuda_is_available(self, args):
        print(cuda_is_available())

    def hello(self, args):
        print('Hello World!\n')

    def sub1(self, args):
        print('sub1 example command')
