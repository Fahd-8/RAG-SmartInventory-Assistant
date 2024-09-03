import streamlit as st
from langchain_helper import get_few_shot_db_chain
import time

# Set the page configuration
st.set_page_config(page_title="Smart Inventory: Assistant 👕", page_icon="🛍️", layout="wide")

# Custom CSS for advanced styling and animations
st.markdown("""
    <style>
    .stApp {
        background-color: #f7f7f7;
        font-family: 'Arial', sans-serif;
    }
    .title {
        text-align: center;
        color: #28a745;
        font-size: 4rem;
        font-weight: bold;
        margin-top: 50px;
        margin-bottom: 30px;
        animation: fadeIn 2s ease-in-out, bounce 2s infinite;
    }
    .input-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .input-container input {
        width: 70%;
        padding: 15px;
        font-size: 1.2rem;
        border: 2px solid #28a745;
        border-radius: 5px;
        outline: none;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }
    .input-container input:focus {
        border-color: #218838;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    }
    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 10px;
    }
    .button-container button {
        background-color: #28a745;
        color: white;
        padding: 15px 30px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.2rem;
        transition: background-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .button-container button:hover {
        background-color: #218838;
        transform: scale(1.05);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    .loading-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 200px;
    }
    .loading-spinner {
        border: 16px solid #f3f3f3;
        border-radius: 50%;
        border-top: 16px solid #28a745;
        width: 120px;
        height: 120px;
        animation: spin 2s linear infinite;
    }
    .response-header {
        text-align: center;
        color: #333;
        font-size: 2rem;
        margin-top: 30px;
        animation: fadeIn 2s ease-in-out;
    }
    .response {
        background: white;
        border-radius: 5px;
        padding: 20px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        font-size: 1.2rem;
        color: #555;
        margin: 0 auto;
        width: 70%;
        animation: fadeIn 2s ease-in-out, slideIn 1s ease-in-out;
    }
    .sidebar {
        position: fixed;
        top: 0;
        left: -300px; /* Start hidden off-screen */
        width: 300px;
        height: 100%;
        background-color: #28a745;
        color: white;
        padding: 20px;
        transition: left 0.3s ease-in-out;
        overflow: hidden;
        z-index: 1000;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .sidebar:hover {
        left: 0; /* Slide in when hovered */
    }
    .sidebar-content {
        opacity: 0;
        transform: translateY(20px); /* Start off slightly lower */
        transition: opacity 0.3s ease-in-out, transform 0.3s ease-in-out;
    }
    .sidebar:hover .sidebar-content {
        opacity: 1;
        transform: translateY(0); /* Slide up to normal position */
    }
    .sidebar-header {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 20px;
        animation: fadeIn 2s ease-in-out;
    }
    .sidebar p {
        margin: 0;
        font-size: 1.2rem;
        animation: fadeIn 2s ease-in-out;
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }
    @keyframes slideIn {
        0% { transform: translateY(20px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar with interactive animations
st.sidebar.markdown("""
    <div class="sidebar">
        <div class="sidebar-header">Smart Inventory Assistant</div>
        <div class="sidebar-content">
            <p>Welcome to the Smart Inventory Assistant! Ask me anything about our inventory and I'll do my best to provide you with accurate information.</p>
            <p>Type your question below and hit submit.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Streamlit UI
st.markdown('<div class="title">Smart Inventory: Assistant 👕</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    question = st.text_input("What do you want to know about Inventory?")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if question:
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        submit_button = st.button("Submit")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if submit_button:
            with st.spinner('Processing...'):
                time.sleep(2)  # Simulating a delay for loading animation

                chain = get_few_shot_db_chain()
                response = chain.run(question)
                
                st.markdown('<div class="response-header">Answer</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="response">{response}</div>', unsafe_allow_html=True)
