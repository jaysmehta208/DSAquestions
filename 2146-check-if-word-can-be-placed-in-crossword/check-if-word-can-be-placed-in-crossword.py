class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        all_words = []
        for i in range(len(board)):
            word1 = ""
            for j in range(len(board[0])):
                if board[i][j] != "#":
                    word1+=board[i][j]
                else:
                    all_words.append(word1)
                    word1 = ""
            if (word1!= ""):
                all_words.append(word1)
        for i in range(len(board[0])):
            word1 = ""
            for j in range(len(board)):
                if board[j][i] != "#":
                    word1+=board[j][i]
                else:
                    all_words.append(word1)
                    word1 = ""
            if (word1!= ""):
                all_words.append(word1)
        print(all_words)
        for i in range(len(all_words)):
            flag = True
            if (len(all_words[i]) == len(word)):
                for j in range(len(word)):
                    if all_words[i][j]==" ":
                        continue
                    else:
                        if all_words[i][j] != word[j]:
                            flag = False
            else:
                flag = False
            if (flag == True):
                return True
        for i in range(len(all_words)):
            flag = True
            if (len(all_words[i]) == len(word)):
                for j in range(len(word)):
                    if all_words[i][j]==" ":
                        continue
                    else:
                        if all_words[i][j] != word[len(word) - 1 -j]:
                            flag = False
            else:
                flag = False
            if (flag == True):
                return True
        
        return False
