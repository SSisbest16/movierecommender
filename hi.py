
import streamlit as st
import pickle
import pandas as pd
def rec(movie):

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    rm=[]
    for i in movies_list:
        rm.append(movies.iloc[i[0]].title)
    return rm




movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title(" movie recommeneder system")
smn=st.selectbox("please choose your movie",
movies['title'])
if st.button('recommendations'):
    rec=rec(smn)
    for i in rec:
        st.write(i)
