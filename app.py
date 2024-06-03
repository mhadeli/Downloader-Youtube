# Import necessary libraries
import streamlit as st
from pytube import YouTube
import ssl
import os

# Disable SSL verification (not recommended in production)
ssl._create_default_https_context = ssl._create_unverified_context

# Set the title of the Streamlit app
st.title("YouTube Video Downloader")

# Create a text input box for the user to enter the YouTube link
link = st.text_input("Enter Link of Youtube Video:")

# Initialize the yt variable in the session state
if "yt" not in st.session_state:
    st.session_state.yt = None

# Create a button to get the video details
if st.button("Get Video Details"):
    try:
        # Create a YouTube object with the entered link
        yt = YouTube(link)
        # Store the YouTube object in the session state
        st.session_state.yt = yt
    except Exception as e:
        # Display an error message if there's an exception
        st.error("Error: ", e)

# If the yt object is not None, display the video details
if st.session_state.yt:
    # Display the video title
    st.write("Title :", st.session_state.yt.title)
    # Display the video views
    st.write("Views :", st.session_state.yt.views)
    # Display the video duration
    st.write("Duration :", st.session_state.yt.length)
    # Display the video description
    st.write("Description :", st.session_state.yt.description)
    # Display the video ratings
    st.write("Ratings :", st.session_state.yt.rating)

    # Create a button to download the video
    if st.button("Download Video"):
        # Get the highest resolution stream
        stream = st.session_state.yt.streams.get_highest_resolution()
        # Set the download path to the current directory
        download_path = os.path.dirname(__file__)
        # Download the video
        stream.download(output_path=download_path)
        # Display a success message
        st.success("Download completed!!")