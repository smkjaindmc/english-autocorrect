from tkinter import *


def editDistanceDp(word1,word2):
    dist=[]  

    l1=len(word1)
    l2=len(word2)
    for i in range(l1+1):
        b=[0]*(l2+1)
        dist.append(b)   # creating a dist matrix of m+1 rows and n+1 columns where m and n are lengths

    for i in range(l1+1):
        dist[i][0]=i

    for j in range(l2+1):       # initialising the matrix
        dist[0][j]=j

    p=0
    q=0
    r=0

    for i in range(1,l1+1):
        for j in range(1,l2+1):
            if(word1[i-1]==word2[j-1]):          # if prefixes are equal then store the top left index
                dist[i][j]= dist[i-1][j-1]
            else:
                p= dist[i][j-1]
                q= dist[i-1][j]
                r= dist[i-1][j-1]
            
                dist[i][j]=min(p,q,r)+1
    

    return dist[l1][l2]

def printDist(dist, l1, l2):

    for i in range(l1+1):
        for j in range(l2+1):
            print(int(dist[i][j]),end=" ")  # printing the initial distance matrix
        print()



def calc(word, numWords):
    
    file = open('1000-dict/1-1000.txt', 'r') 
    lines = file.readlines() 
    file.close()
    dictWordDist = []
    Idx = 0
    
    for line in lines: 
        wordDistance = editDistanceDp(word, line.strip())
        if wordDistance >= 10:
            wordDistance = 9
        dictWordDist.append(str(int(wordDistance)) + "-" + line.strip())
        Idx = Idx + 1

    closestWords = []
    wordDetails = []
    currWordDist = 0
    dictWordDist.sort()
    for i in range(numWords):
        currWordDist = dictWordDist[i]
        wordDetails = currWordDist.split("-")
        closestWords.append(wordDetails[1])
    Lab=Label(root, text="Possible auto-corrected words for "+word+" are :", bg="orange" ,font="none 20 bold underline")
    Lab.pack()
        
    for j in closestWords:
        Lab=Label(root, text=j, bg="orange", font="none 16 bold")
        Lab.pack()




root= Tk()
root.title("English Auto-Correct using edit distance")
root.geometry("500x500")
root.configure(background="orange")
print("Enter a word")
s=input()
calc(s,3)
root.mainloop()






















