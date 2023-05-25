import streamlit as st
import pandas as pd
import numpy as np

# pip install openpyxl
# import openpyxl 

st.title('Targeting Taxonomies')

# App setup 
with st.container():
    # st.set_page_config(layout="wide")
    col1, col2, col3 = st.columns((2,2,2))

    col1.header('Main Field')
    col2.header('Sub Field')
    col3.header('Sub Sub Fields')

# Loading in data 
main_category = ('','Household Demographic', 'Insurance Behavior', 'Alcohol Behavior', 'Apparel and Jewelry Behavior', 'Automotive Behavior', 
                'Commuting Behavior', 'Video Consumption Behavior', 'Environment-related Behavior', 'Financial Behavior', 'Food and Beverages Behavior',
                'Health Behavior', 'Home Improvement Behavior', 'Items in Home', 
                'Magazines and Newspaper Behavior', 'Voting Behavior', 'Travel Behavior', 'Print Media Usage & Alternative Advertising',
                'Neighborhood Demographics', 'Psychographics', 'Radio Behavior', 'Restaurants Behavior', 'Retail Shopping Behavior',
                'Sports and Leisure Behavior', 'Telecommunications Behavior')

# df = pd.read_excel('household_demo.xlsx')
household_demo = pd.read_excel('data.xlsx', sheet_name = 'household_demo')
insurance_behavior = pd.read_excel('data.xlsx', sheet_name = 'insurance_behavior')
alcohol_behavior = pd.read_excel('data.xlsx', sheet_name = 'alcohol_behavior')
apparel_and_jewelry = pd.read_excel('data.xlsx', sheet_name = 'apparel_and_jewelry')
automative_behavior = pd.read_excel('data.xlsx', sheet_name = 'automative_behavior')
commuting = pd.read_excel('data.xlsx', sheet_name = 'commuting')
videos = pd.read_excel('data.xlsx', sheet_name = 'videos')
environment = pd.read_excel('data.xlsx', sheet_name = 'environment')
financial = pd.read_excel('data.xlsx', sheet_name = 'financial')
food_and_beverages = pd.read_excel('data.xlsx', sheet_name = 'food_and_beverages')
health = pd.read_excel('data.xlsx', sheet_name = 'health')
home_improvement = pd.read_excel('data.xlsx', sheet_name = 'home_improvement')
home_items = pd.read_excel('data.xlsx', sheet_name = 'home_items')
magazine_newspaper = pd.read_excel('data.xlsx', sheet_name = 'magazine_newspaper')
voting = pd.read_excel('data.xlsx', sheet_name = 'voting')
travel = pd.read_excel('data.xlsx', sheet_name = 'travel')
advertising = pd.read_excel('data.xlsx', sheet_name = 'advertising')
neighborhood = pd.read_excel('data.xlsx', sheet_name = 'neighborhood')
psychographics = pd.read_excel('data.xlsx', sheet_name = 'psychographics')
radio = pd.read_excel('data.xlsx', sheet_name = 'radio')
restaurants = pd.read_excel('data.xlsx', sheet_name = 'restaurants')
shopping = pd.read_excel('data.xlsx', sheet_name = 'shopping')
sports = pd.read_excel('data.xlsx', sheet_name = 'sports')
telecom = pd.read_excel('data.xlsx', sheet_name = 'telecom')

# alcohol_behavior = pd.read_csv('data.csv', sheet_name = 'alcohol_behavior')
# apparel_and_jewelry = pd.read_csv('data.csv', sheet_name = 'apparel_and_jewelry')
# automative_behavior = pd.read_csv('data.csv', sheet_name = 'automative_behavior')
# commuting = pd.read_csv('data.csv', sheet_name = 'commuting')
# videos = pd.read_csv('data.csv', sheet_name = 'videos')
# environment = pd.read_csv('data.csv', sheet_name = 'environment')
# financial = pd.read_csv('data.csv', sheet_name = 'financial')
# food_and_beverages = pd.read_csv('data.csv', sheet_name = 'food_and_beverages')

# Code for each container and its three columns
def each_container(count):
    with st.container():
        col1, col2, col3 = st.columns((2,2,2))

        with col1: 
            option1 = st.selectbox(
                'Please select a field:',
                main_category,
                key = count)
            count += 1

        with col2: 

            if option1 == "":
                sub_category = ('')
            elif option1 == "Household Demographic":
                sub_category = (household_demo['Main'].dropna())
            elif option1 == "Insurance Behavior":
                sub_category = (insurance_behavior['Main'].dropna())
            elif option1 == "Alcohol Behavior":
                sub_category = (alcohol_behavior['Main'].dropna())
            elif option1 == "Apparel and Jewelry Behavior":
                sub_category = (apparel_and_jewelry['Main'].dropna())
            elif option1 == "Automotive Behavior":
                sub_category = (automative_behavior['Main'].dropna())
            elif option1 == "Commuting Behavior":
                sub_category = (commuting['Main'].dropna())
            elif option1 == "Video Consumption Behavior":
                sub_category = (videos['Main'].dropna())
            elif option1 == "Environment-related Behavior":
                sub_category = (environment['Main'].dropna())
            elif option1 == "Financial Behavior":
                sub_category = (financial['Main'].dropna())
            elif option1 == "Food and Beverages Behavior":
                sub_category = (food_and_beverages['Main'].dropna())
            elif option1 == "Health Behavior":
                sub_category = (health['Main'].dropna())
            elif option1 == "Home Improvement Behavior":
                sub_category = (home_improvement['Main'].dropna())
            elif option1 == "Items in Home":
                sub_category = (home_items['Main'].dropna())
            elif option1 == "Magazines and Newspaper Behavior": 
                sub_category = (magazine_newspaper['Main'].dropna())
            elif option1 == "Voting Behavior":
                sub_category = (voting['Main'].dropna())
            elif option1 == "Travel Behavior":
                sub_category = (travel['Main'].dropna())
            elif option1 == "Print Media Usage & Alternative Advertising":
                sub_category = (advertising['Main'].dropna())
            elif option1 == "Neighborhood Demographics":
                sub_category = (neighborhood['Main'].dropna())
            elif option1 == "Psychographics":
                sub_category = (psychographics['Main'].dropna())
            elif option1 == "Radio Behavior":
                sub_category = (radio['Main'].dropna())
            elif option1 == "Restaurants Behavior":
                sub_category = (restaurants['Main'].dropna())
            elif option1 == "Retail Shopping Behavior":
                sub_category = (shopping['Main'].dropna())
            elif option1 == "Sports and Leisure Behavior":
                sub_category = (sports['Main'].dropna())
            elif option1 == "Telecommunications Behavior":
                sub_category = (telecom['Main'].dropna())
        
            option2 = st.selectbox(
                'And a subfield within the field:',
                sub_category,
                key = count)
            # st.write('You selected:', option2)
            count += 1 

        with col3: 
            if option2:
                if option1 == "Household Demographic":
                    option3 = st.selectbox(option2, household_demo[option2].dropna())
                    # st.dataframe(household_demo[option2].dropna())
                elif option1 == "Insurance Behavior":
                    st.dataframe(insurance_behavior[option2].dropna())
                elif option1 == "Alcohol Behavior":
                    st.table(alcohol_behavior[option2].dropna())
                elif option1 == "Apparel and Jewelry Behavior":
                    st.table(apparel_and_jewelry[option2].dropna())
                elif option1 == "Automotive Behavior":
                    st.table(automative_behavior[option2].dropna())
                elif option1 == "Commuting Behavior":
                    st.table(commuting[option2].dropna())
                elif option1 == "Video Consumption Behavior":
                    st.table(videos[option2].dropna())
                elif option1 == "Environment-related Behavior":
                    st.table(environment[option2].dropna())
                elif option1 == "Financial Behavior":
                    st.table(financial[option2].dropna())
                elif option1 == "Food and Beverages Behavior":
                    st.table(food_and_beverages[option2].dropna())
                elif option1 == "Health Behavior":
                    st.table(health[option2].dropna())
                elif option1 == "Home Improvement Behavior":
                    st.table(home_improvement[option2].dropna())
                elif option1 == "Items in Home":
                    st.table(home_items[option2].dropna())
                elif option1 == "Magazines and Newspaper Behavior":
                    st.table(magazine_newspaper[option2].dropna())
                elif option1 == "Voting Behavior":
                    st.table(voting[option2].dropna())
                elif option1 == "Travel Behavior":
                    st.table(travel[option2].dropna())
                elif option1 == "Print Media Usage & Alternative Advertising":
                    st.table(advertising[option2].dropna())
                elif option1 == "Neighborhood Demographics":
                    st.table(neighborhood[option2].dropna())
                elif option1 == "Psychographics":
                    st.table(psychographics[option2].dropna())
                elif option1 == "Radio Behavior":
                    st.table(radio[option2].dropna())
                elif option1 == "Restaurants Behavior":
                    st.table(restaurants[option2].dropna())
                elif option1 == "Retail Shopping Behavior":
                    st.table(shopping[option2].dropna())
                elif option1 == "Sports and Leisure Behavior":
                    st.table(sports[option2].dropna())
                elif option1 == "Telecommunications Behavior":
                    st.table(telecom[option2].dropna())

        st.write("You selected Main Field:", option1, ", Sub Field:", option2, ", Sub Sub Field:", option3)
        add_field = st.checkbox('Add another field?', key = count)
        count += 1
    
    return add_field, count

# add_field, count = each_container(count=0)

add_field = True
count = 0
max_containers = 300 # variable - can change
for i in range(max_containers):
    if add_field: 
        add_field, count = each_container(count)
