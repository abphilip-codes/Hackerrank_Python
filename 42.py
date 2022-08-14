# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    l = len(string)
    t = int(l*(l+1)/2)
    k = sum((l-z) for z in range(l) if(string[z] in "AEIOU"))   
    
    if(t>2*k): print(f"Stuart {t-k}")
    elif(t<2*k): print(f"Kevin {k}")
    else: print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)