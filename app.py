import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image 

st.set_page_config(page_title="Data analysis using pandas, matplotlib and streamlit")
st.header("Top 100 popular movies from 2003 to 2022 (iMDB)")
st.subheader("Loading DataFrame")

# Load dataframe
excel_file = "movies.xlsx"
sheet_name = "Worksheet"

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols="A:D",
                   header=0)

df_Directors = pd.read_excel(excel_file,
                             sheet_name=sheet_name,
                             usecols="A,G",
                             header=0)

df_Informations = pd.read_excel(excel_file,
                             sheet_name=sheet_name,
                             usecols="A,B,C,D,I,M",
                             header=0)

st.dataframe(df)
st.dataframe(df_Directors)
st.dataframe(df_Informations)


# Streamlit slider selection and multiselection
year = df["Year"].unique().tolist()
rating = df["Rating"].unique().tolist()

rating_selection = st.slider("Rating:",
                            min_value= min(rating),
                            max_value= max(rating),
                            value=(min(rating),max(rating)))

year_selection = st.multiselect("Year:",
                                year,
                                default=year)


mask =(df["Rating"].between(*rating_selection)) & (df["Year"].isin(year_selection))
number_of_result = df[mask].shape[0]
st.markdown(f"*Available Results: {number_of_result}*")


# Matplotlib graph visualization
st.subheader("Top rating according to year")
data = pd.read_excel("movies.xlsx")
rating = data['Rating']
year = data['Year']

plt.scatter(year, rating)

plt.xlabel('Year')
plt.ylabel('Rating')
plt.title("Top rating according to year")

st.set_option('deprecation.showPyplotGlobalUse', False)

st.pyplot()


# Ploty pie chart visualization
pie_chart = px.pie(df_Informations,
                title='Average rating according to year',
                values='Rating',
                names='Year')

st.plotly_chart(pie_chart)



# IMAGES
st.title("And since we love cinema so much. Here are some iconic cinema shots!")

image1 = Image.open('images/Amelie-Poulain-at-Studio-28-Paris-cinema.jpeg')
st.image(image1)
st.caption("Amélie(2001)")

image2 = Image.open('images/Cinema-Paradiso.png')
image3 = Image.open('images/Cinema-Paradiso.jpeg')
st.image(image2)
st.image(image3)
st.caption("Cinema Paradiso(1988)")

image4 = Image.open('images/everythingeverywhereallatonce.jpeg')
st.image(image4)
st.caption("Everything Everywhere All at Once(2022)")

image5 = Image.open('images/leon.jpeg')
st.image(image5)
st.caption("Léon: The Professional(1994)")

image6 = Image.open('images/The-Shawshank-Redemption-movie-scene-2-1100x625.jpeg')
st.image(image6)
st.caption("The Shawshank Redemption(1994)")