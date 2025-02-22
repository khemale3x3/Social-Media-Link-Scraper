#IG & tiktok only
# import time
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

# # Step 1: Initialize Chrome WebDriver with headless mode
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# # Step 2: Load the Excel file that contains the URLs
# df = pd.read_excel(r"input\TEST UPDATE.xlsx")  # Replace with your actual file path

# # Step 3: Function to extract Instagram and TikTok links only
# def extract_instagram_tiktok_links(url):
#     try:
#         driver.get(url)
#         time.sleep(5)

#         insta_links = []
#         tiktok_links = []

#         links = driver.find_elements(By.TAG_NAME, 'a')  # Find all <a> tags
#         for link in links:
#             href = link.get_attribute('href')
#             if href:
#                 if "instagram.com" in href:
#                     insta_links.append(href)
#                 elif "tiktok.com" in href:
#                     tiktok_links.append(href)

#         return insta_links, tiktok_links
#     except Exception as e:
#         print(f"Error extracting Instagram and TikTok links from {url}: {e}")
#         return [], []

# # Step 4: Loop through each row in the Excel sheet and extract Instagram/TikTok links
# for index, row in df.iterrows():
#     site_url = row['Site URL']
#     print(f"Checking website: {site_url}")

#     # Extract Instagram and TikTok links
#     insta_links, tiktok_links = extract_instagram_tiktok_links(site_url)

#     # Save the extracted links to the DataFrame
#     if insta_links:
#         print(f"Instagram links found: {insta_links}")
#         df.at[index, 'Instagram Links'] = ', '.join(insta_links)
#     else:
#         df.at[index, 'Instagram Links'] = 'No'

#     if tiktok_links:
#         print(f"TikTok links found: {tiktok_links}")
#         df.at[index, 'TikTok Links'] = ', '.join(tiktok_links)
#     else:
#         df.at[index, 'TikTok Links'] = 'No'
        

#     # Add a delay to avoid being detected as a bot
#     time.sleep(2)

# # Step 5: Save the updated DataFrame to a new Excel file
# output_file = r"output\updated_profiles.xlsx"
# df.to_excel(output_file, index=False)
# print(f"Updated Excel saved to {output_file}")

# # Step 6: Close the WebDriver
# driver.quit()

# print("Process completed successfully.")




import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Step 1: Initialize Chrome WebDriver with headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Step 2: Load the Excel file that contains the URLs
df = pd.read_excel(r"input\TEST UPDATE.xlsx")  # Replace with your actual file path

# Step 3: Function to extract Instagram, TikTok, Facebook, and Twitter links only
def extract_social_media_links(url):
    try:
        driver.get(url)
        time.sleep(5)

        insta_links = []
        tiktok_links = []
        facebook_links = []
        twitter_links = []

        links = driver.find_elements(By.TAG_NAME, 'a')  # Find all <a> tags
        for link in links:
            href = link.get_attribute('href')
            if href:
                if "instagram.com" in href:
                    insta_links.append(href)
                elif "tiktok.com" in href:
                    tiktok_links.append(href)
                elif "facebook.com" in href:
                    facebook_links.append(href)
                elif "twitter.com" in href:
                    twitter_links.append(href)

        return insta_links, tiktok_links, facebook_links, twitter_links
    except Exception as e:
        print(f"Error extracting social media links from {url}: {e}")
        return [], [], [], []

# Step 4: Loop through each row in the Excel sheet and extract Instagram, TikTok, Facebook, and Twitter links
for index, row in df.iterrows():
    site_url = row['Site URL']
    print(f"Checking website: {site_url}")

    # Extract social media links (Instagram, TikTok, Facebook, Twitter)
    insta_links, tiktok_links, facebook_links, twitter_links = extract_social_media_links(site_url)

    # Save the extracted links to the DataFrame
    if insta_links:
        print(f"Instagram links found: {insta_links}")
        df.at[index, 'Instagram Links'] = ', '.join(insta_links)
    else:
        df.at[index, 'Instagram Links'] = 'No'

    if tiktok_links:
        print(f"TikTok links found: {tiktok_links}")
        df.at[index, 'TikTok Links'] = ', '.join(tiktok_links)
    else:
        df.at[index, 'TikTok Links'] = 'No'
        
    if facebook_links:
        print(f"Facebook links found: {facebook_links}")
        df.at[index, 'Facebook Links'] = ', '.join(facebook_links)
    else:
        df.at[index, 'Facebook Links'] = 'No'
        
    if twitter_links:
        print(f"Twitter links found: {twitter_links}")
        df.at[index, 'Twitter Links'] = ', '.join(twitter_links)
    else:
        df.at[index, 'Twitter Links'] = 'No'
        
    # Add a delay to avoid being detected as a bot
    time.sleep(2)

# Step 5: Save the updated DataFrame to a new Excel file
output_file = r"output\updated_profiles.xlsx"
df.to_excel(output_file, index=False)
print(f"Updated Excel saved to {output_file}")

# Step 6: Close the WebDriver
driver.quit()

print("Process completed successfully.")
