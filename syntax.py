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
            print(consumed)
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
            # if token_id is None:
            #     if consumed.token == token:
            #         return
            #     else:
            #         raise SyntacticError(consumed, self.lines, token)
            # else:
            #     if consumed.token_id == token_id:
            #         return
            #     else:
            #         raise SyntacticError(consumed, self.lines, expected_id=token_id)
        # except SyntacticError:
        #     error = f"{self.lines[consumed.li_num - 1]}"[:-1] +
        #           f"Syntax error at line {consumed.li_num}: {token} was expected.",
        #           sep="\n")
        #     quit()

    def peek_token(self, token="", token_id=0):
        if token_id == 0:
            return self.lexical_components.peek().token == token

        else:
            return self.lexical_components.peek().token_id == token_id

    def is_inset(self,items):
        return self.lexical_components.peek().token in items

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
        
        if self.peek_token("var"):
            #<Identifier>
            self.consume_token("var")
            self.variable_declaration()
            self.consume_token(";")
            if self.peek_token(token_id=100):
                while self.peek_token(token_id=100):
                    self.variable_declaration()
                    self.consume_token(";")

    def variable_declaration(self):
        # <variable declaration> ::= <identifier > { , <identifier> } : <identifier>

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

        self.consume_token("begin")
        self.statement()
        

        if self.peek_token(";"):
            while self.peek_token(";"):
                self.consume_token(";")
                self.statement()
        
        self.consume_token("end")
    
    def statement(self):
        #<statement> ::= <simple statement> | <structured statement>  

        # print(self.lexical_components.peek())

        if self.peek_token(token_id=100) or self.is_inset({"read", "write"}):
            self.simple_statement()
        
        elif self.lexical_components.peek().token in {"begin", "if", "while"}:
            self.structured_statement()
    

    def simple_statement(self):
        # <simple statement> ::= <assignment statement> |  
        #                        <read statement> | <write statement>  

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
        if self.peek(","):
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
                self.expression()

        self.consume_token(")")

    def structured_statement(self):
        if self.peek_token("begin"):
            self.statement_part()

        elif self.peek_token("if"):
            self.if_statement()

        elif self.peek_token("while"):
            self.while_statement()

    def expression(self):
        self.simple_expression()
        
        if self.lexical_components.peek().token in {'<', '>', "<>", "=", ">=", "<="}:
            self.relational_operator()

            self.simple_expression()


    def simple_expression(self):
        # <simple expression> ::= <sign> <term> { <adding operator> <term> } 
        

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
        #<factor> ::= <variable> | <constant> | ( <expression> ) | not <factor>  

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
        #<while statement> ::= while <expression> do <statement>  
 
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
            return

        elif self.peek_token("-"):
            self.consume_token("-")
            return

        else:
            return

    def adding_operator(self):
        if self.peek_token("+"):
            self.consume_token("+")
            return

        elif self.peek_token("-"):
            self.consume_token("-")
            return

        elif self.peek_token("or"):
            self.consume_token("or")
            return

    def multiplying_operator(self):
        if self.peek_token("*"):
            self.consume_token("*")
            return
        elif self.peek_token("div"):
            self.consume_token("div")
            return
        elif self.peek_token("and"):
            self.consume_token("and")
            return

    def relational_operator(self):
        if self.peek_token("="):
            self.consume_token("=")
            return
        elif self.peek_token("<>"):
            self.consume_token("<>")
            return
        
        elif self.peek_token("<"):
            self.consume_token("<")
            return
        
        elif self.peek_token("<="):
            self.consume_token("<=")
            return
        
        elif self.peek_token(">="):
            self.consume_token(">=")
            return

        elif self.peek_token(">"):
            self.consume_token(">")
            return

    def constant(self):
        #Constant identifier"

        if self.peek_token(token_id=100):
            self.consume_token(token_id=100)
            return

        #Integer
        elif self.peek_token(token_id=101):
            self.consume_token(token_id=101)
            return

        #Real
        elif self.peek_token(token_id=102):
            self.consume_token(token_id=102)
            return
        
        #Character constant
        elif self.peek_token(token_id=118):
            self.consume_token(token_id=118)
            return

