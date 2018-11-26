class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #lets check if the first character for pattern is ? or not
        import numpy as np
       
        isvisited=np.zeros((len(s)+1, len(p)+1))
        isvisited[0][0] = 1;
        for j in range(1, len(p)+1) :
            
            if (p[j - 1] == '*') :
                isvisited[0][j] = isvisited[0][j - 1]; 
                           
        for i in range(1, len(s)+1):
            
            for j in range(1, len(p)+1):
                
                if (p[j - 1] == '*'):
                    isvisited[i][j] = isvisited[i][j - 1] or isvisited[i - 1][j]; 
                elif (p[j - 1] == '?' or s[i - 1] == p[j - 1]) :
                    isvisited[i][j] = isvisited[i - 1][j - 1]; 
                else : isvisited[i][j] = False        
        output=False
        if(isvisited[len(s)][len(p)]==1):
            output=True
                           
        return (output)
