class Scanner:
    def __init__(self,input):
        self.matrix = [dict() for _ in range(16)]
        self.term = [False] * 16
        self.mark=[False] *16
        self.star=[False]*16
        self.other=[0] *16
        self.message=['']*16
        self.keywords= ["if", "else", "void", "int", "while", "break", "switch", "default", "case", "return","continue"]


        self.currentState=0
        self.currentStr=""
        self.commentAll=False
        self.lastComment=-1
        self.tk_counter=1



        self.input_file =open(input,'r')
        self.close_file=self.input_file.close()







        self.symbol=[';', ':' , '[', ']', '(',' )', '{', '}', '+', '-' ,'<']
        self.digit= map(chr, range (ord ('0'), ord ('9')+1))
        self.letter=map(chr, range (ord ('a'), ord ('z')+1)) or map (chr, range (ord ('A'), ord ('Z')+1))
        self.whitespace=['\n','\t']


    def is_keyword(self,str):
        return str in self.keywords

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




    def diffrent_type(self,character):
        if(character in self.letter):
            return "letter"
        if (character in self.digit):
            return  "digit"
        if (character in self.symbol) or (character in self.whitespace):
            return character

        return '!'


    def find_next_character(self,character):
        if character == '\n' or character == '\t':
            if not self.commentAll:
                self.currentState=0

            self.tk_counter=self.tk_counter+1
            self.commentAll=False

            finish= False

            while not finish:
                finish=True









