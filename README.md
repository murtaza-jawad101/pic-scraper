# Rolex Watch Image Scraper

This repository contains a Python script that uses Selenium and BeautifulSoup to scrape images of Rolex watches from their official website. The script opens each URL, extracts image URLs using BeautifulSoup, and then downloads and saves the images locally.

## Prerequisites

- Python 3.x
- Install the required packages by running:
  ```
  pip install beautifulsoup4 selenium pandas requests webdriver_manager Pillow
  ```

## Installation

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/murtaza-jawad101/pic-scraper.git
   ```

2. Navigate to the project directory:

   ```
   cd pic-scraper
   ```

3. Install the Chrome WebDriver using the `webdriver_manager`:
   ```
   pip install webdriver_manager
   ```

## Usage

1. Place your CSV file named `crownProds.csv` in the same directory as the script `crownScraper.py`.

2. Open the script file `crownScraper.py` and adjust any necessary settings or parameters if needed.

3. Run the script using the following command:

   ```
   python crownScraper.py
   ```

   The script will start processing the URLs from the CSV file and download the Rolex watch images to the current directory.

## Configuration

You can modify the following parameters in the script to customize its behavior:

- `options.add_argument('--headless')`: Enables headless mode for the Chrome WebDriver. If you want to see the browser in action, you can remove this line.

- `time.sleep(5)`: Adjust the sleep time as needed to ensure the page loads properly before extracting data.

- `i=1`: Use this variable to keep track of the loop iteration for debugging purposes.

- You can customize the column names used to access URLs and image names from the CSV file if your CSV structure is different.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Make sure to check if your CSV file is correctly formatted and includes the necessary Rolex watch URLs. Replace the existing contents of the `README.md` file in your repository with the text above. If you want to keep the current content of your `README.md` file, you can append the customized section to it.

Feel free to reach out if you have any more questions or need further assistance!
