import string
import json

from collections import OrderedDict

from lgraph.vertex import Vertex
from lgraph.edge import Edge


class LGraph:
    def __init__(self, alphabet=string.ascii_lowercase):
        self.__initial_main_name = 'initial_main'
        self.__final_main_name = 'final_main'

        self.__alphabet = alphabet
        self.__initials = dict(initial_main=Vertex(self.__initial_main_name))
        self.__finals = dict(final_main=Vertex(self.__final_main_name))
        self.__vertexes = dict()
        self.__edges = set()

        self.__square_brackets = list()
        self.__round_brackets = list()

    def __contains__(self, item: str):
        pass

    def __dict__(self):
        def edge_dict_key(edg):
            return edg['beginning'], edg['end'], edg['label'], edg['round_trace'], edg['square_trace']

        return OrderedDict(
            alphabet=self.__alphabet,
            initials=sorted(list(self.__initials.keys())),
            finals=sorted(list(self.__finals.keys())),
            vertexes=sorted(list(self.__vertexes.keys())),
            edges=sorted([edg.__dict__() for edg in self.__edges], key=edge_dict_key),
        )

    @property
    def alphabet(self):
        return self.__alphabet

    @property
    def initials(self):
        return self.__initials

    @property
    def finals(self):
        return self.__finals

    @property
    def vertexes(self):
        return self.__vertexes.values()

    @property
    def edges(self):
        return self.__edges

    @property
    def initial_main(self):
        return self.__initials['initial_main']

    @property
    def final_main(self):
        return self.__finals['final_main']

    @property
    def vertex_names(self):
        return list(self.__vertexes) + list(self.__initials) + list(self.__finals)

    @property
    def number_of_vertexes(self):
        return len(self.__vertexes)

    @property
    def number_of_edges(self):
        return len(self.__edges)

    def add_vertex(self, vtx_name=None, initial=False, final=False):
        vertex_dict = self.__initials if initial else self.__finals if final else self.__vertexes
        vtx_name = (
            vtx_name if vtx_name else
            f'initial_{len(self.__initials)}' if initial else
            f'final_{len(self.__finals)}' if final else
            f'{len(self.__vertexes)}'
        )
        if vtx_name in self.vertex_names:
            raise ValueError(f'Vertex with name "{vtx_name}" already exists.')

        vertex_dict[vtx_name] = Vertex(name=vtx_name)

    def remove_vertex(self, vtx_name: str):
        if vtx_name in [self.__initial_main_name, self.__final_main_name]:
            raise ValueError(f'Can not remove vertex with name {vtx_name}')
        vtx_removed = (
            self.__initials.pop(vtx_name, None),
            self.__finals.pop(vtx_name, None),
            self.__vertexes.pop(vtx_name, None)
        )
        if not any(vtx_removed):
            raise ValueError(f'Vertex with name "{vtx_name}" was not found.')

    def get_vertex(self, vtx_name: str):
        vtx = (
            self.__vertexes[vtx_name] if vtx_name in self.__vertexes else
            self.__initials[vtx_name] if vtx_name in self.__initials else
            self.__finals[vtx_name] if vtx_name in self.__finals else
            None
        )
        if not vtx:
            raise ValueError(f'Vertex with name "{vtx_name}" was not found.')
        return vtx

    def rename_vertex(self, vtx_name: str, new_vtx_name: str):
        if new_vtx_name in self.vertex_names:
            raise ValueError(f'Vertex with name "{new_vtx_name}" already exists.')
        if vtx_name not in self.vertex_names:
            raise ValueError(f'Vertex with name "{vtx_name}" was not found.')
        vtx_dict = (
            self.__vertexes if vtx_name in self.__vertexes else
            self.__initials if vtx_name in self.__initials else
            self.__finals if vtx_name in self.__finals else
            None
        )
        vtx_dict[new_vtx_name] = vtx_dict[vtx_name]
        vtx_dict[new_vtx_name].rename(new_vtx_name)
        vtx_dict.pop(vtx_name, None)

    def add_edge(self, beg_vtx_name: str, end_vtx_name: str, label = '', round_trace=('', 0), square_trace=('', 0)):
        if label not in self.alphabet:
            raise ValueError(f'Edge label "{label}"" is not from the alphabet.')

        beg_vtx, end_vtx = self.get_vertex(beg_vtx_name), self.get_vertex(end_vtx_name)
        edg = Edge(beg_vtx, end_vtx, label=label, round_trace=round_trace, square_trace=square_trace)
        self.__edges.add(edg)
        beg_vtx.add_edge(edg)

    def remove_edge(self, edg: Edge):
        try:
            self.__edges.remove(edg)
        except KeyError:
            raise ValueError(f'Edge from {edg.beg.name} to {edg.end.name} with label "{edg.label}", '
                             f'round trace {edg.round_trace} and square trace {edg.square_trace} was not found.')
        edg.beg.remove_edge(edg)

    def get_edges_between(self, beg_vtx: Vertex, end_vtx: Vertex):
        return [edg for edg in self.__edges if edg.beg == beg_vtx and edg.end == end_vtx]

    def save(self, path: str):
        with open(path, 'w') as file:
            print(json.dumps(self.__dict__(), indent=4), file=file)

    def load(self, path: str):
        with open(path, 'r') as file:
            data = json.load(file)
            self.__init__(data['alphabet'])

            for vtx_set_name in ['initials', 'finals', 'vertexes']:
                for vtx_name in data[vtx_set_name]:
                    if vtx_name not in [self.__initial_main_name, self.__final_main_name]:
                        self.add_vertex(
                            vtx_name,
                            initial=vtx_set_name == 'initials',
                            final=vtx_set_name == 'finals'
                        )

            for edg in data['edges']:
                self.add_edge(
                    edg['beginning'], edg['end'],
                    label=edg['label'],
                    round_trace=tuple(edg['round_trace']),
                    square_trace=tuple(edg['square_trace'])
                )
