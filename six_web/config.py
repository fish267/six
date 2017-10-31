def load(target, **namespace):
    '''
    import a module

    '''
    pass


class CallClass():
    def __init__(self, value):
        self.value = value

    def __call__(self, *args, **kwargs):
        self.value = self.value ** 3
