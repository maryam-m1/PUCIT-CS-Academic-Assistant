from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from agent import agent

load_dotenv()

llm = init_chat_model("groq:openai/gpt-oss-20b")

st.set_page_config(page_title="PUCIT Academic Assistant", page_icon="🎓", layout="centered")

st.title("🎓 PUCIT BS(CS) Academic Assistant")
st.write("Ask me about your course grades, semester GPAs, CGPA projections, or graduation targets!")

# Initialize chat history in session state if not present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display prior chat messages
for msg in st.session_state.messages:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(msg.content)

# Accept user input
if prompt := st.chat_input("Type your question here (e.g., What's my GPA for 78, 85, 64?)"):
    # Add user message to session state
    user_msg = HumanMessage(content=prompt)
    st.session_state.messages.append(user_msg)
    
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response from agent using full message history
    with st.chat_message("assistant"):
        with st.spinner("Calculating via tools..."):
            try:
                response = agent.invoke({"messages": st.session_state.messages})
                ai_msg = response["messages"][-1]
                st.markdown(ai_msg.content)
                # Append assistant response to session state
                st.session_state.messages.append(ai_msg)
            except Exception as e:
                st.error(f"An error occurred: {e}")