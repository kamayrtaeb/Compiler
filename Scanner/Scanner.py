class Scanner:
    def __init__(self,input):
        self.matrix = [dict() for range 16]
        self.finalState = [0] * 16
        self.other=[0] *16



        self.symbol=[';', ':' , '[', ']', '(',' )', '{', '}', '+', '-' ,'<']
        self.digit= map (chr, range (ord ('0'), ord ('9')+1))
        self.letter=map (chr, range (ord ('a'), ord ('z')+1)) or map (chr, range (ord ('A'), ord ('Z')+1))




    def defrrentType(self ,character):
        if (character in self.letter):
            return 'letter'
        elif (character in self.digit):
            return 'digit'
        elif(character in self.symbol):
            return character


    def state(self):
        self.matrix[0]["letter"] =1
        self.matrix[0]["digit"]=3
        self.matrix[0][":"]=5
        self.matrix[0][";"]=5
        self.matrix[0][","]=5
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