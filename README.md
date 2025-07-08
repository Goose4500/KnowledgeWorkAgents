# KnowledgeWorkAgents
PydanticAI agents exposed as Model Context Protocol servers focused on knowledge work - self-contained with PEP 723 dependencies

## Usage

```json
{
    "mcpServers": {
      "competitive-intelligence-agent": {
            "command": "uv",
            "args": ["run", "PATH"],
            "env": {
              "GOOGLE_API_KEY": "",
              "LOGFIRE_TOKEN": ""
            }
          }
        }
      }
```