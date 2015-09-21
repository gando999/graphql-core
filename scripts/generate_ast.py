if __name__ == '__main__':
    import os.path
    import sys
    import subprocess
    project_root = os.path.join(os.path.dirname(__file__), '..')
    with open(os.path.join(project_root, 'graphql/core/language/ast.py'), 'w') as fp:
        process = subprocess.Popen(
            ['python', '../libgraphqlparser/ast/ast.py', 'generate_ast', '../libgraphqlparser/ast/ast.ast'],
            stdout=fp,
            cwd=os.path.join(project_root, 'scripts'),
            env={'PYTHONPATH': '.'}
        )
        sys.exit(process.wait())


from casing import snake

# Fix inconsistencies between libgraphqlparser and graphql-js
REMAP_TYPES = {
    'ArrayValue': 'ListValue',
}

def remap_type(typename):
    return REMAP_TYPES.get(typename, typename)


class Printer(object):
    def __init__(self):
        self._current_union = None
        self._parent_types = {}
        self._fields = []

    def start_file(self):
        print '''# This is autogenerated code. DO NOT change this manually.
# Run scripts/generate_ast.py to generate this file.


class Node(object):
    pass'''

    def end_file(self):
        pass

    def start_type(self, name):
        name = remap_type(name)
        parent_type = self._parent_types.get(name, 'Node')
        print '''

class {name}({parent_type}):'''.format(name=name, parent_type=parent_type)

    def field(self, type, name, nullable, plural):
        type = remap_type(type)
        self._fields.append((type, name, nullable, plural))

    def end_type(self, typename):
        typename = remap_type(typename)
        self._print_slots()
        self._print_ctor()
        self._print_comparator(typename)
        self._print_repr(typename)
        self._fields = []

    def _print_slots(self):
        slots = ', '.join("'" + snake(name) + "'" for (type, name, nullable, plural) in self._fields)
        print '''    __slots__ = ('loc', {slots})'''.format(slots=slots)

    def _print_ctor(self):
        fields = (
            [field for field in self._fields if not field[2]] +
            [field for field in self._fields if field[2]])
        ctor_args = ', '.join(snake(name) + ('=None' if nullable else '') for (type, name, nullable, plural) in fields)
        print '''
    def __init__(self, {ctor_args}, loc=None):
        self.loc = loc'''.format(ctor_args=ctor_args)
        for type, name, nullable, plural in self._fields:
            print '''        self.{name} = {name}'''.format(name=snake(name))

    def _print_comparator(self, typename):
        print '''
    def __eq__(self, other):
        return (
            isinstance(other, {typename}) and
            self.loc == other.loc and'''.format(typename=typename)
        print ' and\n'.join(
            '''            self.{name} == other.{name}'''.format(name=snake(name))
            for type, name, nullable, plural in self._fields
        )
        print '        )'

    def _print_repr(self, typename):
        print '''
    def __repr__(self):
        return ('{typename}(' '''.rstrip().format(typename=typename)
        first = True
        for type, name, nullable, plural in self._fields:
            print "                '{comma}{name}={{self.{name}!r}}'".format(
                comma=', ' if not first else '',
                name=snake(name)
            )
            first = False
        print '''                ')').format(self=self)'''

    def start_union(self, name):
        self._current_union = name
        print '''

class {name}(Node):
    pass'''.format(name=name)

    def union_option(self, option):
        option = remap_type(option)
        self._parent_types[option] = self._current_union

    def end_union(self, name):
        self._current_union = None

