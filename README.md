# Tool Ahead Of Time: Because Why Wait? 🕒
Ever found yourself staring at a shiny new LLM through Langchain's window, but can't use tool calling because it's "not supported yet"? 

*Sad react-agent noises* 😢

Well, hold my JSON parser, because this repo says "NOT TODAY!" 🦾

## What is this sorcery? 🧙‍♂️

This is a Python package that enables tool calling for any model available on Langchain's ChatOpenAI library (and by extension, any model available on the base OpenAI's library), even before LangChain and LangGraph officially supports it! 

Yes, you read that right. We're living in the age of AI and things move fast 🏎️💨

This repo showcases with DeepSeek-R1, which isn't currently supported with tool calling by LangChain and LangGraph (as of 16th Feb 2025).

## Features 🌟

- Tool calling support for OpenAI and non-OpenAI models available through Langchain's ChatOpenAI library (and by extension, OpenAI and non-OpenAI models available through OpenAI's library).
- Handles conversation history like a pro.
- More robust than a caffeinated developer at 3 AM. ☕
- Zero waiting for official support required.

## Quick Start 🚀

The repo essentially works by reformatting the output reponse of the model into a JSON parser and passing this on to a tool.

Follow the tutorial in the "tool-ahead-of-time-tutorial.ipynb" file in this repo for an easy and practical guide.

I have decided not to make this package available via pip install because there may be some minimal code customization required depending on the model you are using available through Langchain's ChatOpenAI library.

## Contributions 🤝

Feel free to contribute! Whether it's adding features, fixing bugs, adding comments in the code or any suggestions to improve this repo, all are welcomed 😄

## Disclaimer ⚠️

This package is like that friend who shows up to the party early - technically not invited yet, but hopes to bring such good vibes that everyone's glad they came.

## License 📜

MIT License - Because sharing is caring, and we care about you having tool calling RIGHT NOW.

---

Made with ❤️ and a healthy dose of impatience.
