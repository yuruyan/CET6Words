# -*- coding:utf-8 -*-
import random
import collections

wordlist = []  # 单词列表
existed = []  # 抽取过的单词
with open('./../src/words.txt', encoding='utf-8') as f:
    wordlist = collections.deque(list(f.read().strip().split('\n')))
    
count = 0  # 计数器
list_len = len(wordlist)  # 列表中长度
print('length: ' + str(list_len))
while count < list_len:
    count += 1
    word = random.choice(wordlist)
    wordlist.remove(word)
    print(count, word, end='')
    input('')

# while len(existed) != len(wordlist):
#     word = random.choice(wordlist)
#     # word = wordlist[random.randint(0, len(wordlist) - 1)]
#     if word not in existed:
#         existed.append(word)
#         print(count, word, end='')
#         count += 1
#         input('')
"""
/dictionary/word/query/web
610000061616848254609this%20way
7ece94d9f9c202b0d2ec557dg4r9bc

0b6764a9bdef077d06aa2d6d9c483de6
0b6764a9bdef077d06aa2d6d9c483de6

/dictionary/word/query/web610000061616848254609this%20way7ece94d9f9c202b0d2ec557dg4r9bc
"""