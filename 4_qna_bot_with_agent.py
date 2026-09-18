## Approach
## LLM
## Tools - Google Search Tool
## Agent
## Memory
## Streaming
## Web Interface


from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.tools import tool
import streamlit as st


load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    streaming=True
)
search = GoogleSerperAPIWrapper()
tools = [search.run]


if "memory" not in st.session_state:
    st.session_state.memory = MemorySaver()
    st.session_state.history = []

agent = create_agent(
    model = model,
    tools = tools,
    checkpointer=st.session_state.memory,
    system_prompt= "You're an amazing AI assistent and can search on Google as well."
)


st.subheader("my ai chatbot- ans at the speed of thought")
for message in st.session_state.history:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)


query = st.chat_input("Ask Anything..")

if query:
    st.chat_message("user").markdown(query)
    st.session_state.history.append({"role": "user", "content": query})
    
    res = agent.stream(
    {"messages": [{"role": "user", "content": query}]},
    {"configurable": {"thread_id": "1"}},
    stream_mode="messages"
    )
    
    ai_container = st.chat_message("ai")
    with ai_container:
        space = st.empty()
        
        message = ""
        
        for chunk in res:
            message = message + chunk[0].content
            space.write(message)
            
    
        st.session_state.history.append({"role": "ai", "content": message})

