import sys

# Workaround for the "print is a keyword/function" Python 2/3 dilemma
# and a fallback for mod_wsgi (resticts stdout/err attribute access)

try:
    _stdout, _stderr = sys.stdout.write, sys.stderr.write
except IOError:
    _stdout = lambda x: sys.stdout.write(x)
    _stderr = lambda x: sys.stderr.write(x)

from . import __version__, __package__


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
    opt('-b', '--bind', metavar='ip:port', help='bind address, default localhost:8888')
    opt('-s', '--server', metavar='SERVER', help='user SERVER as backend')
    opt('-C', '--param', metavar='NAME=VALUE', help='overwrite config value')
    opt('--debug', help='run server in debug mode')
    opt('--reload', help='auto reload on file changes')

    # 过滤掉第一个入参
    arggs_namespace = parser.parse_args(args[1:])
    return parser, arggs_namespace


def _pre_proccess(argv):
    '''
        处理命令行输入, 入参预处理
    :param argv: sys.argv
    :return:
    '''

    parse, args_namespace = _cli_parse(argv)

    # 读取版本信息
    if args_namespace.version:
        _get_version()

    # 拼装 server:port
    host, port = 'localhost', '8888'
    if args_namespace.bind:
        host, port = _parse_server_port(args_namespace)

    sys.path.insert(0, '.')
    sys.modules.setdefault(__package__, sys.modules['__main__'])


def _parse_server_port(args):
    '''
        获取 ip 与端口号
    :param args:
    :return:
    '''
    ip, port = args.bind.split(':')

    # 检查 ip 的合规性
    def validate_ip_address(ip):
        from ipaddress import ip_address
        try:
            ip_address(ip)
        except ValueError:
            _stderr('Not Legal IPV4 address: %s' % ip)
            sys.exit(1)

    def validate_port(port):
        port = int(port)
        if port < 0 or port > 65535:
            _stderr('Port %d is not legal' % port)

    validate_ip_address(ip)
    validate_port(port)
    return ip, port


def _get_version():
    '''
        获取版本信息
    :return:
    '''
    _stdout('%s version: %s\n' % (__package__, __version__))
    sys.exit(0)
