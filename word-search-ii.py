class Solution:
    def recursivefind(self,isvisited, characterpassed, row, column,wordscollection,prefixset,rows,columns,board,output):
        #add to output if the generated word via self recursive function is in words
        if characterpassed in wordscollection:
                output.add(characterpassed)
        # if the character passed is not prefix, return back for next character. This helps to avoid uncessary recursive
        if characterpassed not in prefixset:
            return
        
        #set the isvisted to True for word in prefix set
        isvisited[row][column] = True
        #for each character we get the adjacent neighbours and loop for over to check if the words is reached. if not we return
        neighbours=(self.Neighbours(row,column,rows,columns))
        
        for neighboursx, neighboursy in neighbours:          
            if (isvisited[neighboursx][neighboursy]==0):
                self.recursivefind(isvisited, characterpassed+board[neighboursx][neighboursy], neighboursx, neighboursy,wordscollection,prefixset,rows,columns,board,output)
        
        
        isvisited[row][column] = False
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        import numpy as np
        rows = len(board)
        
        columns = len(board[0])
        
        #Define varibales
        output = set()# this will be return
        wordscollection = set(words)#set of unique words
        prefixset=set()
        #Track the position visisted
        isvisited=np.zeros((rows, columns))
        
        #prefix of all the words will be created for example for word pea, p, pe will be stored in it
    
        for word in words:
            #print(word)
            for i in range(len(word)-1):
                prefixset.add(word[:i+1])
        
        for row in range(rows):
            for column in range(columns):
                self.recursivefind(isvisited, board[row][column], row, column,wordscollection,prefixset,rows,columns,board,output)
        
               
        return list(output)
    
    def Neighbours(self,x,y,lengthx,lengthy):
        '''
        type x: x cordinate of the character passed
        type y: y cordinate of the character passed
        type lengthx: rowlength of the board(2d array)
        type lengthy: rowlength of the board(2d array)
        '''
        Neighbours = []
 
        for ix, iy in ([[-1, 0], [0, -1], [0, 1], [1, 0]]):
            xnew, ynew=x+ix,y+iy
            if xnew>=0 and xnew<lengthx and ynew>=0 and ynew<lengthy:
                Neighbours.append([xnew,ynew])
        
        return Neighbours
