"""Load ChronoVerify as native LangChain tools (verify_image, get_signed_report).

Install:  pip install langchain-mcp-adapters
"""
from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
    {
        "chronoverify": {
            "command": "npx",
            "args": ["-y", "chronoverify-mcp"],
            "transport": "stdio",
            # "env": {"CHRONOVERIFY_API_KEY": "cv_live_..."},  # optional, for metered use
        },
    }
)

# tools = await client.get_tools()   # pass these to your agent
# On Windows, an npx stdio server sometimes needs command "npx.cmd".
