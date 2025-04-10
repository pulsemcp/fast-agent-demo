import asyncio

from mcp_agent.core.fastagent import FastAgent

fast: FastAgent = FastAgent("MCP WebCam Demo")


@fast.agent(
    "webcam",
    servers=["mcp_webcam"],
    instruction="produce a very detailed description of the captured image",
    model="sonnet",
)
@fast.router("router", agents=["product", "room"])
@fast.agent(
    "product",
    instruction="if the human is holding an item, change the colour of the office"
    "backlight to match the item",
    servers=["hass"],
)
@fast.agent(
    "room",
    instruction="if there is no human in the frame, describe the scene. "
    "use shuttleai jaguar to"
    "generate an image  and reproduce it!",
    servers=["mcp_hfspace"],
)
@fast.chain(name="workflow", sequence=["webcam", "router"])
async def main() -> None:
    async with fast.run() as agent:
        await agent.interactive()


if __name__ == "__main__":
    asyncio.run(main())
