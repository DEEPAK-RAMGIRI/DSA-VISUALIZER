import streamlit as st
from stack_dsa import Stack  

st.title("STACK VISUALIZATION")


if 'stack' not in st.session_state:
    st.session_state.stack = Stack()
    
if 'actions' not in st.session_state:
    st.session_state.actions = []


col1,col3,col2 = st.columns([2,1,3])

with col1:
    inputs = st.text_input("**Enter the value to the stack**")
    
with col2:
    col2a,col2b,col2c = st.columns(3)
    with col2a:
        if st.button("Push"):
            if inputs.strip():
                st.session_state.stack.push(inputs)
                st.session_state.msg_type = "push"
                st.session_state.actions.append(f"Pushed: {inputs}")
                st.session_state.msg_value = inputs
            else:
                st.session_state.msg_type = "warn"
    with col2b:
        if st.button("Pop"):
            popped = st.session_state.stack.pop()
            st.session_state.msg_type = "pop"
            st.session_state.actions.append(f"Pop: {popped}")
            st.session_state.msg_value = popped
            
    with col2c:
        if st.button("peek"):
            top_element = st.session_state.stack.peek()
            st.session_state.msg_type = "peek"
            st.session_state.msg_value = top_element
            
    if st.session_state.get("msg_type") == "push":
        st.markdown(f"**✅ Pushed:** `{st.session_state.msg_value}`")

    elif st.session_state.get("msg_type") == "pop":
        st.markdown(f"**🗑️ Popped:** `{st.session_state.msg_value}`")
        
    elif st.session_state.get("msg_type") == "peek":
        st.markdown(f"**Top Element:** `{st.session_state.msg_value}`")

    elif st.session_state.get("msg_type") == "warn":
        st.markdown("**⚠️ Warning:** Please enter a value.")

st.markdown("-------")



stack_list = st.session_state.stack.print_stack()

if stack_list:
    for item in stack_list:
        st.markdown(
            f"""
            <div style='
                border: 1px solid #4CAF50;
                padding: 4px;
                margin: 2px 0;
                border-radius: 4px;
                background-color: #e8f5e9;
                text-align: center;
                font-size: 12px;
                font-weight: 500;
                color:black;
                width: 120px;
                margin-left: auto;
                margin-right: auto;
            '>
                {item}
            </div>
            """, unsafe_allow_html=True
        )
else:
    st.markdown("<p style='color:red;'>Stack is empty.</p>", unsafe_allow_html=True)

