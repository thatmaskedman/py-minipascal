class SyntacticError(Exception):

    errors = {
        100: "Identifier was expected.",
        101: "Integer number was expected.",
        102: "Real number was expected",
        118: "String was expected"
    }

    def __init__(self, component, lines, expected="", expected_id=0):
        self.component = component
        self.lines = lines
        self.expected = expected
        self.expected_id = expected_id
    
    def __str__(self):
        if self.expected != "":
            return (
                    f"\n{self.lines[self.component.li_num - 1][:-1]}\n"
                    f"Syntax error at line {self.component.li_num}: "
                    f"\"{self.expected}\" was expected, got \"{self.component.token}\"") 
        else:
            return (
                    f"\n{self.lines[self.component.li_num - 1][:-1]}\n"
                    f"Syntax error at line {self.component.li_num}: "
                    f"{self.errors[self.expected_id]}" 
                )
