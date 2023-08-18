# Web Scraping ReadMe

This repository contains a Python script for web scraping content from the [CodeSpace Academy](https://www.codespace.co.za/) LMS and saving it to a Word document using the requests, BeautifulSoup, and docx libraries. The script allows you to extract content from web pages and compile it into a single Word document.

## Purpose

The aim is to extract content from the CodeSpace Academy LMS in order to generate a comprehensive document. This document will undergo quality assurance and editing before being restructured and integrated back into the backend system. This approach streamlines the overall process.

## Requirements
#### Before running the script, make sure you have the following requirements installed:

<ul>
<li> Python 3.x: The programming language used to run the script.</li>
<li>Selenium library: Used for automating interactions with the website.</li>
<li>requests library: Used to make HTTP requests to the specified URLs.</li>
<li>BeautifulSoup library: Used for parsing HTML content and extracting text.</li>
<li>docx library: Used for creating and manipulating Word documents.</li>
<li>Flask library: Used for creating a local web server.</li>
<li>contextlib library: Used for managing the WebDriver context.</li>
</u>

## Dependencies
#### The following Python libraries are used in the script and should be installed via pip:


### bash
Copy code
pip install requests
pip install beautifulsoup4
pip install python-docx
pip install urljoin
pip install docx
pip install pandas
pip install Flask
pip install contextlib2


## Usage

Clone the repository or download the script to your local machine.
Install the required dependencies as mentioned above.
Open the script in a code editor or IDE of your choice.
Replace the dropdown_urls list with the URLs you want to scrape. Add or remove URLs as needed.

python
Copy code
dropdown_urls = [
    "https://learn.codespace.co.za/courses/144",
    "https://learn.codespace.co.za/courses/142",
    "https://learn.codespace.co.za/courses/147",
    # Add more URLs as needed
]

#### Run the script using the following command:
bash
Copy code
python web_scraping_script.py
The script will scrape the content from each URL, create a Word document, and save the scraped content to the document.

The resulting Word document, named "scraped_content.docx", will be saved in the same directory where the script is located.

## Notes
Please ensure that you have the necessary permissions to scrape and use content from the CodeSpace Academy website in compliance with their terms of use and legal guidelines.


