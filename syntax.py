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

        if next(self.lexical_components).token != "program":
            pass
        
        #<Identifier>
        if next(self.lexical_components).token_id != 100:
            pass

        if next(self.lexical_components).token != ';':
            pass

        self.block()

        if next(self.lexical_components).token != '.':
            self.passes = True


    def block(self):
        self.variable_declaration_part()
        self.statement_part()

    def variable_declaration_part(self):
        if self.lexical_components.peek != "var":
            return

        if next(self.lexical_components).token != "var":
            pass
        
        self.variable_declaration()

    def variable_declaration(self):
        if next(self.lexical_components).token_id != 100:
            pass

        if next(self.lexical_components).token != ":":
            pass
        
        self.type()

    def type(self):
        self.simple_type()

    def simple_type(self):
        type_identifier()
        pass

    def type_identifier(self):
        #<identifier>
        if next(self.lexical_components).token_id != 100:
            pass

    def statement_part(self):
        self.compound_statement()
        pass

    def compound_statement(self):
        if next(self.lexical_components).token != "begin":
            pass

        self.statement()

        if next(self.lexical_components).token != "end":
            pass
    
    def statement(self):
        self.simple_statement()
        self.structured_statement()
    
    def simple_statement(self):
        self.assignment_statement()
        self.read_statement()
        self.write_statement()
        pass
    
    def assignment_statement(self):
        self.variable()

        if next(self.lexical_components).token != ":=":
            pass

        self.expression()
    
    def procedure_statement(self):
        pass
    
    def procedure_identifier(self):
        pass
    
    def read_statement(self):
        if next(self.lexical_components).token != "read":
            pass
        if next(self.lexical_components).token != "(":
            pass

        self.input_variable()

        if next(self.lexical_components).token != ")":
            pass

    def input_variable():
        pass
    
    def write_statement(self):
        if next(self.lexical_components).token != "write":
            pass
        if next(self.lexical_components).token != "(":
            pass

        self.output_value()

        if next(self.lexical_components).token != ")":
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

        if next(self.lexical_components).token != "if":
            pass
        
        self.expression()

        if next(self.lexical_components).token != "then":
            pass
        self.statement()
        pass
    
    def while_statement(self):
        if next(self.lexical_components).token != "while":
            pass

        self.expression()

        if next(self.lexical_components).token != "do":
            pass
    
        self.statement()

    def expression():
        self.simple_expression()
        pass

    def simple_expression():
        self.sign()
        self.term()
        pass

    def term():
        self.factor()

        #{}


        pass

    def factor():
        #|
        self.variable()
        #|
        self.constant()
        #|
        if next(self.lexical_components).token != "(":
            pass
        
        self.expression()

        if next(self.lexical_components).token != ")":
            pass

        #|

        if next(self.lexical_components).token != "not":
            pass

        self.factor()

    def relational_operator():

        if next(self.lexical_components).token != "=":
            pass
        #|
        if next(self.lexical_components).token != "<>":
            pass
        #|
        if next(self.lexical_components).token != "<":
            pass
        #|
        if next(self.lexical_components).token != "<=":
            pass
        #|
        if next(self.lexical_components).token != ">=":
            pass
        #|
        if next(self.lexical_components).token != ">":
            pass

        pass

    def sign():
        #|
        if next(self.lexical_components).token != "+":
            pass

        #|
        if next(self.lexical_components).token != "=":
            pass

        #|
        if next(self.lexical_components).token != "None":
            pass

    def adding_operator():
        if next(self.lexical_components).token != "+":
            pass

        if next(self.lexical_components).token != "-":
            pass

        if next(self.lexical_components).token != "or":
            pass
        pass

    def multiplying_operator():
        if next(self.lexical_components).token != "*":
            pass

        if next(self.lexical_components).token != "div":
            pass

        if next(self.lexical_components).token != "and":
            pass

    def variable():
        self.entire_variable()
        pass

    def entire_variable():
        self.variable_identifier()
        pass

    def variable_identifier():
        #identifier
        if next(self.lexical_components).token_id != 100:
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
