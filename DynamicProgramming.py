def wordBreak(dictionary, str, lookup, result):
    n = len(str)
    if n == 0:
        return True
    if lookup[n] == -1:
        lookup[n] = 0
        for i in range(1, n + 1):
            prefix = str[:i]
            if prefix in dictionary and wordBreak(dictionary, str[i:], lookup, result):
                lookup[n] = 1
                result.insert(0, prefix)
                return True
    return lookup[n] == 1
 
import time
if __name__ == '__main__':
    start = time.time()
    # local dictionary
    dictionary = [
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
    for i in range (1, len(input)-1):
        str = ""
        str += (input[0])
        for j in range (len(input)-1):
            now += i
            if (now > len(input)-1):
                now = now % (len(input)-1)
            str+=(input[now])
        str = str.replace('_','')
        lookup = [-1] * (len(str) + 1)
        result = []
        if wordBreak(dictionary, str, lookup, result):
            print("The decrypted message is: ")
            for words in result:
                print(words, end=" ")
            print()
            break
        else:
            if (i == len(input)-2):
                print("The string can't be segmented")
    end = time.time()
    print(round(end-start, 8), "seconds are needed to find the solution above")
    