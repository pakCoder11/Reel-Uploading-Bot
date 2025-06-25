import time 
import browser_functions 
import bot_functions
from playwright.sync_api import sync_playwright
import pyautogui 
import file_functions
from bs4 import BeautifulSoup
import random


def remove_url_from_file(file_path, url_to_remove):
    """
    Removes all occurrences of a specific URL from a file and rewrites the file with updated content.

    Args:
        file_path (str): Path to the file.
        url_to_remove (str): The URL to remove from the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Remove lines that exactly match the URL (strip whitespace for safety)
    updated_lines = [line for line in lines if line.strip() != url_to_remove]

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)

def auto_share_post(string): 

    # media_path = './Screenshots/Instagram/'
    instagram_media_folder_path = r"C:\Users\Saad Khan\Desktop\Media\Instagram\videos" 

    """
    This function is used to post the content on instagram 
    """

    bot_functions.ClickImageOnScreen('./Screenshots/Instagram/create.png',1)
    time.sleep(1)

    if bot_functions.please_wait_for_n_seconds("./Screenshots/Instagram/post.png",3): 

        bot_functions.ClickImageOnScreen("./Screenshots/Instagram/post.png",1)
        time.sleep(1)

    bot_functions.please_wait('./Screenshots/Instagram/select_from_pc.png')
    bot_functions.ClickImageOnScreen('./Screenshots/Instagram/select_from_pc.png',1)
    time.sleep(1)

    media_filename = file_functions.select_file_from_fileOpener(instagram_media_folder_path)
    time.sleep(1)

    bot_functions.ClickImageOnScreen('./Screenshots/Instagram/next.png',1)
    time.sleep(2)
    bot_functions.ClickImageOnScreen('./Screenshots/Instagram/next.png',1)
    time.sleep(2)

    
    axes = bot_functions.Locate_PNGImageOnScreen('./Screenshots/Instagram/smiley.png')
    pyautogui.click(axes[0],axes[1]-100,clicks=1)

    time.sleep(1)

    # string = generate_insta_post_description()

    pyautogui.write(string)
    time.sleep(2)
    pyautogui.press('space')
    bot_functions.ClickImageOnScreen('./Screenshots/Instagram/share.png',1)
    time.sleep(2)

    status_ = bot_functions.please_wait_for_n_seconds("./Screenshots\Instagram/post_shared_status.PNG",60)

    if status_ == True:

        file_functions.delete_file(instagram_media_folder_path,media_filename)
        pyautogui.press('esc')
        time.sleep(1)

def extract_tweet_text(tweet_url):

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(tweet_url)
        time.sleep(4)

        soup = BeautifulSoup(page.content(), 'html.parser')
        tweet_div = soup.find('div', attrs={'data-testid': 'tweetText'})
        tweet_text = tweet_div.get_text(strip=True) if tweet_div else None

    return tweet_text

def scrap_video_urls(account_url): 
    """
    This function copies the video address from a tweet URL.
    It scrolls the page, extracts video links, removes duplicates and analytics links,
    and saves the result to video_urls.txt.
    """

    all_links = set()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(account_url)
        time.sleep(5)  # Wait for the page to load

        # Scroll down 25 times, extracting links each time
        for _ in range(10):

            # scroll down to load more content
            for _ in range(5):
                page.keyboard.press("PageDown")


            time.sleep(3)
            html_content = page.content()
            soup = BeautifulSoup(html_content, 'html.parser')
            for video in soup.find_all('a'):
                video_src = video.get('href')
                if video_src and 'status' in video_src and '/analytics' not in video_src:
                    video_src = "https://x.com" + video_src
                    all_links.add(video_src)


        browser.close()

    # Write unique, filtered links to file
    with open("video_urls.txt", "w", encoding="utf-8") as f:
        for link in sorted(all_links):
            f.write(link + "\n")

def download_video(tweet_url):
    """
    This function downloads a video from a given tweet URL using x-downloader.com.
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://x-downloader.com/")
        time.sleep(5)  # Wait for 5 seconds

        # Fill the input with id="link"
        page.fill('input#link', tweet_url)

        # Click the "Download Video" button
        page.click('button:has-text("Download Video")')

        time.sleep(5)  # Wait for 5 seconds

        # Wait for the "Download MP4" button to appear and click it, while capturing the download
        try:
            page.wait_for_selector('a:has-text("Download MP4")', timeout=5000)

            with page.expect_download() as download_info:
                page.click('a:has-text("Download MP4")')  # This must trigger a file download
            download = download_info.value 

            # print("Download is ... ", download)

            # Save the file with a proper name and .mp4 extension
            # download.save_as("downloaded_video.mp4") 
            download.save_as(r"C:\Users\Saad Khan\Desktop\Media\Instagram\videos\downloaded_video.mp4")
            print("Video saved as downloaded_video.mp4")

        except Exception as e:
            print("Download MP4 button not found or download failed:", e)

        browser.close()

# download_video("https://x.com/i/status/1937395551420449105") 

# copy_video_urls("https://x.com/x_viral_vibes") 



def get_random_url_from_file(file_path):
    """
    Selects a random non-empty line (URL) from the given file, strips it, and returns it as a string.
    
    Args:
        file_path (str): Path to the file containing URLs.
    Returns:
        str: A randomly selected URL string, stripped of whitespace, or None if no valid URLs found.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        urls = [line.strip() for line in file if line.strip()]
    if not urls:
        return None
    return random.choice(urls)

if __name__ == "__main__": 

    print("Instagram Auto REEL Uploading Bot is running...")
    
    print("Please make sure you are logged in to Instagram in Chrome before running this bot.")

    time.sleep(3) 


    random_url = get_random_url_from_file("video_urls.txt") 

    # If no URL found, scrape new URLs and try again
    if not random_url:
        print("No URLs found in file. Scraping new video URLs...")
        scrap_video_urls("https://x.com/x_viral_vibes")  # <-- Replace with your desired account URL
        random_url = get_random_url_from_file("video_urls.txt")

    print(f"Randomly selected URL: {random_url}")

    if random_url:
        tweet_text = extract_tweet_text(random_url) 

        download_video(random_url)

        print(f"Extracted tweet text: {tweet_text}")

    browser_functions.open_chrome()
    time.sleep(4) 
    bot_functions.redirect_url("https://www.instagram.com/")
    time.sleep(4)

    # Example of posting to Instagram 

    string = f"{tweet_text} \n\n#viral #trending #reels #usa #viralvideo #viralreels #reelsinstagram #reelsviral #reelsusa #reelsvideo #pakistan #usa #reelsusa #reelsviralvideo #reelsviralusa #news #data #ai #science \n \n Follow us @infohub_69"

    auto_share_post(string)
    remove_url_from_file("video_urls.txt", random_url) 

    browser_functions.close_browser()

