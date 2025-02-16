from typing import List, Callable
from pydantic import BaseModel, Field, TypeAdapter
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_core.runnables import Runnable
import re

class ToolCall(BaseModel):
    tool: str = Field(..., description="Name of the tool to call")
    args: dict = Field(..., description="Arguments to pass to the tool")

class ManualToolAgent(Runnable):
    """
    A custom agent that handles tools manually.
    """
    def __init__(self, model: ChatOpenAI, tools: List[Callable]):
        self.model = model
        self.tools = tools
        self.json_parser = JsonOutputParser(pydantic_object=ToolCall)
        self.base_executor = create_react_agent(model, tools=[])
    
    def convert_messages(self, messages: List[dict]) -> List[SystemMessage | HumanMessage | AIMessage]:
        """
        Convert dictionary-based messages to LangChain message objects.
        """
        converted_messages = []
        
        message_types = {
            "system": SystemMessage,
            "user": HumanMessage,
            "assistant": AIMessage
        }
        
        for message in messages:
            role = message["role"]
            content = message["content"]
            
            if role in message_types:
                MessageClass = message_types[role]
                converted_message = MessageClass(content=content)
                converted_messages.append(converted_message)
                
        return converted_messages
    
    def invoke(self, inputs: dict) -> dict:
        """
        Execute the agent with manual tool handling.
        
        Args:
            inputs (dict): Dictionary containing messages
            
        Returns:
            dict: Response containing processed message
        """
        # Get messages
        messages = inputs["messages"]
        system_msg = messages[0]
        previous_message = messages[1] if len(messages) > 2 else []
        human_msg = messages[-1]
        
        # Create messages with proper format
        formatted_system_msg = SystemMessage(
            content=(
                "You are a helpful assistant with access to specific tools. "
                "When a user's question matches a tool's capability, you MUST use that tool. "
                "Do not try to solve problems manually if a tool exists for that purpose.\n\n"
                f"{system_msg}\n"
                "Output ONLY a JSON object (with no extra text) that adheres EXACTLY to the following schema:\n\n"
                f"{self.json_parser.get_format_instructions()}\n\n"
                "If the user's question doesn't require any tool, answer directly in plain text with no JSON."
            )
        )
        
        # Add previous messages
        formatted_messages = [{"role": "system", "content": formatted_system_msg.content}]
        if previous_message:
            if isinstance(previous_message, list):
                formatted_messages.extend(previous_message)
        
        # Convert messages to LangChain format
        converted_formatted_messages = self.convert_messages(formatted_messages)
        
        # Add human message
        formatted_human_msg = HumanMessage(content=human_msg)
        all_messages = converted_formatted_messages + [formatted_human_msg]
        
        # Get response from base executor
        response = self.base_executor.invoke({"messages": all_messages})
        last_response = response["messages"][-1].content
        
        # Process JSON response
        matches = re.findall(r'(\{.*?\})', last_response, re.DOTALL)
        json_text = None
        for m in matches:
            if '"tool"' in m and '"args"' in m:
                json_text = m
                break
        
        if json_text:
            try:
                adapter = TypeAdapter(ToolCall)
                parsed = self.json_parser.parse(json_text)
                
                if isinstance(parsed, dict):
                    tool_call = adapter.validate_python(parsed)
                else:
                    tool_call = parsed
                
                # Find the matching tool
                tool_dict = {tool.name: tool for tool in self.tools}
                
                if tool_call.tool in tool_dict:
                    result = tool_dict[tool_call.tool].invoke(tool_call.args)
                else:
                    result = "Error: Unknown tool"
            except Exception as e:
                result = f"Error processing tool call: {str(e)}"
        else:
            result = re.sub(r'<think>.*?</think>', '', last_response, flags=re.DOTALL).strip()
        
        return {"messages": [{"content": result}]}

def create_react_agent_manual_tool(model: ChatOpenAI, tools: List[Callable]) -> ManualToolAgent:
    """
    Create a React agent with manual tool handling.
    
    Args:
        model (ChatOpenAI): The language model to use
        tools (List[Callable]): List of tool functions
        
    Returns:
        ManualToolAgent: Agent with manual tool handling
    """
    return ManualToolAgent(model, tools)
