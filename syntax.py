from more_itertools import peekable

class LexicalComponent:
    def __init__(self, token, token_id, li_num):
        self.token = token
        self.token_id = token_id 
        self.li_num = li_num

    def __str__(self):
        return f"{self.token}, {self.token_id}, {self.li_num} "

class Parser:
    def __init__(self, lexical_components):
        self.lexical_components = peekable(
                [LexicalComponents(*comp) for comp in lexical_components])
        self.buffer = ""
        self.passes = False

    def program(self):

        if next(self.lexical_components).token == "program":
            pass
        
        #<Identifier>
        if next(self.lexical_components).token_id == 100:
            pass

        if next(self.lexical_components).token == ';':
            pass

        self.block()

        if next(self.lexical_components).token == '.':
            self.passes = True


    def block(self):
        self.variable_declaration_part()
        self.procedure_declaration_part()
        self.statement_part()

    def variable_declaration_part():
        if peekable(self.lexical_components).token != "var":
            pass
        
        #<Identifier>
        if next(self.lexical_components).token_id = 100:
            pass

        if next(self.lexical_components).token == "program":
            pass

        if next(self.lexical_components).token == "program":
            pass

    def variable_declaration():
        pass

    def type():
        pass

    def simple_type():
        pass

    def type_identifier():
        pass

    def procedure_declaration_part(3):
        pass
    
    def procedure_declaration():
        pass

    def statement_part():
        pass

    def compound_statement():
        pass
    
    def statement():
        pass
    
    def simple_statement():
        pass
    
    def assignment_statement():
        pass
    
    def procedure_statement():
        pass
    
    def procedure_identifier():
        pass
    
    def read_statement():
        pass

    def input_variable():
        pass
    
    def write_statement():
        pass
    
    def output_value():
        pass
    
    def structured_statement():
        pass
    
    def if_statement():
        pass
    
    def while_statement():
        pass
    
    def expression():
        pass

    def simple_expression():
        pass

    def term():
        pass

    def factor():
        pass

    def relational_operator():
        pass

    def sign():
        pass

    def adding_operator():
        pass

    def multiplying_operator():
        pass

    def variable():
        pass

    def entire_variable():
        pass

    def variable_identifier():
        pass


"""
# identifier = ""
# variable_identifier = Node("variable identifier", identifier)
# entire_variable = Node("entire_variable", variable_identifier)
# variable = Node()
# multiplying_operator = Node()
# adding_operator = Node()
# sign = Node()
# relational_operator = Node()
# factor = Node()
# term = Node()
# simple_expression = Node()
# variable = Node()
# variable = Node()
# variable = Node()
# variable = Node()

<program> ::=	program <identifier> ; <block> .
<block> ::=	<variable declaration part>

<procedure declaration part>
<statement part>
<variable declaration part> ::=	<empty> |
var <variable declaration> ;
    { <variable declaration> ; }
<variable declaration> ::=	<identifier > { , <identifier> } : <type>
<type> ::=	<simple type> | <array type
<array type> ::=	array [ <index range> ] of <simple type>
<index range> ::=	<integer constant> .. <integer constant>
<simple type> ::=	<type identifier>
<type identifier> ::=	<identifier>
<procedure declaration part> ::=	{ <procedure declaration> ; }
<procedure declaration> ::=	procedure <identifier> ; <block>
<statement part> ::=	<compound statement>
<compound statement> ::=	begin <statement>{ ; <statement> } end
<statement> ::=	<simple statement> | <structured statement>
<simple statement> ::=	<assignment statement> | <procedure statement> |
<read statement> | <write statement>
<assignment statement> ::=	<variable> := <expression>
<procedure statement> ::=	<procedure identifier>
<procedure identifier> ::=	<identifier>
<read statement> ::=	read ( <input variable> { , <input variable> } )
<input variable> ::=	<variable>
<write statement> ::=	write ( <output value> { , <output value> } )
<output value> ::=	<expression>
<structured statement> ::=	<compound statement> | <if statement> |
<while statement>
<if statement> ::=	if <expression> then <statement> |
if <expression> then <statement> else <statement>
<while statement> ::=	while <expression> do <statement>
<expression> ::=	<simple expression> |
<simple expression> <relational operator> <simple expression>
<simple expression> ::=	<sign> <term> { <adding operator> <term> }
<term> ::=	<factor> { <multiplying operator> <factor> }
<factor> ::=	<variable> | <constant> | ( <expression> ) | not <factor>
<relational operator> ::=	= | <> | < | <= | >= | >
<sign> ::=	+ | - | <empty>
<adding operator> ::=	+ | - | or
<multiplying operator> ::=	* | div | and
<variable> ::=	<entire variable> | <indexed variable>
<entire variable> ::=	<variable identifier>
<variable identifier> ::=	<identifier>

"""
