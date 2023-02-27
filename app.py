import streamlit as st
import pandas as pd
import numpy as np

# pip3 install openpyxl
import openpyxl

st.title('Targeting Taxonomies')

# App setup 
with st.container():
    # st.set_page_config(layout="wide")
    col1, col2, col3 = st.columns((2,2,2))

    col1.header('Main Field')
    col2.header('Sub Field')
    col3.header('Categories')

# Loading in data 
main_category = ('','Household Demographic', 'Insurance Behavior', 'Alcohol Behavior', 'Apparel and Jewelry Behavior', 'Automotive Behavior', 
                'Commuting Behavior', 'Video Consumption Behavior', 'Environment-related Behavior', 'Financial Behavior', 'Food and Beverages Behavior')
household_demo = pd.read_excel('data.xlsx', sheet_name = 'household_demo')
insurance_behavior = pd.read_excel('data.xlsx', sheet_name = 'insurance_behavior')
alcohol_behavior = pd.read_csv('data.csv', sheet_name = 'alcohol_behavior')
apparel_and_jewelry = pd.read_csv('data.csv', sheet_name = 'apparel_and_jewelry')
automative_behavior = pd.read_csv('data.csv', sheet_name = 'automative_behavior')
commuting = pd.read_csv('data.csv', sheet_name = 'commuting')
videos = pd.read_csv('data.csv', sheet_name = 'videos')
environment = pd.read_csv('data.csv', sheet_name = 'environment')
financial = pd.read_csv('data.csv', sheet_name = 'financial')
food_and_beverages = pd.read_csv('data.csv', sheet_name = 'food_and_beverages')

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
        
            option2 = st.selectbox(
                'And a subfield within the field:',
                sub_category,
                key = count)
            # st.write('You selected:', option2)
            count += 1 

        with col3: 
            if option2:
                if option1 == "Household Demographic":
                    st.dataframe(household_demo[option2].dropna())
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

        add_field = st.checkbox('Add another field?', key = count)
        count += 1
    
    return add_field, count

# add_field, count = each_container(count=0)

add_field = True
count = 0
max_containers = 100
for i in range(max_containers):
    if add_field: 
        add_field, count = each_container(count)

########## first code
# with st.container():
#     col1, col2, col3 = st.columns((2,2,2))
#     # st.write(household_demo[0])
#     # st.table(household_demo)

#     with col1: 
#         option1 = st.selectbox(
#             'Please select a field:',
#             main_category,
#             key = count)
#         count += 1

#     with col2: 

#         if option1 == "":
#             sub_category = ('')
#         elif option1 == "Household demographic":
#             sub_category = (household_demo['Main'].dropna())
#         elif option1 == "Insurance Behavior":
#             sub_category = (insurance_behavior['Main'].dropna())
     
#         option2 = st.selectbox(
#             'And a subfield within the field:',
#             sub_category,
#             key = count)
#         # st.write('You selected:', option2)
#         count += 1 

#     with col3: 
#         if option2:
#             if option1 == "Household demographic":
#                 st.table(household_demo[option2].dropna())
#             elif option1 == "Insurance Behavior":
#                 st.table(insurance_behavior[option2].dropna())

#     add_field = st.checkbox('Add another field?', key = count)
#     count += 1

########## second code
# if add_field: 
#     add_field, count = each_container(count)

########## first code
# if add_field:
#     with st.container():
#         col1, col2, col3 = st.columns((2,2,2))
#         # st.write(household_demo[0])
#         # st.table(household_demo)

#         with col1: 
#             option1 = st.selectbox(
#                 'Please select a field:',
#                 main_category,
#                 key = count)
#             count += 1

#         with col2: 

#             if option1 == "":
#                 sub_category = ('')
#             elif option1 == "Household demographic":
#                 sub_category = (household_demo['Main'].dropna())
#             elif option1 == "Insurance Behavior":
#                 sub_category = (insurance_behavior['Main'].dropna())
        
#             option2 = st.selectbox(
#                 'And a subfield within the field:',
#                 sub_category,
#                 key = count)
#             # st.write('You selected:', option2)
#             count += 1 

#         with col3: 
#             if option2:
#                 if option1 == "Household demographic":
#                     st.table(household_demo[option2].dropna())
#                 elif option1 == "Insurance Behavior":
#                     st.table(insurance_behavior[option2].dropna())

#         add_field = st.checkbox('Add another field?', key = count)
#         count += 1

###############################################################################################################################
    # option3 = st.radio(
    # 'What are your favorite colors',
    # ['Green', 'Yellow', 'Red', 'Blue'])
    # st.write('You selected:', option3)
