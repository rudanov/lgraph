"""
Creating L-Graph that generates language { a^n b^n c^n | n >= 0 } and saving it to file.
"""
from lgraph import LGraph

lg = LGraph()

for _ in range(3):
    lg.add_vertex()

lg.add_edge(lg.initial_main.name, '0')
lg.add_edge('0', '1')
lg.add_edge('1', '2')
lg.add_edge('2', lg.final_main.name)

lg.add_edge('0', '0', label='a', round_trace='(')
lg.add_edge('1', '1', label='b', round_trace=')', square_trace='[')
lg.add_edge('2', '2', label='c', square_trace=']')

lg.save('a^n_b^n_c^n')
lg.load('a^n_b^n_c^n')
