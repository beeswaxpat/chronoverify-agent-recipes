"""Give a CrewAI agent ChronoVerify's tools (verify_image, get_signed_report).

Install:  pip install 'crewai-tools[mcp]'

StdioServerParameters comes from the `mcp` package, not from crewai_tools.
"""
from crewai import Agent
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters

params = StdioServerParameters(
    command="npx",
    args=["-y", "chronoverify-mcp"],
    # env={"CHRONOVERIFY_API_KEY": "cv_live_..."},  # optional, for metered use
)

with MCPServerAdapter(params) as mcp_tools:
    verifier = Agent(
        role="Image Provenance Verifier",
        goal="Verify image capture-time and provenance with ChronoVerify",
        backstory="I check C2PA, EXIF, and pixel forensics.",
        tools=mcp_tools,
    )
