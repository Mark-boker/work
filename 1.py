import math
import random
import re

import nltk.corpus
from nltk import *
from nltk.corpus import inaugural,brown



def qifuprinciple(text):
    result = FreqDist()#运用nltk本身的一个词频字典构建方法
    wordArray = text
    freqdist = FreqDist([word.lower() for word in wordArray])
    for key in freqdist:
        result[key] = math.log10(freqdist[key])#词频字典使用对数刻度

    result.plot(150)#取前150个词频
    sort_words = sorted(freqdist.items(), key=lambda item: item[1], reverse=True)
    print(type(sort_words))
    x = sort_words[49][1] / sort_words[149][1]
    print(x)
    return result

def newText():
    text = ""
    for i in range(0,10000):#将字符累积成一个很长的字符串
        str = ""
        for i in range(1,random.randint(1,10)):
            char = random.choice("abcdefghijklmnopqrstuvwxyz")
            str += char
        text += str+"0"
    text2 = re.split("0",text)
    return text2

if __name__ == '__main__':

    # 1(1)
    result = qifuprinciple(brown.words())
    # 1(2)
    result = qifuprinciple(newText())



