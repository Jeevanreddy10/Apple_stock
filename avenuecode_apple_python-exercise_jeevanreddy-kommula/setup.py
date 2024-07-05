from setuptools import setup, find_packages

setup(
    name="avenuecode_apple_python-exercise_jeevanreddy-kommula",
    version="1.0.0",
    author="jeevanreddy kommula",
    author_email="jeevanreddykommula99@gmail.com",
    description="A package for analyzing Apple stock data",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your-repo",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pandas",
        "numpy",
        "plotly",
        "python-dateutil",
        "pytz",
        "six",
        "tenacity",
        "tzdata"
    ],
)

