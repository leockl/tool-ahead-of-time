from setuptools import setup, find_packages

setup(
    name="taot",
    version="0.1.3",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "pydantic>=2.0.0",
        "langchain-core>=0.1.0",
        "langchain-openai>=0.0.5",
        "langgraph>=0.0.1",
    ],
    author="Leo Chow",
    author_email="leo.chow11@gmail.com",
    description="Tool Ahead of Time (TAoT)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/leockl/tool-ahead-of-time",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)