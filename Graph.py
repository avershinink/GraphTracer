from sys import maxsize
from CustomErorrs import graphParseError

class Graph:
    """
    Class for graph represention 
    """
    graphDelim = ', '
    AdjacencyMatrix = [[]]
    verticesNames = {}
    verticesCount = 0
    __edgeRecordMinLenght = 3

    def loadFromFile(self, filePath):
        """
        Loading a graph from input file
        The input data is in the following format:
        <start_vertex><end_vertex><cost>
        <start_vertex>  -> character (alias of start vertex)
        <end_vertex>    -> character (alias of end vertex)
        <cost>          -> positive integer
        """
        with open(filePath) as file:
            graphRecord = file.readline()
        self.loadFromString(graphRecord,filePath)

    def loadFromString(self, graphStringRepresentation, source = 'string'):
        """
        Loading a graph from string
        The input data is in the following format:
        <start_vertex><end_vertex><cost>
        <start_vertex>  -> character (alias of start vertex)
        <end_vertex>    -> character (alias of end vertex)
        <cost>          -> positive integer
        >>> g = Graph()
        >>> g.loadFromString('AB1, BC2')
        >>> print(g)
        [[2147483647, 1, 2147483647], [2147483647, 2147483647, 2], [2147483647, 2147483647, 2147483647]]
        """
        edges = graphStringRepresentation.upper().split(self.graphDelim)
        i = 0
        for edge in edges:
            if len(edge) >= self.__edgeRecordMinLenght:
                if edge[0] not in self.verticesNames:
                    self.verticesNames[edge[0]] = i
                    i+=1
                if edge[1] not in self.verticesNames:
                    self.verticesNames[edge[1]] = i
                    i+=1
            else:
                raise graphParseError(source, edge)
        self.verticesCount = len(self.verticesNames)

        gLen = len(self.verticesNames)
        self.AdjacencyMatrix = [[maxsize for x in range(gLen)] for y in range(gLen)] 
        for edge in edges:
            try:
                self.AdjacencyMatrix[self.verticesNames[edge[0]]][self.verticesNames[edge[1]]] = int(''.join(edge[2:]))
            except ValueError:
                raise graphParseError(source, edge)

    def __str__(self):
        return str(self.AdjacencyMatrix)

if __name__ == "__main__":
    
    import doctest
    doctest.testmod()
