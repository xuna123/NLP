#方法一 ：普通方法计算TF-IDF 
import math
import re


# 1) 分词并过滤停用词
filter_word = ['of', 'a', 'is','in','to','or'] #自定义要过滤到的停用词

def transform_vector(corpus):
    all_essay = []
    for essay in corpus:
        tmp_essay = re.split("[ |,]",essay)   #分割后文章1['tf', 'idf', 'short', 'form', 'of', 'term', 'frequency', 'inverse', 'document', 'frequency']
        tmp1_essay = []
        for x in tmp_essay:
            if x not in filter_word:
                tmp1_essay.append(x)
        all_essay.append(tmp1_essay)
    return all_essay


# 2) 统计词频
def count_word_number(transform_essay):
    word_number = []
    for essay in transform_essay:
        tmp_word_number = {}
        for x in essay:
            if not tmp_word_number.get(x):#当前词x不在当前文章的字典中,返回假
                tmp_word_number.update({x:1}) #添加
            elif tmp_word_number.get(x):
                tmp_word_number[x] += 1
        word_number.append(tmp_word_number)
    return word_number
    
    
# 3) 计算TF值
def tf(x, essay):
    return (essay.get(x))/(sum(word_num[0].values()))


# 4) 计算IDF值
def idf(x, word_num):
    cnt = 0 #统计含有指定单词的文章的篇数
    for essay in word_num:
        if essay.get(x):
            cnt += 1
    return math.log((len(word_num))/(cnt+1))


# 5) 计算TF-IDF
def tf_idf(x,essay, word_num):
    return tf(x, essay) * idf(x,word_num)
    

#自定义语料库
corpus = [
    "tf idf,short form of term frequency,inverse document frequency", #文章1
    "is a numerical statistic that is intended to reflect how important",#文章2
    "a word is to a document in a collection or corpus"#文章3
]

transform_essay = transform_vector(corpus) #转化为二维向量存储

'''
#print(transform_essay[0])
['tf', 'idf', 'short', 'form', 'term', 'frequency', 'inverse', 'document', 'frequency']
'''
word_num = count_word_number(transform_essay) #转化为 {词：词出现的次数}的字典

'''
print(word_num[0])
{'tf': 1, 'idf': 1, 'short': 1, 'form': 1, 'term': 1, 'frequency': 2, 'inverse': 1, 'document': 1}

print (word_num[0].get('tf'),sum(word_num[0].values()),tf('tf',word_num[0]))
1 9 0.1111111111111111

print (idf('tf', word_num)) 'tf'的idf值
0.4054651081081644
'''
n = 1
for essay in word_num:
    print("第{}篇文章".format(n))
    n += 1
    for x,cnt in essay.items():
        print ("词 {}, tf值 {}， idf值 {}， tf-idf值 {}".format(x, tf(x,essay), idf(x,word_num), tf_idf(x,essay,word_num)))
        
'''
第1篇文章
词 tf, tf值 0.1111111111111111， idf值 0.4054651081081644， tf-idf值 0.04505167867868493
词 idf, tf值 0.1111111111111111， idf值 0.4054651081081644， tf-idf值 0.04505167867868493
词 short, tf值 0.1111111111111111， idf值 0.4054651081081644， tf-idf值 0.04505167867868493
词 form, tf值 0.1111111111111111， idf值 0.4054651081081644， tf-idf值 0.04505167867868493
词 term, tf值 0.1111111111111111， idf值 0.4054651081081644， tf-idf值 0.04505167867868493
词 frequency, tf值 0.2222222222222222， idf值 0.4054651081081644， tf-idf值 0.09010335735736986
词 inverse, tf值 0.1111111111111111， idf值 0.4054651081081644， tf-idf值 0.04505167867868493
词 document, tf值 0.1111111111111111， idf值 0.0， tf-idf值 0.0
第2篇文章
词 numerical, tf值 0.1111111111111111， idf值 0.4054651081081644， tf-idf值 0.04505167867868493
词 statistic, tf值 0.1111111111111111， idf值 0.4054651081081644， tf-idf值 0.04505167867868493
词 that, tf值 0.1111111111111111， idf值 0.4054651081081644， tf-idf值 0.04505167867868493
词 intended, tf值 0.1111111111111111， idf值 0.4054651081081644， tf-idf值 0.04505167867868493
词 reflect, tf值 0.1111111111111111， idf值 0.4054651081081644， tf-idf值 0.04505167867868493
词 how, tf值 0.1111111111111111， idf值 0.4054651081081644， tf-idf值 0.04505167867868493
词 important, tf值 0.1111111111111111， idf值 0.4054651081081644， tf-idf值 0.04505167867868493
第3篇文章
词 word, tf值 0.1111111111111111， idf值 0.4054651081081644， tf-idf值 0.04505167867868493
词 document, tf值 0.1111111111111111， idf值 0.0， tf-idf值 0.0
词 collection, tf值 0.1111111111111111， idf值 0.4054651081081644， tf-idf值 0.04505167867868493
词 corpus, tf值 0.1111111111111111， idf值 0.4054651081081644， tf-idf值 0.04505167867868493
'''
