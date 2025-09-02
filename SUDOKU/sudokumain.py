import streamlit as st
import pandas as pd
from SUDOKU.sudokudsa import sudoku_solver
from SUDOKU.validsudoku import valid_sudoku

def main():
    st.markdown(
        """
        <style>
            .stApp{
                    background: linear-gradient(135deg, #00f260, #0575e6, #ff00cc);
                    background-sixze: 180% 180%;
                    animation: gradient-animation 7s ease infinite;
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

    st.markdown("<h1 style='color:black;text-align:center; font-weight:bold;'>SUDOKU SOLVER</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:black; font-size:18px; font-weight:bold'>Sudoku Input Grid </p>", unsafe_allow_html= True)


    sudoku_input = []
    for i in range(9):
        cols = st.columns(9)
        row = ['.'] * 9
        for j in range(9):
            val = cols[j].text_input(f"cell-{i}-{j}", max_chars=1, key=f"{i}-{j}",label_visibility="collapsed")
            if val:row[j] = val
        sudoku_input.append(row)
        
        # print(sudoku_input)
    if st.button("submit"):
        if valid_sudoku(sudoku_input):
            sudoku = sudoku_solver(sudoku_input)
            html_board = '<div style="display: inline-block;border: 4px solid black;">'
            for i, row in enumerate(sudoku):
                html_board += '<div style="display: flex;">'
                for j, val in enumerate(row):
                    top = "4px solid black" if i % 3 == 0 else "1px solid gray"
                    left = "4px solid black" if j % 3 == 0 else "1px solid gray"
                    bottom = "4px solid black" if i == 8 else "1px solid gray"
                    right = "4px solid black" if j == 8 else "1px solid gray"
                    
                    color = "#ffffff" if (i+j)%2==0 else "#f5f5dc"  
                    
                    html_board += f'<div style="width:50px; height:50px; margin:1px; background-color:{color}; display:flex; align-items:center; justify-content:center; font-size:24px; font-weight:bold; color:black;  border-top: {top}; border-left: {left}; border-bottom: {bottom}; border-right: {right}">{val}</div>'
                html_board += '</div>'
            html_board += '</div>'
            st.markdown(html_board, unsafe_allow_html=True)
        else:
            st.markdown("<p style='color:red;'>WE CANNOT CREATE VAILD SUDOKU WITH YOUR VALUES</p>", unsafe_allow_html=True)
        
if __name__ == "__main__":
    main()