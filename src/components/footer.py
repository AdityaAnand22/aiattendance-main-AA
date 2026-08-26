import streamlit as st 

def footer_home():
  
  st.markdown(f"""
              
              <div style="display:flex; gap:6px; align-items: center; justify-content:center; margin-top:2rem">
                
                <p style= 'font-width:bold; color: white;'>Made by Jerry</p>
              </div>
              
              """,unsafe_allow_html=True)
  
  
def footer_dashboard():
  
  st.markdown(f"""
              
              <div style="display:flex; gap:6px; align-items: center; justify-content:center; margin-top:2rem">
                
                <p style= 'font-width:bold; color: black;'>Made by Jerry</p>
              </div>
              
              """,unsafe_allow_html=True)