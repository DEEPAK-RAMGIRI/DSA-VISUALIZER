import streamlit as st
from NQueen.nqueens_dsa import queens 


def main():
    st.title("N QUEENS VISUALIZATION")

    chess = None 
    N = st.text_input("Enter a valid chessboard size:", "")
    if st.button("Push"):
    
        if N.isdigit():
            N = int(N)
            chess = queens(N)
            print(chess)  

            if not chess:
                st.write(f"NOT POSSIBLE WITH {N} board")
            else:
                for i, row in enumerate(chess):
                    st.write(" ".join(['👑' if c=='Q' else '⬛' if (i+j)%2 else '🔲' for j, c in enumerate(row)]))

        else:
            st.markdown("<p style='color:red;'>Please enter a valid number for the board size..</p>", unsafe_allow_html=True)
