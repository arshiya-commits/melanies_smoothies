# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col


# Write directly to the app
st.title("\U0001F379 Customize Your Smoothie! \U0001F379")
st.write(
  """Choose the fruits you want in your Smoothie!.
  """
)
from snowflake.snowpark.functions import col
cnx=st.connection("snowflake")
session=cnx.session()
#my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)



name_on_order = st.text_input("Name on Smoothie")
st.write("The name on your Smoothie will be",name_on_order)




ingredients = st.multiselect(
    "Choose up to 5 ingredients:",
    ["Strawberries", "Blueberries", "Mango", "Banana", "Pineapple",
     "Dragon Fruit", "Guava", "Jackfruit", "Elderberries", "Kiwi"],
    max_selections=5
)

# Show the selected ingredients
if ingredients:
    # Create a comma-separated string of ingredients, e.g., "Elderberries, Ximenia, Ziziphus Jujube"
    ingredients_string = ', '.join(ingredients)
    st.write("You selected: " + ingredients_string)
    
    # Prepare SQL statement for inserting the order
    my_insert_stmt = f"""
        insert into smoothies.public.orders(ingredients, name_on_order)
        values ('{ingredients_string}', '{name_on_order}')
    """
    
    # Use a single "Submit Order" button for order submission
    if st.button('Submit Order'):
        session.sql(my_insert_stmt).collect()  # Actually insert order
        st.success(f"Your Smoothie is ordered!  {name_on_order}")
        
