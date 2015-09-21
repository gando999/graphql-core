# This is autogenerated code. DO NOT change this manually.
# Run scripts/generate_ast.py to generate this file.


class Node(object):
    pass


class Definition(Node):
    pass


class Document(Node):
    __slots__ = ('loc', 'definitions')

    def __init__(self, definitions, loc=None):
        self.loc = loc
        self.definitions = definitions

    def __eq__(self, other):
        return (
            isinstance(other, Document) and
            self.loc == other.loc and
            self.definitions == other.definitions
        )

    def __repr__(self):
        return ('Document('
                'definitions={self.definitions!r}'
                ')').format(self=self)


class OperationDefinition(Definition):
    __slots__ = ('loc', 'operation', 'name', 'variable_definitions', 'directives', 'selection_set')

    def __init__(self, operation, selection_set, name=None, variable_definitions=None, directives=None, loc=None):
        self.loc = loc
        self.operation = operation
        self.name = name
        self.variable_definitions = variable_definitions
        self.directives = directives
        self.selection_set = selection_set

    def __eq__(self, other):
        return (
            isinstance(other, OperationDefinition) and
            self.loc == other.loc and
            self.operation == other.operation and
            self.name == other.name and
            self.variable_definitions == other.variable_definitions and
            self.directives == other.directives and
            self.selection_set == other.selection_set
        )

    def __repr__(self):
        return ('OperationDefinition('
                'operation={self.operation!r}'
                ', name={self.name!r}'
                ', variable_definitions={self.variable_definitions!r}'
                ', directives={self.directives!r}'
                ', selection_set={self.selection_set!r}'
                ')').format(self=self)


class VariableDefinition(Node):
    __slots__ = ('loc', 'variable', 'type', 'default_value')

    def __init__(self, variable, type, default_value=None, loc=None):
        self.loc = loc
        self.variable = variable
        self.type = type
        self.default_value = default_value

    def __eq__(self, other):
        return (
            isinstance(other, VariableDefinition) and
            self.loc == other.loc and
            self.variable == other.variable and
            self.type == other.type and
            self.default_value == other.default_value
        )

    def __repr__(self):
        return ('VariableDefinition('
                'variable={self.variable!r}'
                ', type={self.type!r}'
                ', default_value={self.default_value!r}'
                ')').format(self=self)


class SelectionSet(Node):
    __slots__ = ('loc', 'selections')

    def __init__(self, selections, loc=None):
        self.loc = loc
        self.selections = selections

    def __eq__(self, other):
        return (
            isinstance(other, SelectionSet) and
            self.loc == other.loc and
            self.selections == other.selections
        )

    def __repr__(self):
        return ('SelectionSet('
                'selections={self.selections!r}'
                ')').format(self=self)


class Selection(Node):
    pass


class Field(Selection):
    __slots__ = ('loc', 'alias', 'name', 'arguments', 'directives', 'selection_set')

    def __init__(self, name, alias=None, arguments=None, directives=None, selection_set=None, loc=None):
        self.loc = loc
        self.alias = alias
        self.name = name
        self.arguments = arguments
        self.directives = directives
        self.selection_set = selection_set

    def __eq__(self, other):
        return (
            isinstance(other, Field) and
            self.loc == other.loc and
            self.alias == other.alias and
            self.name == other.name and
            self.arguments == other.arguments and
            self.directives == other.directives and
            self.selection_set == other.selection_set
        )

    def __repr__(self):
        return ('Field('
                'alias={self.alias!r}'
                ', name={self.name!r}'
                ', arguments={self.arguments!r}'
                ', directives={self.directives!r}'
                ', selection_set={self.selection_set!r}'
                ')').format(self=self)


class Argument(Node):
    __slots__ = ('loc', 'name', 'value')

    def __init__(self, name, value, loc=None):
        self.loc = loc
        self.name = name
        self.value = value

    def __eq__(self, other):
        return (
            isinstance(other, Argument) and
            self.loc == other.loc and
            self.name == other.name and
            self.value == other.value
        )

    def __repr__(self):
        return ('Argument('
                'name={self.name!r}'
                ', value={self.value!r}'
                ')').format(self=self)


class FragmentSpread(Selection):
    __slots__ = ('loc', 'name', 'directives')

    def __init__(self, name, directives=None, loc=None):
        self.loc = loc
        self.name = name
        self.directives = directives

    def __eq__(self, other):
        return (
            isinstance(other, FragmentSpread) and
            self.loc == other.loc and
            self.name == other.name and
            self.directives == other.directives
        )

    def __repr__(self):
        return ('FragmentSpread('
                'name={self.name!r}'
                ', directives={self.directives!r}'
                ')').format(self=self)


class InlineFragment(Selection):
    __slots__ = ('loc', 'type_condition', 'directives', 'selection_set')

    def __init__(self, type_condition, selection_set, directives=None, loc=None):
        self.loc = loc
        self.type_condition = type_condition
        self.directives = directives
        self.selection_set = selection_set

    def __eq__(self, other):
        return (
            isinstance(other, InlineFragment) and
            self.loc == other.loc and
            self.type_condition == other.type_condition and
            self.directives == other.directives and
            self.selection_set == other.selection_set
        )

    def __repr__(self):
        return ('InlineFragment('
                'type_condition={self.type_condition!r}'
                ', directives={self.directives!r}'
                ', selection_set={self.selection_set!r}'
                ')').format(self=self)


class FragmentDefinition(Definition):
    __slots__ = ('loc', 'name', 'type_condition', 'directives', 'selection_set')

    def __init__(self, name, type_condition, selection_set, directives=None, loc=None):
        self.loc = loc
        self.name = name
        self.type_condition = type_condition
        self.directives = directives
        self.selection_set = selection_set

    def __eq__(self, other):
        return (
            isinstance(other, FragmentDefinition) and
            self.loc == other.loc and
            self.name == other.name and
            self.type_condition == other.type_condition and
            self.directives == other.directives and
            self.selection_set == other.selection_set
        )

    def __repr__(self):
        return ('FragmentDefinition('
                'name={self.name!r}'
                ', type_condition={self.type_condition!r}'
                ', directives={self.directives!r}'
                ', selection_set={self.selection_set!r}'
                ')').format(self=self)


class Value(Node):
    pass


class Variable(Value):
    __slots__ = ('loc', 'name')

    def __init__(self, name, loc=None):
        self.loc = loc
        self.name = name

    def __eq__(self, other):
        return (
            isinstance(other, Variable) and
            self.loc == other.loc and
            self.name == other.name
        )

    def __repr__(self):
        return ('Variable('
                'name={self.name!r}'
                ')').format(self=self)


class IntValue(Value):
    __slots__ = ('loc', 'value')

    def __init__(self, value, loc=None):
        self.loc = loc
        self.value = value

    def __eq__(self, other):
        return (
            isinstance(other, IntValue) and
            self.loc == other.loc and
            self.value == other.value
        )

    def __repr__(self):
        return ('IntValue('
                'value={self.value!r}'
                ')').format(self=self)


class FloatValue(Value):
    __slots__ = ('loc', 'value')

    def __init__(self, value, loc=None):
        self.loc = loc
        self.value = value

    def __eq__(self, other):
        return (
            isinstance(other, FloatValue) and
            self.loc == other.loc and
            self.value == other.value
        )

    def __repr__(self):
        return ('FloatValue('
                'value={self.value!r}'
                ')').format(self=self)


class StringValue(Value):
    __slots__ = ('loc', 'value')

    def __init__(self, value, loc=None):
        self.loc = loc
        self.value = value

    def __eq__(self, other):
        return (
            isinstance(other, StringValue) and
            self.loc == other.loc and
            self.value == other.value
        )

    def __repr__(self):
        return ('StringValue('
                'value={self.value!r}'
                ')').format(self=self)


class BooleanValue(Value):
    __slots__ = ('loc', 'value')

    def __init__(self, value, loc=None):
        self.loc = loc
        self.value = value

    def __eq__(self, other):
        return (
            isinstance(other, BooleanValue) and
            self.loc == other.loc and
            self.value == other.value
        )

    def __repr__(self):
        return ('BooleanValue('
                'value={self.value!r}'
                ')').format(self=self)


class EnumValue(Value):
    __slots__ = ('loc', 'value')

    def __init__(self, value, loc=None):
        self.loc = loc
        self.value = value

    def __eq__(self, other):
        return (
            isinstance(other, EnumValue) and
            self.loc == other.loc and
            self.value == other.value
        )

    def __repr__(self):
        return ('EnumValue('
                'value={self.value!r}'
                ')').format(self=self)


class ListValue(Value):
    __slots__ = ('loc', 'values')

    def __init__(self, values, loc=None):
        self.loc = loc
        self.values = values

    def __eq__(self, other):
        return (
            isinstance(other, ListValue) and
            self.loc == other.loc and
            self.values == other.values
        )

    def __repr__(self):
        return ('ListValue('
                'values={self.values!r}'
                ')').format(self=self)


class ObjectValue(Value):
    __slots__ = ('loc', 'fields')

    def __init__(self, fields, loc=None):
        self.loc = loc
        self.fields = fields

    def __eq__(self, other):
        return (
            isinstance(other, ObjectValue) and
            self.loc == other.loc and
            self.fields == other.fields
        )

    def __repr__(self):
        return ('ObjectValue('
                'fields={self.fields!r}'
                ')').format(self=self)


class ObjectField(Node):
    __slots__ = ('loc', 'name', 'value')

    def __init__(self, name, value, loc=None):
        self.loc = loc
        self.name = name
        self.value = value

    def __eq__(self, other):
        return (
            isinstance(other, ObjectField) and
            self.loc == other.loc and
            self.name == other.name and
            self.value == other.value
        )

    def __repr__(self):
        return ('ObjectField('
                'name={self.name!r}'
                ', value={self.value!r}'
                ')').format(self=self)


class Directive(Node):
    __slots__ = ('loc', 'name', 'arguments')

    def __init__(self, name, arguments=None, loc=None):
        self.loc = loc
        self.name = name
        self.arguments = arguments

    def __eq__(self, other):
        return (
            isinstance(other, Directive) and
            self.loc == other.loc and
            self.name == other.name and
            self.arguments == other.arguments
        )

    def __repr__(self):
        return ('Directive('
                'name={self.name!r}'
                ', arguments={self.arguments!r}'
                ')').format(self=self)


class Type(Node):
    pass


class NamedType(Type):
    __slots__ = ('loc', 'name')

    def __init__(self, name, loc=None):
        self.loc = loc
        self.name = name

    def __eq__(self, other):
        return (
            isinstance(other, NamedType) and
            self.loc == other.loc and
            self.name == other.name
        )

    def __repr__(self):
        return ('NamedType('
                'name={self.name!r}'
                ')').format(self=self)


class ListType(Type):
    __slots__ = ('loc', 'type')

    def __init__(self, type, loc=None):
        self.loc = loc
        self.type = type

    def __eq__(self, other):
        return (
            isinstance(other, ListType) and
            self.loc == other.loc and
            self.type == other.type
        )

    def __repr__(self):
        return ('ListType('
                'type={self.type!r}'
                ')').format(self=self)


class NonNullType(Type):
    __slots__ = ('loc', 'type')

    def __init__(self, type, loc=None):
        self.loc = loc
        self.type = type

    def __eq__(self, other):
        return (
            isinstance(other, NonNullType) and
            self.loc == other.loc and
            self.type == other.type
        )

    def __repr__(self):
        return ('NonNullType('
                'type={self.type!r}'
                ')').format(self=self)


class Name(Node):
    __slots__ = ('loc', 'value')

    def __init__(self, value, loc=None):
        self.loc = loc
        self.value = value

    def __eq__(self, other):
        return (
            isinstance(other, Name) and
            self.loc == other.loc and
            self.value == other.value
        )

    def __repr__(self):
        return ('Name('
                'value={self.value!r}'
                ')').format(self=self)
