import streamlit as st
import time
from Queue.queue_dsa import Queue

def main():
    
    st.markdown(
        """
        <style>
            .stApp{
                    background: linear-gradient(200deg,#511D43,#FDFFB8,#4DFFBE,#63C8FF);
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
    if 'queue' not in st.session_state:
        st.session_state.queue = Queue()

    if 'colors' not in st.session_state:
        st.session_state.colors = []

    if 'last_action' not in st.session_state:
        st.session_state.last_action = None

    st.title("QUEUE VISUALIZER")

    col1, col3, col2 = st.columns([2, 1, 3])

    with col1:
        value = st.text_area("Enter Value", key="box", height=100, label_visibility="collapsed")
        st.markdown('<div class="custom-input"></div>', unsafe_allow_html=True)
    # st.write("You entered:", value)


    with col2:
        c1, c2 = st.columns(2)
        c3, c4 = st.columns(2)

        with c1:
            if st.button("ENQUEUE"):
                if value:
                    st.session_state.queue.enque(value.strip())
                    st.session_state.colors.append("green")
                    st.session_state.last_action = "enqueue"
                    st.rerun()

        with c2:
            if st.button("Dequeue"):
                if not st.session_state.queue.isempty():
                    st.session_state.colors[0] = "red"  
                    st.session_state.last_action = "dequeue"
                    st.rerun()
        
        with c3:
            if st.button("Peek"):
                if not st.session_state.queue.isempty():
                    st.session_state.colors[0] = "yellow"
                    st.session_state.last_action = "peek"
                    st.rerun()

        with c4:
            if st.button("Clear"):
                st.session_state.queue.clear()
                st.session_state.colors.clear()
                st.session_state.last_action = None
            

    # st.markdown(f"**Queue Size:** {len(st.session_state.queue)}")
    st.markdown("---")
    if len(st.session_state.queue) > 0:
        queue_html = ""
        for item, color in zip(st.session_state.queue, st.session_state.colors):
            print(color)
            queue_html += f'<div style="display:inline-block;margin:5px;padding:10px 20px;background-color:{color};color:black;border-radius:5px;border:1px solid #333;">{item}</div>'
        st.markdown(queue_html, unsafe_allow_html=True)


        if st.session_state.last_action == "dequeue" and st.session_state.colors[0] == "red":
            time.sleep(0.5)
            st.session_state.queue.deque()
            st.session_state.colors.pop(0)
            st.session_state.last_action = None
            st.rerun()

        elif st.session_state.last_action == "enqueue":
            st.session_state.colors[-1] = "skyblue"
            st.session_state.last_action = None
            st.rerun()

        elif st.session_state.last_action == "peek":
            time.sleep(0.5)
            st.session_state.colors[0] = "skyblue"
            st.session_state.last_action = None
            st.rerun()

    else:
        st.markdown("<p style='color:red;'>Queue is empty.</p>", unsafe_allow_html=True)
