import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import io

st.markdown("# **Group Activity 2**")
st.markdown("""
---
**BM7 - Group 1**
* Segador, John Russel C.
* Tejada, Kurt Dhaniel A.
* Agor, John Schlieden A.
---
""")

# ======================================================================== #

st.markdown("## **Describing the dataset**")

if 'dataset' not in st.session_state:
    @st.cache_data
    def load_data(url):
        df = pd.read_csv(url)
        return df

    st.session_state.dataset = load_data('out.csv')
    
df = st.session_state.dataset

# ======================================================================== #

st.markdown("### Dataframe (Sampled)")
sample_df = df.sample(n=100)
st.dataframe(sample_df)

# ====================================== #
st.markdown("---")
st.markdown("### df.info()")

buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

# ====================================== #
st.markdown("---")
st.markdown("### df.isna().sum()")
null_values = df.isna().sum()
st.write(null_values)

# ====================================== #
st.markdown("---")
st.markdown("### df.describe()")
st.dataframe(df.describe())


# ====================================== #
st.markdown("---")
st.markdown("### Count of legitimate and phishing URLs")


# ====================================== #
st.markdown("---")
st.markdown("### Count of URLs based on sources")


# ====================================== #
st.markdown("---")
st.markdown("### Count of URLs based on whether they start with an IP address or not")


# ====================================== #
st.markdown("---")
st.markdown("### Count of URLs based on whether they have punycode characters")
has_punycode = df['has_punycode'].value_counts()
st.write(has_punycode)

# ====================================== #
st.markdown("---")
st.markdown("### Count of URLs based on whether their domain contains digits")
domain_has_digits = df['domain_has_digits'].value_counts()
st.write(domain_has_digits)

# ====================================== #
st.markdown("---")
st.markdown("### Count of URLs based on whether their subdirectory contains links")
has_internal_links = df['has_internal_links'].value_counts()
st.write(has_internal_links)

# ================================================================================================================================== #
st.markdown("---")
st.markdown("## **Graphs**")
# ================================================================================================================================== #
st.markdown("---")
st.markdown("### **Segador**")

starts_with_ip = df['starts_with_ip'].value_counts()
colors = ['cornflowerblue', 'darkgrey']
plt.pie(starts_with_ip,  labels = ['Does not start with IP Address', 'Starts with IP Address'], autopct='%1.1f%%', colors=colors)
plt.title('Proportion of URLs Starting with IP Address')
st.pyplot(plt)
plt.clf()

st.markdown("""The pie chart shows the proportions of URLs that start with an IP address and those 
            that do not. The URLs with an IP as their base account for ***98.9%*** of the dataset.""")



url_length_average = df.groupby('label')['url_length'].mean().reset_index()

plt.figure(figsize=(7, 7))
colors = ['cornflowerblue', 'salmon']
ax = sns.barplot(x='label', y='url_length', hue='label', data=url_length_average, palette=colors)

plt.title('Average URL Length by Label (Phishing vs Legitimate)')
plt.xlabel('Label')
plt.ylabel('Average URL Length')

for p in ax.patches:
    ax.annotate(f'Average: {p.get_height():.1f}',(p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center',  xytext=(0, 10), textcoords='offset points')
st.pyplot(plt)
plt.clf()

st.markdown("""The diagram illustrates the average URL length of the legitimate URLs and phishing 
            URLs. It shows that phishing URLs have higher average lengths with ***71.9*** characters 
            compared to legitimate URLS with ***19.9***.""")

# ================================================================================================================================== #

st.markdown("---")
st.markdown("### **Tejada**")

domain_has_digits = df['domain_has_digits'].value_counts()
colors = ['salmon', 'skyblue']
plt.pie(domain_has_digits,  labels = ['Domains that does not contain digits', 'Domains that contains digits'], autopct='%1.1f%%', colors=colors)
plt.title('Proportion of Domains Containing Digits')
st.pyplot(plt)
plt.clf()

st.markdown("""Pie chart shows the proportions of domains that does and does not contain digits. As you can see from the data that was gathered,
 a majority or ***89.1%*** to be precise of the domains from the data does not contain digits while ***10.9%*** of the domains from the data contains digits.""")

has_punycode = df['has_punycode'].value_counts()
colors = ['orange', 'lightgreen']
plt.pie(has_punycode,  labels = ['URLs that does not have punycode', 'URLs that have punycode'], autopct='%1.1f%%', colors=colors)
plt.title('Proportion of URLs with punycode')
st.pyplot(plt)
plt.clf()

st.markdown("""Pie chart shows the proportions of URLs with and without punycode.
 From the data that was gathered it shows that only ***0.1%*** URLs have punycode while an astounding ***99.9%*** of the URLs does not have punycode.""")

# ================================================================================================================================== #

st.markdown("---")
st.markdown("### **Agor**")

# ================================================================================================================================== #
st.markdown("---")
st.markdown("## **Conclusion**")

st.markdown("""**Insights from our Data Visualization and Data Analysis:**
1. **Balance of the Dataset:**

    - The dataset has balanced distribution of the URLs, with each label (phishing and legitimate) having 1,250,000 samples.
    
     &nbsp;
2. **Structure and Length of URLs:**
    - Majority of the URLs in the dataset have base URLs that starts with an IP address, which is ***98.9%*** of the dataset while those that do not start with and IP address are only ***1.1%***.
    
    - According to the findings, the average length of phishing URLs in the dataset is ***71.9*** characters, while legitimate URLs have an average of ***19.9***.
    
    - Majority of the of the domains in the URLs (***89.1%***) do not contain digits, only ***10.9%*** do.
    
    - Almost all of the URLs in the dataset don't have puny codes (99.9), only ***0.1%*** of the URLs do.
    
    - A significant proportion of ***97.6%*** of the URLs do not contain internal links, only ***2.4%*** do.
    
    - These findings highlight that we can detect whether a URL is malicious based to its structure and length.""", unsafe_allow_html=True)
