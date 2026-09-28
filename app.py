import streamlit as st
from langchain_core.messages import HumanMessage
from agent import agent

st.set_page_config(page_title="PUCIT Academic Assistant", page_icon="🎓", layout="centered")

st.title("🎓 PUCIT BS(CS) Academic Assistant")
st.write("Ask me about your course grades, semester GPAs, CGPA projections, or graduation targets!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous conversation
for msg in st.session_state.messages:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(msg.content)

# User input handling
if prompt := st.chat_input("Type your question here (e.g., What's my GPA for 78, 85, 64?)"):
    user_msg = HumanMessage(content=prompt)
    st.session_state.messages.append(user_msg)
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Calculating via tools..."):
            try:
                response = agent.invoke({"messages": st.session_state.messages})
                ai_msg = response["messages"][-1]
                st.markdown(ai_msg.content)
                st.session_state.messages.append(ai_msg)
            except Exception as e:
                st.error(f"An error occurred: {e}")