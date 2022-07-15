import streamlit as st
import pandas as pd
import altair as alt

st.title('Yearly Alcohol Consumption 2010')
st.markdown("""
Here you will be able to view the average yearly alcohol consumption per person in a given country.
* **Libraries Used:** Pandas, Altair, and Streamlit
* **Data Source:** [Github.com](https://github.com/fivethirtyeight/data/tree/master/alcohol-consumption)
""")

# top level dataframe of all countries
alcohol_data = pd.read_csv('alcohol_data.csv')
st.title('Per person glasses per year')
st.dataframe(alcohol_data)

# Barchart for top beer drinking countries
st.title('Top 10 beer drinking countries')
beer_data = alcohol_data.sort_values('beer_servings')
beer_data = beer_data.tail(10)
beer_chart = alt.Chart(beer_data).mark_bar().encode(
    x='country',
    y='beer_servings'
)

beer_chart = beer_chart.properties(
    width=alt.Step(50)
)
st.write(beer_chart)

# Barchart for wine consumption
st.title('Top 10 wine drinking countries')
wine_data = alcohol_data.sort_values('wine_servings')
wine_data = wine_data.tail(10)
wine_chart = alt.Chart(wine_data).mark_bar().encode(
    x='country',
    y='wine_servings'
)

wine_chart = wine_chart.properties(
    width=alt.Step(50)
)
st.write(wine_chart)

# Barchart for wine consumption
st.title('Top 10 spirit drinking countries')
spirit_data = alcohol_data.sort_values('spirit_servings')
spirit_data = spirit_data.tail(10)
spirit_chart = alt.Chart(spirit_data).mark_bar().encode(
    x='country',
    y='spirit_servings'
)

spirit_chart = spirit_chart.properties(
    width=alt.Step(50)
)
st.write(spirit_chart)

# Barchart for wine consumption
st.title('Top 10 total total litres consumed')
total_data = alcohol_data.sort_values('total_litres_of_pure_alcohol')
total_data = total_data.tail(10)
total_chart = alt.Chart(spirit_data).mark_bar().encode(
    x='country',
    y='total_litres_of_pure_alcohol'
)

total_chart = total_chart.properties(
    width=alt.Step(50)
)
st.write(total_chart)

# sidebar to select countries
st.sidebar.header('User Input Features')
country_names = alcohol_data['country']
country_selected = st.sidebar.multiselect("Select Countries to Compare", country_names)

selected_country = alcohol_data[(alcohol_data.country.isin(country_selected))]

st.title('User Selected Countries')
st.write('Select Countries on side bar to view')
st.dataframe(selected_country)

# Bar chart of selected countries
st.title('Beer Comparison of user selections')
p = alt.Chart(selected_country).mark_bar().encode(
    x='country',
    y='beer_servings'
)

p = p.properties(
    width=alt.Step(50)
)
st.write(p)
