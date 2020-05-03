from more_itertools import peekable

class LexicalComponent:
    def __init__(self, token, token_id, li_num):
        self.token = token
        self.token_id = token_id 
        self.li_num = li_num

    def __str__(self):
        return f"{self.token}, {self.token_id}, {self.li_num} "

class SyntacticError(exception):
    pass

class Parser:
    def __init__(self, lexical_components):
        self.lexical_components = seekable(
                [LexicalComponents(*comp) for comp in lexical_components])
        self.buffer = ""
        self.passes = False


    def consume_token(self, token=None, token_id=None):
        if token_id is None:
            if next(self.lexical_components.token) == token:
                return
            else:
                raise SyntacticError("Syntax Error")
        else:
            if next(self.lexical_components.token_id) == token_id:
                return
            else:
                raise SyntacticError("Syntax Error")


    def peek_token(self, token="", token_id=0):
        if token_id is None:
            return self.lexical_components.peek().token == token:

        else:
            return self.lexical_components.peek().token_id == token_id:


    def program(self):
        # <program> ::=	program <identifier> ; <block> .
        self.consume_token("program")
        self.consume_token(token_id=100)
        self.consume_token(";")
        self.block()
        self.consume_token(".")

    def block(self):
        # <block> ::= <variable declaration part>
        #             <statement part>
        self.variable_declaration_part()
        self.statement_part()

    def variable_declaration_part(self):

        # <variable declaration part> ::= <empty>
        #                                 |var <variable declaration> ;
        #                                  { <variable declaration> ; }

        self.consume_token("var")
        self.consume_token(token_id=100)
        self.consume_token(";")

        if self.peek_token("var"):
            #<Identifier>
            while self.peek_token(token_id=100):
                self.variable_declaration()
                self.consume_token(";")
        return

    def variable_declaration(self):
        # <variable declaration> ::=	<identifier > { , <identifier> } : <identifier>

        self.consume_token(token_id=100)

        if self.peek_token(","):
            self.consume_token(",")
            while self.peek_token(","):
                pass

        self.consume_token(":")
        self.consume_token(token_id=100)

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

    def input_variable(self):
        pass
    
    def write_statement(self):
        pass
    
    def output_value(self):
        pass
    
    def structured_statement(self):
        pass
    
    def if_statement(self):

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

    def expression(self):
        self.simple_expression()
        pass

    def simple_expression(self):
        self.sign()
        self.term()
        pass

    def term(self):
        self.factor()

        #{}


        pass

    def factor(self):
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

    def relational_operator(self):

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

    def sign(self):
        #|
        if next(self.lexical_components).token != "+":
            pass

        #|
        if next(self.lexical_components).token != "=":
            pass

        #|
        if next(self.lexical_components).token != "None":
            pass

    def adding_operator(self):
        if next(self.lexical_components).token != "+":
            pass

        if next(self.lexical_components).token != "-":
            pass

        if next(self.lexical_components).token != "or":
            pass
        pass

    def multiplying_operator(self):
        if next(self.lexical_components).token != "*":
            pass

        if next(self.lexical_components).token != "div":
            pass

        if next(self.lexical_components).token != "and":
            pass

    def variable():
        self.entire_variable(self)
        pass

    def entire_variable():
        self.variable_identifier(self)
        pass

    def variable_identifier(self):
        #identifier
        if next(self.lexical_components).token_id != 100:
            pass

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
