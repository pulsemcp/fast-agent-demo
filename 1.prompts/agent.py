import asyncio

from mcp_agent.core.fastagent import FastAgent
fast: FastAgent = FastAgent("MCP WebCam Demo")


@fast.agent(name="sizer",servers=["prompt_server"],model="sonnet")

async def main() -> None:
    # Use the app's context manager
    async with fast.run() as agent:
        await agent()


if __name__ == "__main__":
    asyncio.run(main())

