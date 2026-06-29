# ChronoVerify agent recipes

Drop-in recipes to give any AI agent one capability: **verify a photo's capture
time and provenance** (cryptographic C2PA Content Credentials validation, EXIF and
XMP metadata, and classical pixel forensics) and return one verdict with a
confidence and a signed audit record.

Provenance-first, **not** a deepfake or AI-generation detector. Results are
investigative triage, not proof.

- Website: https://chronoverify.com
- Integrations: https://chronoverify.com/integrations
- API and method: https://chronoverify.com/method#api
- npm (MCP server): https://www.npmjs.com/package/chronoverify-mcp
- npm / PyPI (SDKs): `chronoverify`

## One-click MCP install

[![Add to Cursor](https://img.shields.io/badge/Add%20to-Cursor-1f1f1f?style=flat-square)](cursor://anysphere.cursor-deeplink/mcp/install?name=chronoverify&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsImNocm9ub3ZlcmlmeS1tY3AiXX0=)
[![Install in VS Code](https://img.shields.io/badge/VS%20Code-Install-blue?style=flat-square&logo=visualstudiocode)](https://insiders.vscode.dev/redirect/mcp/install?name=chronoverify&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22chronoverify-mcp%22%5D%7D)

Or paste this into your MCP client config (Claude Desktop, Claude Code, Cline,
Windsurf):

```json
{
  "mcpServers": {
    "chronoverify": {
      "command": "npx",
      "args": [
        "-y",
        "chronoverify-mcp"
      ],
      "env": {
        "CHRONOVERIFY_API_KEY": "cv_live_..."
      }
    }
  }
}
```

Omit the `env` block to use the free, rate-limited public path. See
[`mcp/install.md`](mcp/install.md) for every client.

## Direct function calling

Copy-paste tool definitions:

- [`tool-definitions/openai-chat-completions.json`](tool-definitions/openai-chat-completions.json)
- [`tool-definitions/openai-responses.json`](tool-definitions/openai-responses.json)
- [`tool-definitions/anthropic-messages.json`](tool-definitions/anthropic-messages.json)

When the model calls `chronoverify_verify_image`, POST the arguments to
`https://chronoverify.com/v1/verify` and return the JSON verdict.

## Frameworks

Point each framework's MCP adapter at the published server:

- [`frameworks/langchain.py`](frameworks/langchain.py)
- [`frameworks/llamaindex.py`](frameworks/llamaindex.py)
- [`frameworks/crewai.py`](frameworks/crewai.py)
- [`frameworks/n8n.md`](frameworks/n8n.md)

## SDKs

Runnable examples on the first-party SDKs:

- Python ([`examples/example.py`](examples/example.py)): `pip install chronoverify`
- TypeScript ([`examples/example.ts`](examples/example.ts)): `npm i chronoverify`

## Claude Skill

[`skill/SKILL.md`](skill/SKILL.md) is a ready Claude skill that calls the MCP tool
or the REST API.

## License

MIT
