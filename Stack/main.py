import streamlit as st
import time
from stack_dsa import Stack

st.title("📚 STACK VISUALIZATION")

# Init session state
if 'stack' not in st.session_state:
    st.session_state.stack = Stack()
if 'actions' not in st.session_state:
    st.session_state.actions = []
if 'pop_pending' not in st.session_state:
    st.session_state.pop_pending = False
if 'popped_value' not in st.session_state:
    st.session_state.popped_value = None

# Layout
col1, col3, col2 = st.columns([2, 1, 3])

with col1:
    inputs = st.text_input("**Enter the value to the stack**")

with col2:
    col2a, col2b, col2c = st.columns(3)

    with col2a:
        if st.button("Push"):
            if inputs.strip():
                st.session_state.stack.push(inputs)
                st.session_state.msg_type = "push"
                st.session_state.msg_value = inputs
                st.session_state.actions.append(f"Pushed: {inputs}")
            else:
                st.session_state.msg_type = "warn"

    with col2b:
        if st.button("Pop"):
            if not st.session_state.pop_pending and st.session_state.stack.print_stack():
                st.session_state.popped_value = st.session_state.stack.peek()
                st.session_state.pop_pending = True
                st.rerun()

    with col2c:
        if st.button("Peek"):
            top = st.session_state.stack.peek()
            st.session_state.msg_type = "peek"
            st.session_state.msg_value = top

    # Messages
    if st.session_state.get("msg_type") == "push":
        st.markdown(f"**✅ Pushed:** `{st.session_state.msg_value}`")
    elif st.session_state.get("msg_type") == "pop":
        st.markdown(f"**🗑️ Popped:** `{st.session_state.msg_value}`")
    elif st.session_state.get("msg_type") == "peek":
        st.markdown(f"**Top Element:** `{st.session_state.msg_value}`")
    elif st.session_state.get("msg_type") == "warn":
        st.markdown("**⚠️ Warning:** Please enter a value.")

st.markdown("---")

# Step 1: Show top in red before removing
if st.session_state.pop_pending:
    stack_list = st.session_state.stack.print_stack()
    top_value = st.session_state.popped_value
    for index, item in enumerate(stack_list):
        is_top = (index == 0 and item == top_value)
        bg_color = "#ffcccc" if is_top else "#e8f5e9"
        border_color = "#ff1744" if is_top else "#4CAF50"
        st.markdown(
            f"""
            <div style='
                border: 2px solid {border_color};
                padding: 6px;
                margin: 5px 0;
                border-radius: 8px;
                background-color: {bg_color};
                text-align: center;
                font-size: 14px;
                font-weight: 600;
                color: black;
                width: 130px;
                margin-left: auto;
                margin-right: auto;
            '>
                {item}
            </div>
            """,
            unsafe_allow_html=True
        )
    time.sleep(0.3)
    popped = st.session_state.stack.pop()
    st.session_state.actions.append(f"Popped: {popped}")
    st.session_state.msg_type = "pop"
    st.session_state.msg_value = popped
    st.session_state.pop_pending = False
    st.rerun()

# Normal display
else:
    stack_list = st.session_state.stack.print_stack()
    if stack_list:
        for item in stack_list:
            st.markdown(
                f"""
                <div style='
                    border: 2px solid #4CAF50;
                    padding: 6px;
                    margin: 5px 0;
                    border-radius: 8px;
                    background-color: #e8f5e9;
                    text-align: center;
                    font-size: 14px;
                    font-weight: 600;
                    color: black;
                    width: 130px;
                    margin-left: auto;
                    margin-right: auto;
                '>
                    {item}
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.markdown("<p style='color:red;'>Stack is empty.</p>", unsafe_allow_html=True)
