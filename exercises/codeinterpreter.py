import os
os.environ["OPENAI_API_KEY"] = "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"

from codeinterpreterapi import CodeInterpreterSession


async def main():
    # create a session
    session = CodeInterpreterSession(model="gpt-3.5-turbo")
    await session.astart()

    # generate a response based on user input
    response = await session.generate_response(
        "Plot the Apple stock price chart from 2007 to 2023 june"
    )

    # output the response (text + image)
    print("AI: ", response.content)
    for file in response.files:
        file.show_image()

    # terminate the session
    await session.astop()


if __name__ == "__main__":
    import asyncio
    # run the async function
    asyncio.run(main())
    