import streamlit as st 
from src.components.header import header_home
from src.components.footer import footer_home
from ui.base_layout import style_base_layout, style_background_home

def home_screen():
  
  
  header_home()
  style_background_home()
  style_base_layout()
  
  col1, col2 = st.columns(2, gap='large')
  
  with col2:
    st.header("I'm Teacher")
    st.image("https://i.ibb.co/Kj9xhqy7/Gemini-Generated-Image-a6eufsa6eufsa6eub.png", width= 120)
    if st.button('Teacher portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
      st.session_state['login_type'] = 'teacher'
      st.rerun()
      
  with col1:
    st.header("I'm Student")
    st.image("https://i.ibb.co/bM1F5Ym0/Gemini-Generated-Image-a6eufsa6eufsa6euv.png", width= 120)
    if st.button('Student portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
      st.session_state['login_type'] = 'student'
      st.rerun()
      
  footer_home()
  