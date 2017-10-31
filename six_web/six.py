import sys

# Workaround for the "print is a keyword/function" Python 2/3 dilemma
# and a fallback for mod_wsgi (resticts stdout/err attribute access)

try:
    _stdout, _stderr = sys.stdout.write, sys.stderr.write
except IOError:
    _stdout = lambda x: sys.stdout.write(x)
    _stderr = lambda x: sys.stderr.write(x)


def add(a, b):
    return a + b


def haha():
    print("xx")


class Six(object):
    def __init__(self):
        pass


def _cli_parse(args):
    '''
        python -m six_web 输出的帮助文档
    :param args: 参数输入
    :return:
    '''
    from argparse import ArgumentParser
    parser = ArgumentParser(prog=args[0], usage="%(prog)s [options] package.moudle:app",
                            epilog='Life is short, love python!',
                            description='Coding to change the world for better.')
    opt = parser.add_argument
    opt('-v', '--version', action='store_true', help='show version number')
    opt('-b', '--bind', metavar='ip:port', help='bind address, default localhost:8080')
    opt('-s', '--server', metavar='SERVER', help='user SERVER as backend')
    opt('-C', '--param', metavar='NAME=VALUE', help='overwrite config value')
    opt('--debug', help='run server in debug mode')
    opt('--reload', help='auto reload on file changes')

    # 过滤掉第一个入参
    arggs_namespace = parser.parse_args(args[1:])
    return parser, arggs_namespace


def _main(argv):
    '''
        处理命令行输入, 入参预处理
    :param argv: sys.argv
    :return:
    '''

    from . import __version__, __package__
    parse, args_namespace = _cli_parse(argv)

    # 读取版本信息
    if args_namespace.version:
        _stdout('%s version: %s\n' % (__package__, __version__))
        sys.exit(0)
    sys.path.insert(0, '.')
    sys.modules.setdefault(__package__, sys.modules['__main__'])


if __name__ == '__main__':
    test_args = sys.argv
    test_args.append('--version')

    _main(test_args)
