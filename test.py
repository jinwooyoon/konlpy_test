#%%
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from konlpy.tag import Okt
from PIL import Image
import numpy as np
import pandas as pd
from IPython.display import set_matplotlib_formats
import matplotlib
from IPython.display import set_matplotlib_formats 

matplotlib.rc('font',family = 'Malgun Gothic') 
set_matplotlib_formats('retina') 
matplotlib.rc('axes',unicode_minus = False)

cnt1 = 0
cnt2 = 100

df = pd.read_csv('./movie_cmt_02.csv')


df_title = df['title']


while True:
    
    
    text = df['text'][cnt1:cnt2].tolist()

    text = [x for x in text if pd.isnull(x) == False]
    
    
    text = "".join(str(_)for _ in text)
    
    
    okt = Okt()
    nouns = okt.nouns(text) # 명사만 추출
    nouns = nouns[:50]


    words = [n for n in nouns if len(n) > 1] # 단어의 길이가 1개인 것은 제외

    c = Counter(words) # 위에서 얻은 words를 처리하여 단어별 빈도수 형태의 딕셔너리 데이터를 구함  
    

    wordcloud = WordCloud(font_path = '/Users/dabeen/Desktop/K-DigitalTraining/Project/D.A_numpy/data/malgun.ttf', background_color='white',colormap = "Accent_r", width=1500, height=1000).generate_from_frequencies(c) 
    plt.imshow(wordcloud) 
    plt.axis('off') 
    plt.show()
    
    wordcloud.to_file(f'{df_title[cnt1]}.png')
    
    cnt1 += 100
    cnt2 += 100
    
    if cnt2 == 2000:
        break
    
    
    
    
    

#%%
df = pd.read_csv('./movie_cmt_02.csv')


#%%



df['title'][200]

#%%
text = df['text'][100:200].tolist()

text = [x for x in text if pd.isnull(x) == False]

#%%
text[-1:]
#%%

text = "".join(str(_)for _ in text)

#%%

text

#%%



okt = Okt()
nouns = okt.nouns(text) # 명사만 추출

#%%
nouns = nouns[:30]

#%%
words = [n for n in nouns if len(n) > 1] # 단어의 길이가 1개인 것은 제외

c = Counter(words) # 위에서 얻은 words를 처리하여 단어별 빈도수 형태의 딕셔너리 데이터를 구함



#%%

import matplotlib 
from IPython.display import set_matplotlib_formats 

matplotlib.rc('font',family = 'Malgun Gothic') 
set_matplotlib_formats('retina') 
matplotlib.rc('axes',unicode_minus = False)


wordcloud = WordCloud(font_path = '/Users/dabeen/Desktop/K-DigitalTraining/Project/D.A_numpy/data/malgun.ttf', background_color='white',colormap = "Accent_r", width=1500, height=1000).generate_from_frequencies(c) 
plt.imshow(wordcloud) 
plt.axis('off') 
plt.show()

# %%

wc = WordCloud(font_path='malgun', width=400, height=400, scale=2.0, max_font_size=250)
gen = wc.generate_from_frequencies(c)
plt.figure()
plt.imshow(gen)
# %%
wc.to_file('법전_워드클라우드.png')
# %%
