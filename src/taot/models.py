from pydantic import BaseModel, Field

class ToolCall(BaseModel):
    tool: str = Field(..., description="Name of the tool to call")
    args: dict = Field(..., description="Arguments to pass to the tool")