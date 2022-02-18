#%%
from wordcloud import WordCloud
from collections import Counter
from konlpy.tag import Okt
import pandas as pd
import matplotlib
import operator


df = pd.read_csv('./movie_cmt_02.csv')

start = 0
end = 100


finish_cnt = 1
result_word = []

del_word = ['영화','정말','우리','진짜','지금','대해','보고','놀란']

while True:
    text = df['text'][start:end].tolist()

    text = [x for x in text if pd.isnull(x) == False]

    text = "".join(str(_)for _ in text)

    okt = Okt()
    nouns = okt.nouns(text) # 명사만 추출

    words = [n for n in nouns if len(n) > 1] # 단어의 길이가 1개인 것은 제외

    c = Counter(words) # 위에서 얻은 words를 처리하여 단어별 빈도수 형태의 딕셔너리 데이터를 구함  

    result = sorted(c.items(), key=lambda x: x[1],reverse=True)

    for cnt in result:
        
        if any([cnt[0]== x for x in del_word]):
            pass
            
        elif cnt[1] >= 10:
            result_word.append([df['title'][start],cnt[0],cnt[1]])
    
    
    start +=100
    end +=100
    
    print(f'{finish_cnt}세트 완료')
    if start == 10000:
        break
    
    
    
    

#%%    

test = pd.DataFrame(result_word)
test
#%%

test.to_csv('./test2.csv',encoding='cp949')
# sorted(c.items(),reverse=True)
# wordcloud.to_file(f'{df_title[cnt1]}.png')

#%%
df

#%%
wordcloud = WordCloud(font_path = '/Users/dabeen/Desktop/K-DigitalTraining/Project/D.A_numpy/data/malgun.ttf', background_color='white',colormap = "Accent_r", width=1500, height=1000).generate_from_frequencies(c) 
plt.imshow(wordcloud) 
plt.axis('off')
plt.show()




# %%
c
# %%
