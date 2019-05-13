from lgraph import LGraph

# # Creating some L-graphs and saving them
# lg = LGraph(3)
#
# lg.add_edge(lg.initial_main.name, '1')
# lg.add_edge('1', '2', label='b', round_trace=')', square_trace='[')
# lg.add_edge('2', '3', label='c', square_trace=']')
# lg.add_edge('3', lg.final_main.name)
#
# lg.add_edge('1', '1', label='a', round_trace='(')
# lg.add_edge('2', '2', label='b', round_trace=')', square_trace='[')
# lg.add_edge('3', '3', label='c', square_trace=']')
#
# lg.save('graph_examples/a^n_b^n_c^n')
#
# lg = LGraph(2)
#
# lg.add_edge(lg.initial_main.name, '1')
# lg.add_edge('1', '2')
# lg.add_edge('2', lg.final_main.name)
#
# lg.add_edge('1', '1', label='a')
# lg.add_edge('2', '2', label='b')
#
# lg.save('graph_examples/a^n_b^k')
#
# lg = LGraph(2)
#
# lg.add_edge(lg.initial_main.name, '1')
# lg.add_edge('1', '2', label='b', round_trace=')')
# lg.add_edge('2', lg.final_main.name)
#
# lg.add_edge('1', '1', label='a', round_trace='(')
# lg.add_edge('2', '2', label='b', round_trace=')')
#
# lg.save('graph_examples/a^n_b^n')

# lg = LGraph()
#
# lg.add_vertex('A')
# lg.add_vertex('B')
# lg.add_vertex('C')
#
# lg.add_edge(lg.initial_main.name, 'A')
# lg.add_edge('A', 'B', label='b', round_trace=')', square_trace='[')
# lg.add_edge('B', 'C', label='c', square_trace=']')
# lg.add_edge('C', lg.final_main.name)
#
# lg.add_edge('A', 'A', label='a', round_trace='(')
# lg.add_edge('B', 'B', label='b', round_trace=')', square_trace='[')
# lg.add_edge('C', 'C', label='c', square_trace=']')
#
# lg.save('graph_examples/left')
#
# lg = LGraph()
#
# lg.add_vertex('A')
# lg.add_vertex('B')
# lg.add_vertex('C')
#
# lg.add_edge(lg.initial_main.name, 'A')
# lg.add_edge('A', 'B', label='c', round_trace='(')
# lg.add_edge('B', 'C', label='a', square_trace='[')
# lg.add_edge('C', lg.final_main.name)
#
# lg.add_edge('A', 'A', label='c', round_trace='(')
# lg.add_edge('B', 'B', label='a', square_trace='[')
# lg.add_edge('C', 'C', label='b', round_trace=')', square_trace=']')
#
# lg.save('graph_examples/right')

# lg = LGraph()
# lg.load('graph_examples/a^n_b^n_c^n')
#
# for line in ['', 'abc', 'abcc', 'aaaabbbbcccc']:
#     path = lg.find_successful_path(line)
#     print(f'"{line}": {LGraph.path_to_string(path)}')
#
# print('abc' in lg, 'asdf' in lg)

# lg = LGraph()
# for graph_name in ['a^n_b^n_c^n', 'a^n_b^n', 'a^n_b^k']:
#     lg.load(f'graph_examples/{graph_name}')
#     print(
#         f'Graph {graph_name} is {lg.type.name.replace("_", " ").capitalize()} ('
#         f'regular - {lg.is_regular()}, '
#         f'context free - {lg.is_context_free()}, '
#         f'context sensitive - {lg.is_context_sensitive()})'
#     )

# UNION TEST

# lg_left, lg_right = LGraph(), LGraph()
#
# lg_left.load('graph_examples/left')
# lg_right.load('graph_examples/right')
#
# lg = lg_left + lg_right
# lg.save('graph_examples/union_result')
