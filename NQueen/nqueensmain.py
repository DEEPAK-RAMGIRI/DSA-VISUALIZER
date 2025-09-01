import streamlit as st
from NQueen.nqueens_dsa import queens 


def main():
    st.title("N QUEENS VISUALIZATION")
    
    st.markdown(
        """
        <style>
            .stApp{
                    background: linear-gradient(280deg,#0020ff,#ff0004,#eb00ff);
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

    chess = None 
    N = st.text_input("Enter a valid chessboard size:", "")
    if st.button("GET BOARD"):    
        if N.isdigit():
            N = int(N)
            chess = queens(N)
            if not chess:
                st.write(f"NOT POSSIBLE WITH {N} board")
            # else:
            #     html_board = '<div style="display: inline-block;">'
            else:
                for i, row in enumerate(chess):
                    html_board += '<div style="display: flex;">'
                    for j, c in enumerate(row):
                        color = "#f0d9b5" if (i+j)%2==0 else "#b58863" 
                        piece = '👑' if c=='Q' else ""
                        html_board += f'<div style="width:50px; height:50px; background-color:{color}; display:flex; align-items:center; justify-content:center; font-size:30px;">{piece}</div>'
                    html_board += '</div>'
                html_board += '</div>'

                st.markdown(html_board, unsafe_allow_html=True)
        else:
            st.markdown("<p style='color:red;'>Please enter a valid number for the board size..</p>", unsafe_allow_html=True)
