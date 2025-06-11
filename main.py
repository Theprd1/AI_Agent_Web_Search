from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
load_dotenv()

#Defining the prompt template
class CapitalResponse(BaseModel):
    topic:str
    summary: str
    sources:list[str]
    tools_used: list[str]



llm1 = ChatOpenAI(model="gpt-4o")
llm2 = ChatAnthropic(model="claude-3-5-sonnet-20240229")
parser = PydanticOutputParser(pydantic_object=CapitalResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use neccessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

agent = create_tool_calling_agent(
    llm=llm2,
    tools=[],
    prompt=prompt,
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[],
    verbose=True,
)

raw_response = agent_executor.invoke({"query": "What is a stone?"})
print(raw_response)