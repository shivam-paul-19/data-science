import streamlit as st
import pandas as pd

# title of the app
st.title("Hello world")

# inserting text 
st.write("Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusantium incidunt ipsa asperiores molestiae voluptatem ad, atque quos sit iste iure fugiat corrupti magni at eveniet iusto illo facere natus rerum!")

# inserting a data frame
car_sales = pd.read_csv(r"C:\Users\91977\Desktop\coding\aiml\streamlit\carsales.csv")
df = pd.DataFrame(car_sales)
st.write(df.head(10))

# inserting charts
chart_data = df[['Doors', 'Price']]
st.line_chart(chart_data)

bar_data = df.groupby('Make')['Price'].sum()
st.bar_chart(bar_data)

# inserting input field
name = st.text_input("Enter your name: ")
if name:
    st.write(f"Hi there! {name}")

age = st.slider("What's your age? ", 0, 100, 20)
st.write(f"Your age is {age}")

langs = ['Python', 'Java', 'C++', 'JavaScript']
choice = st.selectbox("Your favourite language?: ", langs)
st.write(f"You selected {choice}")

# taking a file
file = st.file_uploader("Upload a csv file", type='csv')
if file is not None:
    uploaded_file = pd.read_csv(file)
    st.write(pd.DataFrame(uploaded_file))
