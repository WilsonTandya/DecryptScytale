def wordBreak(dict, str, out=""):
    if not str:
        print(out[1:])
        return
    for i in range(1, len(str) + 1):
        prefix = str[:i]
        if prefix in dict:
            wordBreak(dict, str[i:], out + " " + prefix)
 
import time
if __name__ == '__main__':
    start = time.time()
    dict = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "me", "you", "we", "to", "with",
        "please", "help", "write", "read", "think",
        "apples", "bananas", "melons", "mangoes", "mushrooms", "strawberries",
        "can", "give", "and", "not", "do", "want", "build", "together", "houses"
    ]
    #other sample ciphertexts
    #input = "pemlheee_al_sp_"
    #input = "cumeaneeageendasnitbafp_yvhasip_oernavl_"
    input = "dbtheouoevyigleolepnudtmmwhheaaoegnnurigtsavoteneeosdss"

    now = 0
    print("The decrypted message is: ")
    for i in range (1, len(input)-1):
        str = ""
        str += (input[0])
        for j in range (len(input)-1):
            now += i
            if (now > len(input)-1):
                now = now % (len(input)-1)
            str+=(input[now])
        str = str.replace('_','')
        wordBreak(dict, str)
    end = time.time()
    print(round(end-start, 8), "seconds are needed to find the solution above")
    