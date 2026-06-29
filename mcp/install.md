# Install the ChronoVerify MCP server

npm package: `chronoverify-mcp`. Two tools: `verify_image` and `get_signed_report`.

## One-click

- Cursor: `cursor://anysphere.cursor-deeplink/mcp/install?name=chronoverify&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsImNocm9ub3ZlcmlmeS1tY3AiXX0=`
- VS Code: `vscode:mcp/install?%7B%22name%22%3A%22chronoverify%22%2C%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22chronoverify-mcp%22%5D%7D`
- VS Code (badge/redirect): `https://insiders.vscode.dev/redirect/mcp/install?name=chronoverify&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22chronoverify-mcp%22%5D%7D`

## Manual config

Paste into your MCP client config (Claude Desktop `claude_desktop_config.json`, Windsurf `~/.codeium/windsurf/mcp_config.json`, Cline, and others):

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

Omit the `env` block to use the free, rate-limited public path.
