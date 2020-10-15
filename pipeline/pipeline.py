import time

class Pipeline():
    def __init__(self, sink):
        self.__sink = sink
        
    def process(self, element):
        return element
    
    def pipe(self, element):
        c = type(self).__name__
        if 'step' not in element:
            element['step'] = list()
        element['step'].append(c)
        element = self.process(element)

        if element == None:
            # done
            return

        if 'stamp' not in element:
            element['stamp'] = dict()
        element['stamp'][c] = time.perf_counter()

        if (self.__sink):
            self.__sink.pipe(element)
