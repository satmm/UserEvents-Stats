import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load data
@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)

# Sidebar - File upload and dataset selection
st.sidebar.title("Upload File")
uploaded_file = st.sidebar.file_uploader(label="Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load CSV file
    df = load_data(uploaded_file)
    
    # Show raw data
    st.subheader("Raw Data")
    st.write(df)
    
    # Show event summary statistics
    st.subheader("Event Summary Statistics")
    st.write("Total number of events:", len(df))
    st.write("Log level distribution:")
    st.write(df['LogLevel'].value_counts())
    st.write("Tag distribution:")
    st.write(df['Tag'].value_counts())
    
    # Plot time series graph
    st.subheader("Time Series Analysis")
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df.set_index('Timestamp', inplace=True)
    st.line_chart(df.resample('D').size(), use_container_width=True)
    
    # Plot event distribution by Subscription ID
    st.subheader("Event Distribution by Subscription ID")
    subscription_counts = df['SubscriptionId'].value_counts()
    st.bar_chart(subscription_counts)
    
    # Plot log level distribution
    st.subheader("Log Level Analysis")
    st.write(df['LogLevel'].value_counts().plot(kind='pie'))
    st.pyplot()
    





    # Plot tag analysis 
    st.subheader("Tag Analysis")
    tags = ' '.join(df['Tag'].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color ='white').generate(tags)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot()

else:
    st.info("Please upload a CSV file.")

