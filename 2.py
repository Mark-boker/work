import nltk
from nltk.corpus import wordnet as wn

if __name__ == "__main__":
    n = 0.0 # 名词
    v = 0.0 # 动词
    a = 0.0 # 形容词
    r = 0.0 # 副词

    #义项
    n_s = 0.0
    v_s = 0.0
    a_s = 0.0
    r_s = 0.0


    for i in wn.words():#通过方法取出不同词性单词义项数目
        n_s += len(wn.synsets(i, 'n'))
        v_s += len(wn.synsets(i, 'v'))
        a_s += len(wn.synsets(i, 'a'))
        r_s += len(wn.synsets(i, 'r'))


    for ss in wn.all_synsets():#通过方法取出不同词性单词数目
        if ss.pos() == 'n':
            n += 1.0
        elif ss.pos() == 'v':
            v += 1.0
        elif ss.pos() == 'a':
            a += 1.0
        elif ss.pos() == 'r':
            r += 1.0


    print("============================================")
    print("n_s:",n_s)
    print("n:",n)
    print("n_s/n:",n_s/n)
    print("============================================")
    print("v_s:",v_s)
    print("v:",v)
    print("v_s/v:",v_s/v)
    print("============================================")
    print("a_s:",a_s)
    print("a:",a)
    print("a_s/a:",a_s/a)
    print("============================================")
    print("r_s:",r_s)
    print("r:",r)
    print("r_s/r:",r_s/r)



