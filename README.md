# AI Agent Web Search

## Overview
AI Agent Web Search is a Python-based project that leverages LangChain, OpenAI, and Anthropic models to execute queries and parse structured responses. The project is designed to act as a research assistant, generating research papers and saving outputs to text files.

## Features
- **Agent Execution**: Uses LangChain's `AgentExecutor` to process queries and generate structured responses.
- **Tool Integration**: Includes tools for web search (DuckDuckGo) and Wikipedia queries, as well as a custom tool for saving outputs to text files.
- **Multi-LLM Support**: Utilizes OpenAI's GPT-4o and Anthropic's Claude models for generating responses.
- **Custom Output Parsing**: Parses responses into a structured format using Pydantic models.

## Code Structure
### `main.py`
- Defines the main agent execution logic.
- Sets up the prompt template for generating structured responses.
- Invokes the agent with a sample query and parses the response using `PydanticOutputParser`.

### `tools.py`
- Implements tools for web search and Wikipedia queries.
- Includes a custom tool for saving data to text files with timestamps.

### `requirements.txt`
Lists the dependencies required for the project:
- `langchain`
- `wikipedia`
- `langchain-community`
- `langchain-openai`
- `langchain-anthropic`
- `python-dotenv`
- `pydantic`
- `duckduckgo-search`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Theprd1/AI_Agent_Web_Search.git
   cd AI_Agent_Web_Search
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Set up environment variables using a `.env` file (if required).
2. Run the `main.py` file to execute the agent:
   ```bash
   python main.py
   ```
3. The agent will process the query and save the output to a text file.

## Example
Sample query:
```python
raw_response = agent_executor.invoke({"query": "What is a stone?"})
```
Output:
- Raw response from the agent.
- Parsed structured response with topic, summary, sources, and tools used.

## Tools
- **DuckDuckGo Search**: Searches the web for information.
- **Wikipedia Query**: Retrieves information from Wikipedia.
- **Save to File**: Saves the output to a text file with a timestamp.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to submit issues or pull requests to improve the project.

## Author
Developed by [Pradeep](https://github.com/Theprd1).
