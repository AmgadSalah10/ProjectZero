import streamlit as st
import requests as rq
import datetime as datetime
from datetime import date

st.set_page_config(page_title="THE FINDER", page_icon=":mag_right:", layout="wide")

st.write("""
         # This is 'THE FINDER :mag_right:'""")
st.caption("            Created by 'Amgad Salah'")           
st.write("""
         ## 'THE FINDER :mag_right:' is a tool to help you access thousands
         ## of articles customized for your needs.
         """)

col1, col2 = st.columns(2)

with col1:
    st.write("""
             ## Here you can get top headlines for a certain country.
             """)
    
    country = st.selectbox(
        'Choose the country you want to get top headlines for',
        ('us', 'gb', 'eg'))
    
    category =  st.selectbox(
        'Choose the category you want to get articles for',
        ('general', 'entertainment', 'business', 'health', 'science', 'sports', 'technology'))
    
    resultsNum1 = st.number_input('Insert the number of results to return', value=5, min_value=1)

    if st.button("FIND top headlines🔎"):
        url1 = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&pageSize={resultsNum1}&apiKey=52f086fb1f134027beee9dce6d85c312"
        news1 = rq.get(url1)
        x1 = 0
        if len(news1.json()["articles"])>resultsNum1:
           for i in range(resultsNum1):
              st.write(news1.json()["articles"][x1]["title"])
              if news1.json()["articles"][x1]["urlToImage"]:
                 st.image(news1.json()["articles"][x1]["urlToImage"])
              st.write("Author: ", news1.json()["articles"][x1]["author"])
              st.write(news1.json()["articles"][x1]["description"])
              st.write("URL: ",news1.json()["articles"][x1]["url"])
              st.write("----------------------------------------------------------------")
              x1 += 1
        else:
           for i in news1.json()["articles"]:
              st.write(news1.json()["articles"][x1]["title"])
              if news1.json()["articles"][x1]["urlToImage"]:
                 st.image(news1.json()["articles"][x1]["urlToImage"])
              st.write("Author: ", news1.json()["articles"][x1]["author"])
              st.write(news1.json()["articles"][x1]["description"])
              st.write("URL: ",news1.json()["articles"][x1]["url"])
              st.write("----------------------------------------------------------------")
              x1 += 1
    else:
        url1 = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&pageSize={resultsNum1}&apiKey=52f086fb1f134027beee9dce6d85c312"
        news1 = rq.get(url1)
        x1 = 0
        if len(news1.json()["articles"])>resultsNum1:
            for i in range(resultsNum1):
                st.write(news1.json()["articles"][x1]["title"])
                if news1.json()["articles"][x1]["urlToImage"]:
                    st.image(news1.json()["articles"][x1]["urlToImage"])
                st.write("Author: ", news1.json()["articles"][x1]["author"])
                st.write(news1.json()["articles"][x1]["description"])
                st.write("URL: ",news1.json()["articles"][x1]["url"])
                st.write("----------------------------------------------------------------")
                x1 += 1
        else:
            for i in news1.json()["articles"]:
                st.write(news1.json()["articles"][x1]["title"])
                if news1.json()["articles"][x1]["urlToImage"]:
                    st.image(news1.json()["articles"][x1]["urlToImage"])
                st.write("Author: ", news1.json()["articles"][x1]["author"])
                st.write(news1.json()["articles"][x1]["description"])
                st.write("URL: ",news1.json()["articles"][x1]["url"])
                st.write("----------------------------------------------------------------")
                x1 += 1


with col2:
    st.write("""
             ## Here you can get customized articles as you wish.
             """)
    
    keyWord = str(st.text_input("Enter key word"))
    if not keyWord.isalpha():
       st.write("Oops! only strings are allowed")
    
    st.write("""
             ### Now you have to set the time range of the articles
             """)
    today = date.today()
    fromDate = st.date_input(
        "Enter the oldest date for the articles",
        today)
    toDate = st.date_input(
        "Enter the newest date for the articles",
        today)
    
    if fromDate and toDate <= today:
       
       if fromDate > toDate:
          
          st.write("Oops! it seems that you've made a logical mistake")
          st.caption("The newest date must be more recent than the oldest date")
    
       else:    

           restSearch = st.selectbox(
               'Choose a field to restrict the search to',
               ('title', 'description', 'content'))

           domain = st.text_input("Enter a domain/domains to restrict the search to ")
           st.caption("*In case of entering more than one domain, you must separate them with a coma','")

           exclDomain = st.text_input("Enter a domain/domains to exclude from the results")
           st.caption("*In case of entering more than one domain, you must separate them with a coma','")

           language = st.radio(
               "Choose the articles language",
               ('ar', 'en', 'fr'))

           sort = st.selectbox(
               'Choose the order to sort the articles in',
               ('relevancy', 'popularity', 'publishedAt'))

           resultsNum2 = st.number_input('Insert the number of results to return', value=10, min_value=1)

           if st.button("FIND 🔎"):
               url2 = f"https://newsapi.org/v2/everything?q={keyWord}&searchIn={restSearch}&domains={domain}&excludeDomains={exclDomain}&from={fromDate}&to={toDate}&language={language}&sortBy={sort}&pageSize={resultsNum2}&apiKey=52f086fb1f134027beee9dce6d85c312"
               news2 = rq.get(url2)
               x = 0
               if len(news2.json()["articles"])>resultsNum2:
                  for i in range(resultsNum2):
                      st.write(news2.json()["articles"][x]["title"])
                      if news2.json()["articles"][x]["urlToImage"]:
                         st.image(news2.json()["articles"][x]["urlToImage"])
                      st.write("Author: ", news2.json()["articles"][x]["author"])
                      st.write(news2.json()["articles"][x]["description"])
                      st.write("URL: ",news2.json()["articles"][x]["url"])
                      st.write("----------------------------------------------------------------")
                      x += 1
               else:
                   for i in news2.json()["articles"]:
                      st.write(news2.json()["articles"][x]["title"])
                      if news2.json()["articles"][x]["urlToImage"]:
                         st.image(news2.json()["articles"][x]["urlToImage"])
                      st.write("Author: ", news2.json()["articles"][x]["author"])
                      st.write(news2.json()["articles"][x]["description"])
                      st.write("URL: ",news2.json()["articles"][x]["url"])
                      st.write("----------------------------------------------------------------")
                      x += 1
    else:
        st.write("Oops! you have to select a valid time frame")