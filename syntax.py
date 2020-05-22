from more_itertools import peekable
from syntax_errors import SyntacticError

class LexicalComponent:
    def __init__(self, token, token_id, li_num):
        self.token = token
        self.token_id = token_id 
        self.li_num = li_num

    def __str__(self):
        return f"{self.token}, {self.token_id}, {self.li_num} "

class Parser:
    def __init__(self, lexical_components, file_source):
        self.lexical_components = peekable(
                [LexicalComponent(*comp) for comp in lexical_components])
        
        self.lines = open(file_source, 'r').readlines()
        self.passes = False

    def consume_token(self, token=None, token_id=None):
        try:
            consumed = next(self.lexical_components)
            # print(consumed)
            if token_id is None:
                if consumed.token == token:
                    return
                else:
                    raise SyntacticError(consumed, self.lines, token)
            else:
                if consumed.token_id == token_id:
                    return
                else:
                    raise SyntacticError(consumed, self.lines, expected_id=token_id)

        except StopIteration:
            print(f"End of file reached, Syntax Error: \"{token}\" was expected")
            quit()

    def peek_token(self, token="", token_id=0):
        if token_id == 0:
            return self.lexical_components.peek().token == token

        else:
            return self.lexical_components.peek().token_id == token_id

    def next_tokens(self, *items):
        return self.lexical_components.peek().token in items

    def program(self):
        self.consume_token("program")
        self.consume_token(token_id=100)
        self.consume_token(";")
        self.block()
        self.consume_token(".")
        
        self.passes = True

    def block(self):
        self.variable_declaration_part()
        self.statement_part()

    def variable_declaration_part(self):
        
        if self.peek_token("var"):
            self.consume_token("var")
            self.variable_declaration()
            self.consume_token(";")
            if self.peek_token(token_id=100):
                while self.peek_token(token_id=100):
                    self.variable_declaration()
                    self.consume_token(";")

    def variable_declaration(self):
        self.consume_token(token_id=100)

        if self.peek_token(","):
            while self.peek_token(","):
                self.consume_token(",")
                self.consume_token(token_id=100)

        self.consume_token(":")
        self.type()

    def type(self):

        #<type> ::= integer | real | string   

        if self.peek_token("integer"):
            self.consume_token("integer")

        elif self.peek_token("real"):
            self.consume_token("real")
        
        elif self.peek_token("string"):
            self.consume_token("string")
    
    def statement_part(self):
        self.compound_statement()

    def compound_statement(self):

        self.consume_token("begin")
        self.statement()

        if self.peek_token(";"):
            while self.peek_token(";"):
                self.consume_token(";")
                self.statement()
        
        self.consume_token("end")
    
    def statement(self):
        if self.peek_token(token_id=100) or self.next_tokens("read", "write"):
            self.simple_statement()
        
        elif self.next_tokens("begin", "if", "while"):  
            self.structured_statement()
    

    def simple_statement(self):
        if self.peek_token(token_id=100):
            self.assignment_statement()

        elif self.peek_token("read"):
            self.read_statement()

        elif self.peek_token("write"):
            self.write_statement()
    
    def assignment_statement(self):
        self.consume_token(token_id=100)
        self.consume_token(":=")
        self.expression()
    
    def read_statement(self):
        self.consume_token("read")
        self.consume_token("(")
        
        self.consume_token(token_id=100)
        if self.peek_token(","):
            while self.peek_token(","):
                self.consume_token(",")
                self.consume_token(token_id=100)

        self.consume_token(")")
        return

    
    def write_statement(self):
        self.consume_token("write")
        self.consume_token("(")
        
        self.expression()
        if self.peek_token(","):
            while self.peek_token(","):
                self.consume_token(",")
                self.output_value()

        self.consume_token(")")

    def output_value(self):
        self.expression()

    def structured_statement(self):
        if self.peek_token("begin"):
            self.compound_statement()

        elif self.peek_token("if"):
            self.if_statement()

        elif self.peek_token("while"):
            self.while_statement()

    def expression(self):
        self.simple_expression()
        
        if self.next_tokens('<', '>', "<>", "=", ">=", "<="):
            self.relational_operator()

            self.simple_expression()


    def simple_expression(self):
        self.sign()
        self.term()
        
        if self.lexical_components.peek().token in {'+', '-', 'or'}:

            while self.lexical_components.peek().token in {'+', '-', 'or'}:
                self.adding_operator()
                self.term()
        return


    def term(self):
        self.factor()
        if self.lexical_components.peek().token in {'div', '*', 'and'}:
            while self.lexical_components.peek().token in {'div', '*', 'and'}:
                self.multiplying_operator()
                self.factor()

        return

    def factor(self):
        if self.peek_token(token_id=100):
            self.consume_token(token_id=100)
            return

        elif self.peek_token("not"):
            self.consume_token("not")
            self.factor()

        elif self.peek_token("not"):
            self.consume_token("not")
            self.factor()

        elif self.peek_token("("):
            self.consume_token("(")
            self.expression()
            self.consume_token(")")
            return 
        
        else:
            self.constant()
            return

    def while_statement(self):
        self.consume_token("while")
        self.expression()
        self.consume_token("do")
        self.statement()

    def if_statement(self):
        self.consume_token("if")
        self.expression()
        self.consume_token("then")
        self.statement()
        
        if self.peek_token("else"):
            self.consume_token("else")
            self.statement()

    def sign(self):
        if self.peek_token("+"):
            self.consume_token("+")

        elif self.peek_token("-"):
            self.consume_token("-")

        else:
            return

    def adding_operator(self):
        if self.peek_token("+"):
            self.consume_token("+")

        elif self.peek_token("-"):
            self.consume_token("-")

        elif self.peek_token("or"):
            self.consume_token("or")

    def multiplying_operator(self):
        if self.peek_token("*"):
            self.consume_token("*")

        elif self.peek_token("div"):
            self.consume_token("div")

        elif self.peek_token("and"):
            self.consume_token("and")

    def relational_operator(self):
        if self.peek_token("="):
            self.consume_token("=")

        elif self.peek_token("<>"):
            self.consume_token("<>")
        
        elif self.peek_token("<"):
            self.consume_token("<")
        
        elif self.peek_token("<="):
            self.consume_token("<=")
        
        elif self.peek_token(">="):
            self.consume_token(">=")

        elif self.peek_token(">"):
            self.consume_token(">")

    def constant(self):
        #Constant identifier"

        if self.peek_token(token_id=100):
            self.consume_token(token_id=100)

        #Integer
        elif self.peek_token(token_id=101):
            self.consume_token(token_id=101)

        #Real
        elif self.peek_token(token_id=102):
            self.consume_token(token_id=102)
        
        #Character constant
        elif self.peek_token(token_id=118):
            self.consume_token(token_id=118)
