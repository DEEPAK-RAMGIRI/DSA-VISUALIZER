import streamlit as st
from streamlit_option_menu import option_menu
from Stack import stackmain
from Queue import queuemain
from NQueen import nqueensmain
from SUDOKU import sudokumain

st.markdown(
        """
        <style>
            .stApp{
                    background: radial-gradient(circle, #ee7752, #e73c7e, #23a6d5, #23d5ab);
                    background-size: 180% 180%;
                    animation: gradient-animation 12s ease infinite;
                     
                }

                @keyframes gradient-animation {
                    0% {
                        background-position: 0% 50%;
                    }
                    50% {
                        background-position: 100% 50%;
                    }
                    100% {
                        background-position: 0% 50%;
                    }
                }
        </style>
        
        """,unsafe_allow_html=True
    )


with st.sidebar:
    selected = option_menu(
        menu_title = None,
        options = ["Home","Stack","Queue",'N queens','Sudoku'],
        default_index = 0,
    )

if selected == "Home":
    st.title("THIS IS HOME PAGE")
    st.markdown('''
            Hi, I'm Deepak (RDK)👋.
I built this project to showcase my Data Structures and Algorithms (DSA) skills. I used ⚡ Streamlit to create a fast and interactive frontend, so you can explore different visualizations with ease.

👉 Start by checking out the 📂 Main Menu on the left side — just click and explore the features. 🚀

🛠️ I'm also currently working on adding more visualizations to make this project even better. Stay tuned for updates!

💡 I'm always open to feedback! If you have any suggestions for improvements, feel free to share them. I’ll definitely consider your thoughts and work on them whenever possible.

✨ So, dive in, experiment, and have fun exploring! 🎉''')

elif selected == "Stack":
    stackmain.main()
    
elif selected == "Queue":
    queuemain.main()

elif selected == "N queens":
    nqueensmain.main()
    
elif selected == "Sudoku":
    sudokumain.main()
    
    
    