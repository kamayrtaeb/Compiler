import os.path


class Scanner:
    def __init__(self,input):
        self.matrix = [dict() for _ in range(16)]
        self.term = [False] * 16
        self.mark=[False] *16
        self.star=[False]*16
        self.other=[0] *16
        self.message=['']*16
        self.keywords= ["if", "else", "void", "int", "while", "break", "switch", "default", "case", "return","continue"]
        self.symbolList=["if", "else", "void", "int", "while", "break", "switch", "default", "case", "return"]


        self.currentState=0
        self.currentStr=""
        self.commentAll=False
        self.lastComment=-1
        self.tk_counter=1
        self.commentline=False
        self.lexicalErrors=[list() for _ in range(10000)]



        self.input_file =open(input,'r')
        self.close_file=self.input_file.close()
        self.allTokens=list()
        self.newTokens=list()
        self.tokens=[list() for _ in range(10000)]


        self.symbol=[';', ':' , '[', ']', '(',' )', '{', '}', '+', '-' ,'<']
        self.digit= map(chr, range (ord ('0'), ord ('9')+1))
        self.letter=map(chr, range (ord ('a'), ord ('z')+1)) or map (chr, range (ord ('A'), ord ('Z')+1))
        self.whitespace=['\n','\t']


    def is_keyword(self,str):
        return str in self.keywords

    def symbolTable(self,filename):
        with open(filename, 'w') as ST:
            st_counter = 0
            for s in self.symbolList:
                st_counter += 1
                ST.write(str(st_counter) + ".\t" + s + '\n')

    def token(self,filename):
        with open(filename, 'w') as f:
            for line_id in range(10000):
                if not self.tokens[line_id]:
                    continue
                f.write(str(line_id) + '.\t')
                f.write(' '.join(f'({token_type}, {string})' for token_type, string in self.tokens[line_id]))
                f.write('\n')

    def lexicalErrors(self, file_name):
        if self.currentState == 11 or self.currentState == 13:
            self.lexicalErrors[self.lastComment].append( "(" + self.currentStr[:7] + "..., " + "Unclosed comment) ")

        with open(file_name, 'w') as LE:
            flag = False
            for i in range(10000):
                if len(self.lexicalErrors[i]) == 0:
                    continue

                flag = True
                LE.write(str(i) + ".\t")
                LE.write(' '.join(s[0: -1] for s in self.lexicalErrors[i]))
                LE.write('\n')

            if not flag:
                LE.write("There is no lexical error.")

    def state(self):
        self.matrix[0]["letter"] =1
        self.matrix[0]["digit"]=3
        self.matrix[0][":"]=5
        self.matrix[0][";"]=5
        self.mat[0][","] = 5
        self.mat[0]["["] = 5
        self.mat[0]["]"] = 5
        self.mat[0]["("] = 5
        self.mat[0][")"] = 5
        self.mat[0]["{"] = 5
        self.mat[0]["}"] = 5
        self.mat[0]["+"] = 5
        self.mat[0]["-"] = 5
        self.mat[0]["<"] = 5
        self.mat[0]["="] = 6
        self.mat[0]["*"] = 8
        self.mat[0]["/"] = 10
        self.mat[0][" "] = 15
        self.mat[0]["\n"] = 15
        self.mat[0]["\t"] = 15
        self.mat[0]["\r"] = 15
        self.mat[0]["\f"] = 15
        self.mat[0]["\v"] = 15
        self.other[0]=-1
        self.message="error"

        self.matrix[1]["letter"]=1
        self.matrix[1]["digit"]=1
        self.other[1]=2

        self.mark[2]=True
        self.term[2]=True
        self.star[2]=True

        self.matrix[3]["digit"]=3
        self.other[3]=4
        self.matrix[3]["letter"]=-1

        self.term[4]=True
        self.mark[4]=True
        self.star[4]=True

        self.term[5]=True
        self.matrix[6]["="]=7
        self.term[7]=True
        self.other[6]=9
        self.matrix[8]["/"]=-1
        self.other[8]=9
        self.term[9]=True
        self.mark[9]=True
        self.star[9]= True

        self.matrix[10]["/"]=11
        self.matrix[11]["\n"]=12
        self.other[11]=11
        self.matrix[10]["*"]=13
        self.other[10]=-1
        self.message[10]="error"
        self.term[12]=True

        self.matrix[13]["*"]=14
        self.other[13]=13
        self.matrix[14]["*"]=14
        self.matrix[14]["/"]=12
        self.other[14]=13

        self.term[15]=True





    def addToken(self,tokenType, str):
        self.allTokens.append((tokenType,str))
        self.newTokens.append(self.tokens[-1])
        self.tokens[self.tk_counter].append((tokenType,str))

    def diffrent_type(self,character):
        if(character in self.letter):
            return "letter"
        if (character in self.digit):
            return  "digit"
        if (character in self.symbol) or (character in self.whitespace):
            return character

        return '!'


    def get_next_token(self):
        if self.newTokens:
            t1,t2=self.newTokens[0]
            if t1 in {'KEYWORD', 'SYMBOL'}:
                t1,t2=t2,t1
            self.newTokens.pop(0)
            return t1,t2
        while True:
            character=self.input_file.read(1)
            if character == '$' or character=='':
                return '$','FILE END'

            self.find_next_character(character)

            if self.newTokens:
                t1, t2 = self.newTokens[0]
                if t1 in {'KEYWORD', 'SYMBOL'}:
                    t1, t2 = t2, t1
                self.newTokens.pop(0)
                return t1, t2



    def find_next_character(self,character):
        if character == '\n' or character == '\t':
            if not self.commentAll:
                self.currentState=0

            self.tk_counter=self.tk_counter+1
            self.commentline=False

            finish= False

            while not finish:
                finish=True

                comment=False
                if self.currentState == 11 or self.currentState ==13:
                    comment=True

                self.currentStr =self.currentStr + character

                a=self.diffrent_type(character)
                if not self.commentAll and not self.commentline and a== '!':
                    if self.currentStr[0:-1] == "/":
                        if len(self.currentStr[0:-1]) >0:
                            self.lexicalErrors[self.tk_counter].append( "(" + self.currentStr[0:-1] + ", " + "Invalid input" + ") ")
                        self.lexicalErrors[self.tk_counter].append( "(" + self.current_string[0:-1] + ", " + "Invalid input" + ") ")
                        self.currentState=0
                        self.currentStr=""
                    else:
                        self.lexicalErrors[self.tk_counter].append( "(" + self.current_string[0:-1] + ", " + "Invalid input" + ") ")
                        self.currentStr=""
                        self.currentState=0
                elif a in self.matrix[self.currentState]:
                    if self.matrix[self.currentState][a]==-1:
                        if character == ' ' or character =='\n' or character =='\t':
                            self.currentStr=self.currentStr[0:-1]
                            self.lexicalErrors[self.tk_counter].append( "(" + self.current_string[0:-1] + ", " + "Invalid input" + ") ")

                    self.currentState=self.matrix[self.currentState][a]
                else:
                    if self.other[self.currentState]==-1 and self.currentState==10 :
                        finish=False
                        self.currentStr=self.currentStr[0:-1]
                        self.lexicalErrors[self.tk_counter].append( "(" + self.current_string[0:-1] + ", " + "Invalid input" + ") ")
                    elif self.other[self.currentState]==-1:
                        if character ==' ' or character == '\n' or character =='\t':
                            self.currentStr=self.currentStr[0:-1]
                        self.lexicalErrors[self.tk_counter].append( "(" + self.current_string[0:-1] + ", " + "Invalid input" + ") ")

                    self.currentState=self.other[self.currentState]
                    if self.currentState==-1:
                        self.currentState=0
                        self.currentStr=""
                if self.currentState == 11:
                    self.commentline=True
                    if not comment:
                        self.lastComment=self.tk_counter
                if self.currentState==13:
                    self.commentAll=True
                    if not comment:
                        self.lastComment=self.tk_counter
                if self.term[self.currentState]:
                    if self.star[self.currentState]:
                        finish=False
                        self.currentStr=self.currentStr[0:-1]


                    if self.currentState==2:
                        flag=False
                        for s in self.symbolList:
                            if s== self.currentStr:
                                flag=True


                        if not self.is_keyword(self.currentStr) and not flag:
                            self.symbolList.append(self.currentStr)

                        if self.is_keyword(self.currentStr):
                            self.addToken("KEYWORD", self.currentStr)
                        else:
                            self.addToken("ID",self.currentStr)

                    elif self.currentState==4:
                        self.addToken("NUM",self.currentStr)
                    elif self.currentState ==5 or self.currentState==7 or self.currentState==9:
                        self.addToken("SYMBOL",self.currentStr)

                    elif self.currentState==12 :
                        self.commentAll= False
                        self.commentline=False

                    self.currentStr=""
                    self.currentState=0

