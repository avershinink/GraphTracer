class graphParseError(BaseException):
    """
    Problem parsing a graph.
    """
    def __init__(self, filename, record):
        print('Grapt parse error: \n\t in file:[{0}]\n\t record: [{1}]'.format(filename, record))

class aliasNotFound(BaseException):
    """
    A vertex alias not found.
    """
    def __init__(self, alias):
        print('Requested [{0}] alias not found'.format(alias)) 
