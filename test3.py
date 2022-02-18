
#%%
from konlpy.tag import Twitter 
from collections import Counter
import pandas as pd
from konlpy.tag import Okt

df = pd.read_csv('./movie_cmt_02.csv')
# df = df.drop(['Unnamed: 0'], axis=1)
# df


df_01 = df['text'][1700:1800].tolist()
df_01

okt = Okt()
nouns = okt.nouns(text) # 명사만 추출
nouns = nouns[:50]





df_02 = [x for x in df_01 if pd.isnull(x) == False]
df_02


twitter = Twitter()
word_01 = []

for sentence in df_02: 
    word_01.append(twitter.pos(sentence))




word_01 = [x for x in word_01 if len(x) > 1]



#%%

word_01[0][0][0]

#%%

noun_adj_adv_list=[] 
for sentence in word_01 : 
    for word, tag in sentence : 
        if len(tag)  and ("영화" not in word): 
            noun_adj_adv_list.append(word)

noun_adj_adv_list

count = Counter(noun_adj_adv_list)
words = dict(count.most_common())


words

# %%
words['역사상']
# %%



okt = Okt()
nouns = okt.nouns(text) # 명사만 추출
nouns = nouns[:50]