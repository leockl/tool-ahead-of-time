# Tool-Ahead-of-Time (TAoT): Because Why Wait? 🕒
Ever found yourself staring at a shiny new LLM through LangChain's window, but can't use tool calling because it's "not supported yet"? 

*Sad agent noises* 😢

Well, hold my JSON parser, because this repo says "NOT TODAY!" 🦾

## What is this sorcery? 🧙‍♂️

This is a Python package that enables tool calling for any model available through Langchain's ChatOpenAI library (and by extension, any model available through OpenAI's library) and Langchain's AzureAIChatCompletionsModel library, even before LangChain and LangGraph officially supports it! 

Yes, you read that right. We're living in the age of AI and things move fast 🏎️💨

It essentially works by reformatting the output response of the model into a JSON parser and passing this on to the relevant tools.

This repo showcases an example with DeepSeek-R1 671B, which isn't currently supported with tool calling by LangChain and LangGraph (as of 16th Feb 2025).

## Features 🌟

- Tool calling support for OpenAI and non-OpenAI models available on:
  - Langchain's ChatOpenAI library (and by extension, OpenAI and non-OpenAI models available on the base OpenAI's library).
  - Langchain's AzureAIChatCompletionsModel library.
- This package follows a similar method to LangChain's and LangGraph's `create_react_agent` method for tool calling, so makes it easy for you to read the syntax. 😊
- Zero waiting for official support required.
- More robust than a caffeinated developer at 3 AM. ☕

## Quick Start 🚀

Follow the notebook tutorials in the "tutorial" folder in this repo for a fast and practical guide:
- "taot_tutorial_ChatOpenAI.ipynb" file for example notebook tutorial on Langchain's ChatOpenAI library (using DeepSeek-R1 on OpenRouter).
- "taot_tutorial_AzureAIChatCompletionsModel.ipynb" file for example notebook tutorial on Langchain's AzureAIChatCompletionsModel library (using DeepSeek-R1 on Microsoft Azure).
- "taot_tutorial_ChatOpenAI_QwQ32B.ipynb" file for example notebook tutorial on Langchain's ChatOpenAI library (using QwQ-32B on OpenRouter).

## Changelog 📖

20th Feb 2025:
- Package now available on PyPI! Just "pip install taot" and you're ready to go.
- Completely redesigned to follow LangChain's and LangGraph's intuitive `create_react_agent` tool calling methods.
- Produces natural language responses when tool calling is performed.

1st Mar 2025:
- Package now available in TypeScript on npm! Just "npm install taot-ts" and you're ready to go. (https://github.com/leockl/tool-ahead-of-time-ts)

8th Mar 2025:
- Updated repo to include implementation support for Microsoft Azure via Langchain's AzureAIChatCompletionsModel library.

16th Mar 2025:
- Updated repo to include example tutorial for tool calling support for QwQ-32B using Langchain's ChatOpenAI library (hosted on OpenRouter). See "taot_tutorial_ChatOpenAI_QwQ32B.ipynb" file under the "tutorial" folder in this repo. While doing this, I noticed OpenRouter's API for QwQ-32B is unstable and returning empty responses (likely because QwQ-32B is a new model added on OpenRouter only about a week ago). Due to this, I have updated the taot package to keep looping until a non-empty response is returned. If you have previously downloaded the package, please update the package via `pip install --upgrade taot`.
- Checked out OpenAI Agents SDK framework for tool calling support for non-OpenAI providers/models (https://openai.github.io/openai-agents-python/models/) and they don't support tool calling for DeepSeek-R1 (or models available through OpenRouter) yet (as of 16th Mar 2025), so there you go! 😉

## Contributions 🤝

Feel free to contribute! Whether it's adding features, fixing bugs, adding comments in the code or any suggestions to improve this repo, all are welcomed 😄

## Disclaimer ⚠️

This package is like that friend who shows up to the party early - technically not invited yet, but hopes to bring such good vibes that everyone's glad they came.

## License 📜

MIT License - Because sharing is caring, and we care about you having tool calling RIGHT NOW.

---

Made with ❤️ and a healthy dose of impatience.
