
def CharCount(word):
    dict={}
    for i in word:
        dict[i]=dict.get(i,0)+1
    return dict



def VWords(validWords,char_list):
    for word in validWords:
        flag = 1
        charCnt = CharCount(word)
        for key,val in charCnt.items():
            if key not in char_list:
                flag = 0
            else:
                if(char_list.count(key) != charCnt[key]):
                    flag = 0                

        if(flag == 1):
            print(word)
        
            
        

if __name__ == "__main__":
    validWords = ["go","bat","me","eat","goal","boy", "run"]
    char_list = ['e','o','b', 'a','m','g', 'l']
    VWords(validWords,char_list)
