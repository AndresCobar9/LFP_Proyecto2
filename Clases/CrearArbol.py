
import graphviz


def create_derivation_tree_graph(Grammar):
    graph = graphviz.Digraph(comment='Derivation Tree')
    i = 0
    real_left = ""
    for production in Grammar.productions:
        left, right = production.split('::=')
        print(left, right)
        right_symbols = right.split()
        print(right_symbols)
        if i == 0:
            left = left + str(i)
            graph.node(left, left)
        
        elif i > 0:
            left = real_left
            
            
        for symbol in right_symbols:
            
            graph.node(symbol + str(i), symbol)
            graph.edge(left  , symbol + str(i))
            for noterminal in Grammar.non_terminals:
                
                if symbol == noterminal:
                    print("Simbolo no terminal: "+noterminal)
                    real_left = symbol + str(i)
            i += 1
            
            
            
            
        
        
        
    return graph