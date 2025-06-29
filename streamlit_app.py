# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
# Write directly to the app
st.title(f":cup_with_straw: Customize your smoothie :cup_with_straw: ")
st.write("choose the fruit's you want in your custom smoothie: ")
name=st.text_input("what is your name: ")
f"The name on Smoothie is {name}"
session = get_active_session()
my_data = session.table("smoothies.public.fruit_options").select(col("Fruit_name"))
ingredient_list=st.multiselect(
    "Choose upto 5 ingredients: ",
    my_data,max_selections=5
)
if ingredient_list:
    ingredients_string=''
    for fruit in ingredient_list:
        ingredients_string+=fruit+' '
        
    #st.write(ingredient_string)
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" +ingredients_string + """','""" +name + """')"""
    st.write(my_insert_stmt)
    submit_=st.button("submit")
    if submit_:
        session.sql(my_insert_stmt).collect()
        st.success(f"Your Smoothie is ordered {name}!", icon="✅")
