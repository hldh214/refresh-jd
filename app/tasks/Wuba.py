''' Task Module Description '''
from masonite.scheduler.Task import Task


class Wuba(Task):
    """ Task description """

    def __init__(self):
        super().__init__()

    def handle(self):
        pass
