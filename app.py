

# # # # import streamlit as st
# # # # import pandas as pd
# # # # import matplotlib.pyplot as plt
# # # # from wordcloud import WordCloud
# # # # import os

# # # # # Load data
# # # # @st.cache_data()
# # # # def load_data(file_path):
# # # #     df = pd.read_csv(file_path)
# # # #     # Convert 'Timestamp' column to datetime format
# # # #     if 'Timestamp' in df.columns:
# # # #         df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce', unit='s')
# # # #     return df

# # # # # Get file path of CSV file in project folder
# # # # file_path = os.path.join(os.getcwd(), "output.csv")

# # # # if os.path.exists(file_path):
# # # #     # Load CSV file
# # # #     df = load_data(file_path)

# # # #     # Show raw data
# # # #     st.subheader("Raw Data")
# # # #     st.write(df)
    
# # # #     # Print DataFrame columns for debugging
# # # #     st.write("Columns:", df.columns)
    
# # # #     # Check if 'Timestamp' column exists after conversion
# # # #     if 'Timestamp' in df.columns:
# # # #         # Show event summary statistics
# # # #         st.subheader("Event Summary Statistics")
# # # #         st.write("Total number of events:", len(df))
# # # #         st.write("Log level distribution:")
# # # #         st.write(df['LogLevel'].value_counts())
# # # #         st.write("Tag distribution:")
# # # #         st.write(df['Tag'].value_counts())
        
# # # #         # Plot time series graph
# # # #         st.subheader("Time Series Analysis")
# # # #         df.set_index('Timestamp', inplace=True)
# # # #         try:
# # # #             resampled_data = df.resample('D').size()
# # # #             st.line_chart(resampled_data, use_container_width=True)
# # # #         except Exception as e:
# # # #             st.error(f"Error during resampling: {str(e)}")

# # # #         # Plot event distribution by Subscription ID
# # # #         st.subheader("Event Distribution by Subscription ID")
# # # #         subscription_counts = df['SubscriptionId'].value_counts()
# # # #         st.bar_chart(subscription_counts)

# # # #         # Plot log level distribution
# # # #         st.subheader("Log Level Analysis")
# # # #         fig1, ax1 = plt.subplots()
# # # #         df['LogLevel'].value_counts().plot(kind='pie', ax=ax1)
# # # #         st.pyplot(fig1)

# # # #         # Plot tag analysis 
# # # #         st.subheader("Tag Analysis")
# # # #         fig2, ax2 = plt.subplots(figsize=(10, 5))
# # # #         tags = ' '.join(df['Tag'].dropna())
# # # #         wordcloud = WordCloud(width=800, height=400, background_color ='white').generate(tags)
# # # #         ax2.imshow(wordcloud, interpolation='bilinear')
# # # #         ax2.axis('off')
# # # #         st.pyplot(fig2)
# # # #     else:
# # # #         st.error("Timestamp column not found in the DataFrame.")
# # # # else:
# # # #     st.error("CSV file not found in the project folder.")












# # # import streamlit as st
# # # import pandas as pd
# # # import matplotlib.pyplot as plt
# # # from wordcloud import WordCloud
# # # import os

# # # # Function to load data from CSV file
# # # @st.cache
# # # def load_data(file_path):
# # #     df = pd.read_csv(file_path)
# # #     # Convert 'Timestamp' column to datetime format
# # #     if 'Timestamp' in df.columns:
# # #         df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce', unit='s')
# # #     return df

# # # # Get file path of CSV file in project folder
# # # file_path = os.path.join(os.getcwd(), "output.csv")

# # # if os.path.exists(file_path):
# # #     # Load CSV file
# # #     df = load_data(file_path)
    
# # #     # Extract Timestamp data from the DataFrame
# # #     timestamp_data = df["Timestamp"].tolist()

# # #     # Show raw data
# # #     st.subheader("Raw Data")
# # #     st.write(df)
    
# # #     # Print DataFrame columns for debugging
# # #     st.write("Columns:", df.columns)
    
# # #     # Check if 'Timestamp' column exists after conversion
# # #     if 'Timestamp' in df.columns:
# # #         # Show event summary statistics
# # #         st.subheader("Event Summary Statistics")
# # #         st.write("Total number of events:", len(df))
# # #         st.write("Log level distribution:")
# # #         st.write(df['LogLevel'].value_counts())
# # #         st.write("Tag distribution:")
# # #         st.write(df['Tag'].value_counts())
        
# # #         # Plot time series graph
# # #         st.subheader("Time Series Analysis")
# # #         df.set_index('Timestamp', inplace=True)
# # #         try:
# # #             resampled_data = df.resample('D').size()
# # #             st.line_chart(resampled_data, use_container_width=True)
# # #         except Exception as e:
# # #             st.error(f"Error during resampling: {str(e)}")

# # #         # Plot event distribution by Subscription ID
# # #         st.subheader("Event Distribution by Subscription ID")
# # #         subscription_counts = df['SubscriptionId'].value_counts()
# # #         st.bar_chart(subscription_counts)

# # #         # Plot log level distribution
# # #         st.subheader("Log Level Analysis")
# # #         fig, ax = plt.subplots()
# # #         df['LogLevel'].value_counts().plot(kind='pie', ax=ax)
# # #         st.pyplot(fig)

# # #         # Plot tag analysis 
# # #         st.subheader("Tag Analysis")
# # #         tags = ' '.join(df['Tag'].dropna())
# # #         wordcloud = WordCloud(width=800, height=400, background_color ='white').generate(tags)
# # #         plt.figure(figsize=(10, 5))
# # #         plt.imshow(wordcloud, interpolation='bilinear')
# # #         plt.axis('off')
# # #         st.pyplot(plt)
# # #     else:
# # #         st.error("Timestamp column not found in the DataFrame.")
# # # else:
# # #     st.error("CSV file not found in the project folder.")








import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os

st.set_option('deprecation.showPyplotGlobalUse', False)

@st.cache_resource(show_spinner=False)
def load_data(file_path):
    df = pd.read_csv(file_path)
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'].astype(int), errors='coerce', unit='s')
    return df

file_path = os.path.join(os.getcwd(), "output.csv")
df = load_data(file_path)

if df is not None:
    # Show raw data
    st.subheader("Raw Data")
    st.write(df)
    
    # Print DataFrame columns for debugging
    st.write("Columns:", df.columns)
    
    # Check if 'Timestamp' column exists after conversion
    if 'Timestamp' in df.columns:
        # Show event summary statistics
        st.subheader("Event Summary Statistics")
        st.write("Total number of events:", len(df))
        st.write("Log level distribution:")
        st.write(df['LogLevel'].value_counts())
        st.write("Tag distribution:")
        st.write(df['Tag'].value_counts())
        
        # Plot time series graph
        st.subheader("Time Series Analysis")
        df.set_index('Timestamp', inplace=True)
        try:
            resampled_data = df.resample('D').size()
            st.line_chart(resampled_data, use_container_width=True)
        except Exception as e:
            st.error(f"Error during resampling: {str(e)}")
        
        # Plot event distribution by Subscription ID
        st.subheader("Event Distribution by Subscription ID")
        subscription_counts = df['SubscriptionId'].value_counts()
        st.bar_chart(subscription_counts)
        
        # Plot log level distribution
        st.subheader("Log Level Analysis")
        fig, ax = plt.subplots()
        df['LogLevel'].value_counts().plot(kind='pie', ax=ax)
        st.pyplot(fig)
        
        # Plot tag analysis 
        st.subheader("Tag Analysis")
        fig, ax = plt.subplots()
        wordcloud = WordCloud(width=800, height=400, background_color ='white').generate_from_text(' '.join(df['Tag'].dropna()))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)
    else:
        st.error("Timestamp column not found in the DataFrame.")
else:
    st.error("CSV file not found in the project folder.")




# import streamlit as st
# import pandas as pd

# # Function to load data from CSV file
# @st.cache_data()
# def load_data(file_path):
#     df = pd.read_csv(file_path)
#     # Convert 'Timestamp' column to datetime format
#     if 'Timestamp' in df.columns:
#         df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce', unit='s')
#     return df

# # Get file path of CSV file in project folder
# file_path = "output.csv"  # Update with your file path

# if file_path:
#     # Load CSV file
#     df = load_data(file_path)

#     # Show raw data
#     st.subheader("Raw Data")
#     st.write(df)

#     # Show event summary statistics
#     st.subheader("Event Summary Statistics")
#     st.write("Total number of events:", len(df))

#     # Show log level distribution
#     st.subheader("Log Level Distribution")
#     st.write(df['LogLevel'].value_counts())

#     # Show tag distribution
#     st.subheader("Tag Distribution")
#     st.write(df['Tag'].value_counts())
