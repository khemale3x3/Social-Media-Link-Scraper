# Social-Media-Link-Scraper
This script automates the process of extracting Instagram, TikTok, Facebook, and Twitter links from a list of websites using Selenium and Python. It then saves the results in an updated Excel file.

🔹 How the Script Works?

1️⃣ Initialize Chrome WebDriver
Headless Mode: Runs Chrome in the background (without opening a visible browser).
WebDriverManager: Automatically installs the latest version of ChromeDriver.

2️⃣ Load URLs from an Excel File
Reads an Excel file (TEST UPDATE.xlsx) containing website URLs.
Extracts social media links from each website.

3️⃣ Visit Each Website & Extract Links
Opens each website using Selenium.
Finds all anchor (<a>) tags that contain social media links.
Uses href attributes to identify links belonging to Instagram, TikTok, Facebook, and Twitter.

4️⃣ Store Extracted Links in the Excel File
If a social media link is found, it is added to the corresponding column.
If no link is found, "No" is stored in that column.

5️⃣ Save Updated Data to Excel
Saves the extracted social media links in a new Excel file (updated_profiles.xlsx).

6️⃣ Close the WebDriver
Ensures the browser instance is properly closed after execution.

🔹 Why This Approach?
✅ Headless Mode → Faster execution, runs in the background.
✅ Automated WebDriver Setup → No need to manually download ChromeDriver.
✅ Efficient Data Extraction → Uses Selenium to find <a> tags quickly.
✅ Error Handling → Prevents crashes if a website is down or unresponsive.
✅ Excel Output → Organized data storage for easy review.

