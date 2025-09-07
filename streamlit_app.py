# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col


# Write directly to the app
st.title(" Customize Your Smoothie! ")
st.write(
  "Choose the fruits you want in your Smoothie!."
)
from snowflake.snowpark.functions import col
cnx=st.connection("snowflake")
session=cnx.session()





name_on_order = st.text_input("Name on Smoothie")
st.write("The name on your Smoothie will be",name_on_order)




ingredients = st.multiselect(
    "Choose up to 5 ingredients:",
    ["Strawberries", "Blueberries", "Mango", "Banana", "Pineapple",
     "Dragon Fruit", "Guava", "Jackfruit", "Elderberries", "Kiwi"],
    max_selections=5
)


import requests
smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
#st.text(smoothiefroot_response.json())
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'),col('SEARCH_ON'))
#sf_df=st.dataframe(data=smoothiefroot_response.json(), use_container_width=True)


# Show the selected ingredients
""""if ingredients:
     for fruit_chosen in ingredients:
        st.subheader(fruit_chosen + ' Nutrition Information')
        smoothie_froot_response = requests.get("https://my.smoothiefroot.com/api/fruit/" + fruit_chosen)
        sf_df = st.dataframe(data=smoothie_froot_response.json(), use_container_width=True)
    # Create a comma-separated string of ingredients, e.g., "Elderberries, Ximenia, Ziziphus Jujube"
     ingredients_string = ', '.join(ingredients)
   # st.write("You selected: " + ingredients_string)
    
    # Prepare SQL statement for inserting the order
      my_insert_stmt = f"""
        insert into smoothies.public.orders(ingredients, name_on_order)
        values ('{ingredients_string}', '{name_on_order}')
    """
    
    # Use a single "Submit Order" button for order submission
    if st.button('Submit Order'):
        session.sql(my_insert_stmt).collect()  # Actually insert order
        st.success(f"Your Smoothie is ordered!  {name_on_order}")
 """       
pd_df=my_dataframe.to_pandas()
# st.dataframe(pd_df)
# st.stop()

ingredients_list = st.multiselect(
    'Choose up to 5 ingredients:',
    my_dataframe,
    max_selections=5
)
if ingredients_list:
    ingredients_string = ''

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

    search_on = pd_df.loc[pd_df['FRUIT_NAME'] == fruit_chosen, 'SEARCH_ON'].iloc[0]
    # st.write('The search value for', fruit_chosen, 'is', search_on, '.')
    st.subheader(fruit_chosen + ' Nutrition Information')
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + search_on)
    fv_df = st.dataframe(data=fruityvice_response.json(), use_container_width=True)
# st.write(ingredients_string)

    # Create a comma-separated string of ingredients, e.g., "Elderberries, X, Y"
    ingredients_string = ', '.join(ingredients)
    
    # Prepare SQL insert statement
    my_insert_stmt = f"""
           insert into smoothies.public.orders(ingredients, name_on_order)
            values ('{ingredients_string}', '{name_on_order}')
    """
    
    # Submit button
    if st.button('Submit Order'):
        session.sql(my_insert_stmt).collect()
        st.success(f"Your Smoothie is ordered!  {name_on_order}")
