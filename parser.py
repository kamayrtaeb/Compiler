



class Parser:
    def __init__(self,scanner):
        self.non_terminals=set()
        self.grammar=list()
        self.first_set=dict()
        self.follow_set=dict()
        self.table=dict([(state,dict()) for state in self.non_terminals])
        self.scanner=scanner
        self.errors=list()
        self.root=None


        self.open_grammar()
        self.open_firsts()
        self.open_follows()






    def open_grammar(self):
        with open('grammar.txt','r') as grammar_file:
            for line in grammar_file.readline():
                ls=line.split()
                self.grammar.append((ls[0],ls[2:]))
                self.non_terminals.add(ls[0])

    def open_firsts(self):
        with open('first.txt', 'r') as first_file:
            for line in first_file.readlines():
                ls = line.split()
                self.first_set[ls[0]] = set(ls[1:])


    def open_follows(self):
        with open('follow.txt', 'r') as follow_file:
            for line in follow_file.readlines():
                ls = line.split()
                self.follow_set[ls[0]] = set(ls[1:])