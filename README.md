*Direct graph tracer<br>
&nbsp;&nbsp;&nbsp;&nbsp;A directed graph usage<br>
*Usage<br>
&nbsp;&nbsp;&nbsp;&nbsp;Command syntax:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GraphTracer.py <graph_input_file> <commands_input_file><br>
&nbsp;&nbsp;&nbsp;&nbsp;Extended syntax:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{path_to_Python_interpreter} "{path_to_project}GraphTracer.py " "{path_to_project}Graph.txt" "{path_to_project}Commands.txt"<br>
*Available Commands<br>
&nbsp;&nbsp;&nbsp;&nbsp;getRoutCost  - Returns cost of provided rout<br>
&nbsp;&nbsp;&nbsp;&nbsp;tripsCount   - Returns a number of trips starting at startVertex and ending at endVertex with a maximum of hoopsCount stops<br>
&nbsp;&nbsp;&nbsp;&nbsp;tripsCountEQ - Returns a number of trips starting at startVertex and ending at endVertex with exactly hoopsCount stops<br>
&nbsp;&nbsp;&nbsp;&nbsp;shortRout    - Returns a length of the shortest route from routStar to routEnd (based on Dijkstra's algorithm)<br>
