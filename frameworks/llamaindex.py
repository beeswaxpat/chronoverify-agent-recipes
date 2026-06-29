"""Load ChronoVerify as LlamaIndex tools (verify_image, get_signed_report).

Install:  pip install llama-index-tools-mcp
"""
from llama_index.tools.mcp import BasicMCPClient, McpToolSpec

client = BasicMCPClient(
    "npx",
    args=["-y", "chronoverify-mcp"],
    # env={"CHRONOVERIFY_API_KEY": "cv_live_..."},  # optional, for metered use
)
tools = McpToolSpec(client=client).to_tool_list()
