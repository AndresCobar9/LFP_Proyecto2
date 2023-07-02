all_grammars = []
class Grammar:
    
    def __init__(self, name, non_terminals, terminals, start_symbol, productions):
        self.name = name
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.start_symbol = start_symbol
        self.productions = productions
   

    def __str__(self):
        return f"Nombre: {self.name}\n" \
               f"No Terminales: {', '.join(self.non_terminals)}\n" \
               f"Terminales: {', '.join(self.terminals)}\n" \
               f"No Terminal Inicial: {self.start_symbol}\n" \
               f"Producciones:\n{self._format_productions()}"

    def _format_productions(self):
        return '\n'.join(self.productions)    
    
def get_all():

    return all_grammars

