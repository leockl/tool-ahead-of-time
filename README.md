# Tool-Ahead-of-Time (TAoT): Because Why Wait? 🕒
Ever found yourself staring at a shiny new LLM through Langchain's window, but can't use tool calling because it's "not supported yet"? 

*Sad react-agent noises* 😢

Well, hold my JSON parser, because this repo says "NOT TODAY!" 🦾

## What is this sorcery? 🧙‍♂️

This is a Python package that enables tool calling for any model available through Langchain's ChatOpenAI library (and by extension, any model available through OpenAI's library), even before LangChain and LangGraph officially supports it! 

Yes, you read that right. We're living in the age of AI and things move fast 🏎️💨

It essentially works by reformatting the output response of the model into a JSON parser and passing this on to the relevant tools.

This repo showcases an example with DeepSeek-R1 671B, which isn't currently supported with tool calling by LangChain and LangGraph (as of 16th Feb 2025).

## Features 🌟

- Tool calling support for OpenAI and non-OpenAI models available on Langchain's ChatOpenAI library (and by extension, OpenAI and non-OpenAI models available on the base OpenAI's library).
- This package follows a similar method to LangChain's and LangGraph's `create_react_agent` method with tool calling (with plans to expand this later), so makes it easy for you to read the syntax. 😊
- More robust than a caffeinated developer at 3 AM. ☕
- Zero waiting for official support required.

## Quick Start 🚀

Follow the notebook tutorial in the "taot_tutorial.ipynb" file (under the "tutorial" folder) in this repo for a fast and practical guide.

UPDATE 20th Feb 2025:
- Package now available on PyPI! Just "pip install taot" and you're ready to go.
- Completely redesigned to follow LangChain's and LangGraph's intuitive tool calling methods.
- Produces natural language responses when tool calling is performed.

## Contributions 🤝

Feel free to contribute! Whether it's adding features, fixing bugs, adding comments in the code or any suggestions to improve this repo, all are welcomed 😄

## Disclaimer ⚠️

This package is like that friend who shows up to the party early - technically not invited yet, but hopes to bring such good vibes that everyone's glad they came.

## License 📜

MIT License - Because sharing is caring, and we care about you having tool calling RIGHT NOW.

---

Made with ❤️ and a healthy dose of impatience.
