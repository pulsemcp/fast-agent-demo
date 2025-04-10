import asyncio

from mcp_agent.core.fastagent import FastAgent

fast: FastAgent = FastAgent("Home Assistant Demo")


@fast.agent(
    "hass",
    servers=["hass", "prompts"],
    instruction="you have control of my house",
    model="sonnet",
)
async def main() -> None:
    # Use the app's context manager
    async with fast.run() as agent:
        await agent.interactive()


if __name__ == "__main__":
    asyncio.run(main())
