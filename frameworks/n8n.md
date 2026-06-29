# ChronoVerify in n8n

n8n is HTTP-native and ChronoVerify is a REST API, so an **HTTP Request node** is
the most reliable path.

## HTTP Request node

- **Method:** POST
- **URL:** `https://chronoverify.com/v1/verify`
- **Headers:** `Authorization: Bearer cv_live_...` (omit for the free public path)
- **Body:** form-data, field `url` = the image URL (or send a binary `file` field
  for an uploaded image)

Branch on `verdict` and `confidence` in the JSON response.

## As an MCP tool

n8n's built-in MCP Client Tool node connects over HTTP/SSE, not stdio, so it
cannot launch `npx` directly. Bridge the stdio server to SSE:

```bash
npx -y supergateway --stdio "npx -y chronoverify-mcp" --port 8000
```

then point the MCP Client Tool node at `http://localhost:8000/sse`.
