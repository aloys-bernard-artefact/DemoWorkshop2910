import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Hello World!')

if st.button('Say hello'):
    st.balloons()



# Load example dataset
df = sns.load_dataset('penguins')

# Create a seaborn plot
fig, ax = plt.subplots()  
sns.scatterplot(data=df, x='bill_length_mm', y='bill_depth_mm', hue='species', ax=ax)

# Display the plot in Streamlit
fig.set_size_inches(3, 2)
st.pyplot(fig)
