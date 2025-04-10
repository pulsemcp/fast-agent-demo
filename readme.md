# fast-agent x pulse-mcp demo

## Video

This repository contains the fast-agent source files used in the pulse-mcp demo.

To run the examples, install the [`uv`](https://docs.astral.sh/uv/) package manager then

```
uv pip install fast-agent-mcp
```

Update the `fastagent.secrets.yaml` with your API Keys. Run agents with `uv run agent.py`.

## 0.new-agent

These files are created with the `fast-agent setup` and `fast-agent bootstrap workflow` commands.

## 1.prompts

A demonstration of MCP Prompts and Resources showing in context learning and a PDF Resource being returned within a prompt. fast-agent's built in `prompt-server` is used to deliver the prompts to the agent.

## 2. resource-sampling

An example of a sampling being used to generate a dynamic resource (resource templating).

## 3. multimodal-routing

Example of vision sampling via mcp-webcam, as well as the use of vision to make agent routing decisions. MCP Webcam, Home Assistant and Hugging Face Spaces Servers are used in the demonstration.
