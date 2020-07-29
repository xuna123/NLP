import numpy as np
import nltk
import string
import os
from collections import Counter 
from nltk.corpus import stopwords
from nltk.stem.porter import * #分词算法
from sklearn.feature_extraction.text import TfidfVectorizer

#1) 读取文档，去掉所有标点字符，分割为一维词向量
def get_tokens():
    #with open('C:/Users/xn/BigDataAnalytics/TF-IDF/shake1.txt', 'r') as shakes:
    with open('C:/Users/xn/BigDataAnalytics/TF-IDF/shake1.txt', 'r') as shakes:
        text = shakes.read()
        lowers = text.lower()
        for i in string.punctuation: # string.punctuation  所有的标点字符 '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
            lowers = lowers.replace(i,' ')#将所有标点字符替换为空格
        #print(type(lowers))
        #no_punctuation = lowers.translate(None,string.punctuation) #过滤掉所有的标点符号，生成字符串文本
        #print (lowers)
        tokens = nltk.word_tokenize(lowers) # 将文本分割为单个词语存放在tokens列表中
    return tokens


#2) 去掉英文停用词
tokens = get_tokens() #一维列表
filtered = []
for w in tokens:
    if w not in stopwords.words('english'):#调用NLTK的停用词库，去掉文本中的停用词
        filtered.append(w)  
count = Counter(filtered)#利用Python的collections包下Counter的类统计每个数据出现的个数,生成 词：出现次数 的键值对字典


#3) 对英文进行分词处理，能够实现还原英文单词原型，比如 boys 变为 boy 等
'''
在英语的语言形式中经常有不同的变形，例如apple和apples表示单复数，process和processing的分词和动名词形式，这些单词往往在语言表示的意思上有相同的含义，所以对类似进行变形过的词汇进行词干抽取，可以提取出有相同词干词义的词
'''
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

stemmer = PorterStemmer()
stemmed = stem_tokens(filtered, stemmer)
count = Counter(stemmed)#分词后的词字典


# 1) 2) 3)为文本的预处理工作
#print(stemmed)
with open('C:/Users/xn/BigDataAnalytics/TF-IDF/shake1.txt', 'r') as shakes:
    corpus = shakes.read()
    corpus_lowers = corpus.lower()
    for i in string.punctuation: # string.punctuation  所有的标点字符 '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
            corpus_lowers = corpus_lowers.replace(i,' ')
            
tfidf_vec = TfidfVectorizer()

corpus_lows = []
corpus_lows.append(corpus_lowers)
#print(corpus_lowers)
tfidf_matrix = tfidf_vec.fit_transform(corpus_lows)#利用fit_transform得到tf-idf矩阵
print(tfidf_vec.get_feature_names()[71])# 输出所提取的文本关键字，也就是特征，或者说词/句子

print(tfidf_vec.vocabulary_)# 输出文本的关键字和其索引


print(tfidf_matrix)
'''
const

0 const属于第一篇文章
71 const 在tfidf_vec.get_feature_names()中下标为71
0.007277588641546741 const的tfidf值
(0, 71)	0.007277588641546741
 '''

