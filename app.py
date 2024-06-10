from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import pandas as pd
import google.generativeai as genai 

## configure API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


## load gemini model, provide corresponding sql query
def get_model_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

## hit database with generated query
def query_db(sql, db):
    conn = sqlite3.connect(db)
    # cur=conn.cursor()
    # cur.execute(sql)
    # rows=cur.fetchall()
    result_df = pd.read_sql(sql, conn)
    conn.commit()
    conn.close()

    # for row in rows:
    print(result_df.head())
    
    return result_df

## prompt definition
prompt = [
    """
    You are a SQL expert, who is able to write SQL queries for any task requested in english.
    The SQL databse, named Salaries, has the following columns: EmployeeName, JobTitle, BasePay, OvertimePay, Year and Agency.
    \n\n For example, \nExample 1 - How many records are present in the dataset?, the SQL query 
    will be something like this: SELECT COUNT(*) FROM SALARIES ;
    \nExample 2 - Who are the employees under the Chief of Police?,
    the query will be something like this: SELECT * FROM SALARIES WHERE JobTitle='Chief of Police' OR JobTitle='CHIEF OF POLICE';
    \nExample 3 - What was the average base salary for every job title in 2011?
    the query will be something like this: SELECT AVG(BasePay) FROM SALARIES GROUP BY JobTitle WHERE Year=='2011'; 
    \nalso, the query should not have ``` in the beginning or the end and SQL word in the output. 
    """
]

# streamlit
st.set_page_config(page_title='SQL Query Retrieval')
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input: ", key='input')

submit = st.button("Search")

if submit:
    response = get_model_response(question,prompt)
    print(response) # print query
    result = query_db(response, "data/sqlite/salaries.db")
    st.markdown(f"Query:`{response}`")
    st.markdown("\nResult:")
    st.dataframe(result)
