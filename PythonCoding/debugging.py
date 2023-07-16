###https://www.hackerrank.com/challenges/default-arguments/problem?isFullScreen=true

class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=EvenStream()):
    if isinstance(stream, EvenStream):
        stream = EvenStream()
    if isinstance(stream, OddStream):
        stream = OddStream()  
    for _ in range(n):
        print(stream.get_next())

