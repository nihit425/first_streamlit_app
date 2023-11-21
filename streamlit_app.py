import streamlit
import pandas

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and Blue Berry Oatmeal')
streamlit.text('🥗 Spinach Sandwith with Soup')
streamlit.text('🐔 Halfried with Boiled Eggs')
streamlit.text('🥑 Avocado Toast')
streamlit.text('🍞 Bombay Cheese Sandwich')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
