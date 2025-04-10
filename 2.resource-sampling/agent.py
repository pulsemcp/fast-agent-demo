import asyncio

from mcp_agent.core.fastagent import FastAgent
fast: FastAgent = FastAgent("Story Sampling Example")


@fast.agent(name="story_teller",servers=["stories"])

async def main() -> None:
    async with fast.run() as agent:
        await agent.story_teller.with_resource(
            resource_uri="resource://fast-agent/short-story/space-adventure",
            prompt_content="Summarize the content of this story"
        )
        await agent.interactive()

if __name__ == "__main__":
    asyncio.run(main())

