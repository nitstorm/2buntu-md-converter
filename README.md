2buntu-md-converter
===================

A Python script to convert HTML and WP Shortcodes into Markdown. Uses [BeautifulSoup 4](https://pypi.python.org/pypi/beautifulsoup4/4.3.2). Written for [2buntu](http://2buntu.com).

## Usage

### Install BeautifulSoup4

**Via `apt-get`**

	$ sudo apt-get install python-bs4

**Via `pip` (or) `easy_install`**

	$ easy_install beautifulsoup4

	$ pip install beautifulsoup4

### Running the script

Import the script into your program and run it as you would do with any other Python file.

The `converter_2buntu` function takes only one input string as an argument and returns the markdown-converted text. 

For an example of what the output of the function might look like, you can run the `example_testing.py` file. The text string inputs provided in the examples are articles from [2buntu](http://2buntu.com) itself. The Licensing they follow can be found on [2buntu](http://2buntu.com).
