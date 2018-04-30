#! /usr/bin/env python3
"""
Main entry point for GraphTracer application.
Initiate from the terminal by typing:
    % python GraphTracer.py
Python 3.* must be installed on your system.
"""
import sys
from os.path import isfile
from Graph import Graph
from CustomErorrs import aliasNotFound

class GraphWorker:
    routSplitterChar = '-'
    def __init__(self, inputFile):
        self.Graph = Graph()
        self.Graph.loadFromFile(inputFile)

    def getRoutCost(self, routLine):
        """
        Returns cost of provided rout
        The input data is in the following format:
        <vertex1>-<vertex2>-...-<vertexN>
        <vertexN>  -> character (alias of vertex)
        "-"        -> is delimiter character
        >>> gw = GraphWorker('GraphTest.txt')
        >>> gw.getRoutCost('A-B-C')
        9
        >>> graphW.getRoutCost('A-D')
        5
        >>> graphW.getRoutCost('A-D-C')
        13
        >>> graphW.getRoutCost('A-E-B-C-D')
        22
        >>> graphW.getRoutCost('A-E-D')
        NO SUCH ROUTE
        """
        cost = 0
        rout = routLine.split(self.routSplitterChar)
        am = self.Graph.AdjacencyMatrix
        vn = self.Graph.verticesNames
        if(len(rout) >= 2):
            for index in range(len(rout)-1):
                if rout[index] in vn:
                    vertexStart = vn[ rout[ index    ]]
                else:
                     raise aliasNotFound(rout[index])
                if rout[index + 1] in vn:
                    vertexEnd   = vn[ rout[ index + 1]]
                else:
                     raise aliasNotFound(rout[index + 1])
                edgeCost = am[vertexStart][vertexEnd]
                if(edgeCost == sys.maxsize):
                    return 'NO SUCH ROUTE'
                cost += edgeCost
        #print('{0} = {1}'.format(routLine,cost))
        return cost

    def tripsCount(self, startVertex, endVertex, hoopsCount):
        """
        Returns a number of trips starting at startVertex and ending at endVertex with a maximum of hoopsCount stops
        >>> gw = GraphWorker('GraphTest.txt')
        >>> gw.tripsCount('C','C',3)
        2
        """
        self.HC = 0
        self.maxHoopsCount = hoopsCount
        routStart = self.Graph.verticesNames[startVertex]
        for vertex in range(len(self.Graph.AdjacencyMatrix[routStart])):
            if(self.Graph.AdjacencyMatrix[routStart][vertex] != sys.maxsize and vertex != routStart):
                self.__tripsCount(vertex, self.Graph.verticesNames[endVertex], 0)
        result = self.HC
        del(self.HC)
        del(self.maxHoopsCount)
        #print('Number of routs from {0} to {1} with no more than {2} stops = {3}'.format(startVertex, endVertex, result))
        return result

    def __tripsCount(self, routStart, routEnd, hoop):
        if(hoop >= self.maxHoopsCount):
            return
        if(routStart == routEnd):
            self.HC += 1
            return 
        hoop += 1
        for edgeNum in range(len(self.Graph.AdjacencyMatrix[routStart])):
            if(self.Graph.AdjacencyMatrix[routStart][edgeNum] != sys.maxsize):
                self.__tripsCount(edgeNum, routEnd, hoop)

    def tripsCountEQ(self, startVertex, endVertex, hoopsCount):
        """
        Returns a number of trips starting at startVertex and ending at endVertex with exactly hoopsCount stops
        >>> gw = GraphWorker('GraphTest.txt')
        >>> gw.tripsCountEQ('A','C',4)
        3
        """
        self.HC = 0
        self.reqHoopsCount = hoopsCount
        routStart = self.Graph.verticesNames[startVertex]
        for vertex in range(len(self.Graph.AdjacencyMatrix[routStart])):
            if(self.Graph.AdjacencyMatrix[routStart][vertex] != sys.maxsize and vertex != routStart):
                self.__tripsCountEQ(vertex, self.Graph.verticesNames[endVertex], 0)
        result = self.HC
        del(self.HC)
        del(self.reqHoopsCount)
        #print('Number of routs from {0} to {1} with no more than {2} stops = {3}'.format(startVertex, endVertex, result))
        return result

    def __tripsCountEQ(self, routStart, routEnd, hoop):
        if(hoop >= self.reqHoopsCount):
            return
        if(routStart == routEnd and hoop == self.reqHoopsCount-1):
            self.HC += 1
            return
        hoop += 1
        for edgeNum in range(len(self.Graph.AdjacencyMatrix[routStart])):
            if(self.Graph.AdjacencyMatrix[routStart][edgeNum] != sys.maxsize):
                self.__tripsCountEQ(edgeNum, routEnd, hoop)

    def tripsDistLT(self, startVertex, endVertex, maxDist):
        """
        Returns a number of different routes from startVertex to endVertex with a distance of less than maxDist
        >>> gw = GraphWorker('GraphTest.txt')
        >>> gw.tripsDistLT('C','C',30)
        7
        """
        self.routsCount = 0
        self.maxDist = maxDist
        routStart = self.Graph.verticesNames[startVertex]
        routEnd = self.Graph.verticesNames[endVertex]
        self.__tripsDistLT(routStart, routEnd)
        result = self.routsCount
        del(self.routsCount)
        del(self.maxDist)
        #print('Number of routs from {0} to {1} with no more than {2} stops = {3}'.format(startVertex, endVertex, result))
        return result

    def __tripsDistLT(self, routStart, routEnd, dist = 0):
        if(dist >= self.maxDist):
            return
        if(routStart == routEnd and dist != 0):
            self.routsCount += 1
        for edgeNum in range(self.Graph.verticesCount):
            if(self.Graph.AdjacencyMatrix[routStart][edgeNum] != sys.maxsize):
                self.__tripsDistLT(edgeNum, routEnd, dist+self.Graph.AdjacencyMatrix[routStart][edgeNum])

    def shortRout(self, routStar, routEnd):
        """
        Returns a length of the shortest route from routStar to routEnd (based on Dijkstra's algorithm)
        >>> gw = GraphWorker('GraphTest.txt')
        >>> gw.shortRout('A','C')
        9
        >>> gw.shortRout('B','B')
        9
        """
        routStartIndex = self.Graph.verticesNames[routStar]
        vn = self.Graph.verticesNames
        am = self.Graph.AdjacencyMatrix
        verticesCount = len(vn)
        distance = [am[routStartIndex][x] for x in range(verticesCount)]
        searchVertices = [x for x in range(verticesCount)]
        path = []
        while len(searchVertices) > 0:
            minDistVrtx = 0
            minDist = sys.maxsize
            for l in range(verticesCount):
                if(minDist>=distance[l] and l not in path):
                    minDist = distance[l]
                    minDistVrtx = l
            path.append(minDistVrtx)

            searchVertices.remove(minDistVrtx)
            for nbr in range(verticesCount):
                if(nbr in searchVertices):
                    distance[nbr] = min(distance[nbr], distance[minDistVrtx]+am[minDistVrtx][nbr])
        #print('The length of the shortest route from {0} to {1} = {2}'.format(routStar, routEnd, distance[vn[routEnd]]))
        if(distance[vn[routEnd]] != sys.maxsize):
            return distance[vn[routEnd]]
        else:
            return 'NO SUCH ROUTE'

if(__name__ == '__main__'):
    #import doctest
    #doctest.testmod()

    # Read commands
    fileCmds = []
    graphWorkerCreated = False
    if len(sys.argv) > 2:
        try:
            if(isfile(sys.argv[1])):
                gw = GraphWorker(sys.argv[1])
                graphWorkerCreated = True
        except IOError:
            print('Could not open [{0}] file with graph''s data.'.format(sys.argv[1]) )

        try:
            if(isfile(sys.argv[2])):
                fileCmds = open(sys.argv[2]).readlines()
        except IOError:
            print('Could not open [{0}] file with commands.'.format(sys.argv[2]) )

    # Process input commands
    if(graphWorkerCreated and fileCmds):
        commNum = 1
        outputTemplate = 'Output#{0}: {1}'
        for line in fileCmds:
            line = line.strip()
            params = line.split(' : ')
            if(len(params) == 2):
                subParamDelim = ','
                if line.startswith('getRoutCost : '):
                    result = gw.getRoutCost(params[1])
                elif line.startswith('tripsCount : '):
                    workerParams = params[1].split(subParamDelim)
                    if(len(workerParams) == 3):
                        result = gw.tripsCount(workerParams[0],workerParams[1],int(workerParams[2]))
                elif line.startswith('tripsCountEQ : '):
                    workerParams = params[1].split(subParamDelim)
                    if(len(workerParams) == 3):
                        result = gw.tripsCountEQ (workerParams[0],workerParams[1],int(workerParams[2]))
                elif line.startswith('shortRout : '):
                    workerParams = params[1].split(subParamDelim)
                    if(len(workerParams) == 2):
                        result = gw.shortRout(workerParams[0],workerParams[1])
                elif line.startswith('tripsDistLT : '):
                    workerParams = params[1].split(subParamDelim)
                    if(len(workerParams) == 3):
                        result = gw.tripsDistLT(workerParams[0],workerParams[1],int(workerParams[2]))
                else:
                    result = 'ERROR! Unsupported command found: {0}'.format(line)
            print(outputTemplate.format(commNum,result))
            commNum += 1
    else:
        print("GraphTracer.py %FileNameWithGraph% %FileNameWithCommands%")
