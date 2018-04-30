*Direct graph tracer
    A directed graph usage

*Usage
    Command syntax:
	GraphTracer.py <graph_input_file> <commands_input_file>
    Extended syntax:
	{path_to_Python_interpreter} "{path_to_project}GraphTracer.py " "{path_to_project}Graph.txt" "{path_to_project}Commands.txt"
*Available Commands
    getRoutCost  - Returns cost of provided rout
    tripsCount   - Returns a number of trips starting at startVertex and ending at endVertex with a maximum of hoopsCount stops
    tripsCountEQ - Returns a number of trips starting at startVertex and ending at endVertex with exactly hoopsCount stops
    shortRout    - Returns a length of the shortest route from routStar to routEnd (based on Dijkstra's algorithm)