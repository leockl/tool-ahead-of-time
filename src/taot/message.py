from langchain_core.output_parsers import JsonOutputParser
from .models import ToolCall

def create_system_message_taot(system_message: str) -> str:
    """
    Create a system message with tool instructions and JSON schema.
    
    Args:
        system_message (str): The specific system message for tools
        
    Returns:
        str: Formatted system message with JSON schema instructions
    """
    json_parser = JsonOutputParser(pydantic_object=ToolCall)
    
    sys_msg_taot = (f"{system_message}\n"
                    f"When a user's question matches a tool's capability, you MUST use that tool. "
                    f"Do not try to solve problems manually if a tool exists for that purpose.\n"
                    f"Output ONLY a JSON object (with no extra text) that adheres EXACTLY to the following schema:\n\n"
                    f"{json_parser.get_format_instructions()}\n\n"
                    f"If the user's question doesn't require any tool, answer directly in plain text with no JSON.")

    return sys_msg_taot