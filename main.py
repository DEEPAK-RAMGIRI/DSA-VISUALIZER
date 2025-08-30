import streamlit as st
from streamlit_option_menu import option_menu
from Stack import stackmain
from Queue import queuemain
from NQueen import nqueensmain


with st.sidebar:
    selected = option_menu(
        menu_title = None,
        options = ["Home","Stack","Queue",'LRU','N queens','Sudoku'],
        default_index = 0,
    )

if selected == "Home":
    st.title("THIS IS HOME PAGE")
    st.info("well this is a normal page or u can consider it as my about page go to sidebar to find out all visualizers available ")

elif selected == "Stack":
    stackmain.main()
    
elif selected == "Queue":
    queuemain.main()

elif selected == "N queens":
    nqueensmain.main()
    
    
    