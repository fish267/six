import sys


class Pro():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._value = None

    @property
    def fullname(self):
        return 'Fullname is %s %s' % (self.last_name, self.first_name)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


def logger(fn):
    def wrapper():
        print('%s starts to executing' % fn.__name__)
        fn()
        print('%s finished executing' % fn.__name__)

    return wrapper


def load(target, **namespace):
    module, target = target.split(":", 1) if ':' in target else (target, None)
    if module not in sys.modules: __import__(module)
    if not target: return sys.modules[module]
    if target.isalnum(): return getattr(sys.modules[module], target)
    package_name = module.split('.')[0]
    namespace[package_name] = sys.modules[package_name]
    print('Start to load: \nmodule:%s\npackage_name: %s\nnamespace: %s' % (module, package_name, namespace))
    object = eval('%s.%s' % (module, target), namespace)
    print(object)
    return object


fp = load('six_web.cli:_get_version')
fp()
