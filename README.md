*Direct graph tracer<br>
    A directed graph usage<br>
*Usage<br>
	Command syntax:<br>
		GraphTracer.py <graph_input_file> <commands_input_file><br>
	Extended syntax:<br>
		{path_to_Python_interpreter} "{path_to_project}GraphTracer.py " "{path_to_project}Graph.txt" "{path_to_project}Commands.txt"<br>
*Available Commands<br>
	getRoutCost  - Returns cost of provided rout<br>
	tripsCount   - Returns a number of trips starting at startVertex and ending at endVertex with a maximum of hoopsCount stops<br>
	tripsCountEQ - Returns a number of trips starting at startVertex and ending at endVertex with exactly hoopsCount stops<br>
	shortRout    - Returns a length of the shortest route from routStar to routEnd (based on Dijkstra's algorithm)<br>
