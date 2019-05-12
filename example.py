"""
Creating L-Graph that generates language { a^n b^n c^n | n >= 0 } and saving it to file.
"""
from lgraph import LGraph


# Creating some L-graphs and saving them
lg = LGraph(3)

lg.add_edge(lg.initial_main.name, '0')
lg.add_edge('0', '1', label='b', round_trace=')', square_trace='[')
lg.add_edge('1', '2', label='c', square_trace=']')
lg.add_edge('2', lg.final_main.name)

lg.add_edge('0', '0', label='a', round_trace='(')
lg.add_edge('1', '1', label='b', round_trace=')', square_trace='[')
lg.add_edge('2', '2', label='c', square_trace=']')

lg.save('graph_examples/a^n_b^n_c^n')

lg = LGraph(2)

lg.add_edge(lg.initial_main.name, '0')
lg.add_edge('0', '1')
lg.add_edge('1', lg.final_main.name)

lg.add_edge('0', '0', label='a')
lg.add_edge('1', '1', label='b')

lg.save('graph_examples/a^n_b^k')

lg = LGraph(2)

lg.add_edge(lg.initial_main.name, '0')
lg.add_edge('1', lg.final_main.name)

lg.add_edge('0', '1', label='b', round_trace=')')
lg.add_edge('0', '0', label='a', round_trace='(')
lg.add_edge('1', '1', label='b', round_trace=')')

lg.save('graph_examples/a^n_b^n')


lg.load('graph_examples/a^n_b^n_c^n')

# path = lg.find_successful_path('')
# print(LGraph.path_to_string(path))
#
# path = lg.find_successful_path('abc')
# print(LGraph.path_to_string(path))
#
# path = lg.find_successful_path('abcc')
# print(LGraph.path_to_string(path))
#
# path = lg.find_successful_path('aaaabbbbcccc')
# print(LGraph.path_to_string(path))
#
# print('abc' in lg, 'asdf' in lg)

for graph_name in ['a^n_b^n_c^n', 'a^n_b^n', 'a^n_b^k']:
    lg.load(f'graph_examples/{graph_name}')
    print(
        f'Graph {graph_name} is {lg.type.name.replace("_", " ").capitalize()} ('
        f'regular - {lg.is_regular()}, '
        f'context free - {lg.is_context_free()}, '
        f'context sensitive - {lg.is_context_sensitive()})'
    )
