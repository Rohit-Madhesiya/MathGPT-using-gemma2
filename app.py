import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain,LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool,initialize_agent
from langchain.callbacks import StreamlitCallbackHandler

# setup the streamlit frontend
st.set_page_config(page_title="Text to Math Problem Solver and Data Search Assistant")
st.title("Text to Math Problem Solver and Data Search Assistant using Gemma2 Model")

groq_api_key=st.sidebar.text_input(label="GROQ API KEY",type="password")

if not groq_api_key:
  st.info("Please add your Groq API Key to continue")

# model
llm_model=ChatGroq(
  model_name="gemma2-9b-it",
  groq_api_key=groq_api_key
)

# initializing the tools
wikipedia_wrapper=WikipediaAPIWrapper()
wikipedia_tool=Tool(
  name='Wikipedia',
  func=wikipedia_wrapper.run,
  description='A tool for searching the Internet to find various information on mentioned topics'
)


# initialize the Math tool
math_chain=LLMMathChain.from_llm(llm=llm_model)
calculator_tool=Tool(
  name="Calculator",
  func=math_chain.run,
  description="A tool for answering math related questions. Only input mathematical expression needs to be provided."
)

prompt=""" 
You are an agent tasked for solving users mathematical questions. Logically arrive at the solution and provide a detailed explanation and display it point-wise for the question below
Question:{question}
Answer:
"""

prompt_template=PromptTemplate(
  input_variables=['question'],
  template=prompt
)

# combine all the tools into chain
chain=LLMChain(llm=llm_model,prompt=prompt_template)

reasoning_tool=Tool(
  name="Reasoning Tool",
  func=chain.run,
  description="A tool for answering logic-based and reasoning questions."
)

# initialize the agents
assistant_agent=initialize_agent(
  tools=[wikipedia_tool,calculator_tool,reasoning_tool],
  llm=llm_model,
  agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
  verbose=True,
  handle_parsing_errors=True
)

if "messages" not in st.session_state:
  st.session_state["messages"]=[
    {"role":"assistant","content":"Hi, I am a Math Chatbot who can answer all your maths questions"}
  ]

for msg in st.session_state.messages:
  st.chat_message(msg['role']).write(msg['content'])

# function to generate the response
def generate_response(question):
  response=assistant_agent.invoke({'input':question})
  return response

# interaction
question=st.text_area("Enter your question:","")

if st.button("Find my answer"):
  if question:
    with st.spinner("Solving.."):
      st.session_state.messages.append({"role":"user","content":question})
      st.chat_message("user").write(question)

      st_callback=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
      response=assistant_agent.run(st.session_state.messages,callbacks=[st_callback])

      st.session_state.messages.append({"role":"assistant","content":response})
      # st.chat_message("assistant")write(response)
      st.write("### Response:")
      st.success(response)
  else:
    st.warning("Please enter your question!!")





