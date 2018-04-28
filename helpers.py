class PrintForDebug:

    def __init__(self, debug):
        self.debug = debug   

    def __call__(self, *args, **kwargs):
        if self.debug:
            print(*args, **kwargs)
