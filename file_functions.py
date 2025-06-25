import bot_functions 
import pyautogui 
import time 
import os
import random
import json_loader

def delete_url_from_file(target_url):

    """
    Deletes a specific URL from a text file and removes duplicate URLs.

    Args:
        file_path (str): Path to the text file containing URLs.
        target_url (str): The URL to be removed.

    Returns:
        None
    """

    file_path = json_loader.read_variable("instagram_profiles_file")

    try:


        # Read all URLs from the file
        with open(file_path, 'r') as file:
            urls = file.readlines()

        # Remove the target URL
        urls = [url.strip() for url in urls if url.strip() != target_url]

        # Remove duplicate URLs
        unique_urls = list(set(urls))

        # Write the cleaned URLs back to the file
        with open(file_path, 'w') as file:
            for url in unique_urls:
                file.write(url + '\n')

        print(f"URL '{target_url}' removed and duplicates cleaned from {file_path}.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Please provide a valid file path.")

def get_random_filename(folder_path):
    try:
        # Get a list of all files in the specified folder
        files = os.listdir(folder_path)

        # Filter out directories (if any)
        files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

        # Choose a random filename from the list
        if files:
            random_filename = random.choice(files)
            return random_filename
        else:
            return "No files found in the folder."

    except FileNotFoundError:
        return "Folder not found. Please provide a valid folder path."

def select_file_from_fileOpener(destination_folder_path): 

    """
    This function is used to select the files from the file opener ... 
    """
    media_filename = get_random_filename(destination_folder_path)

    # Step 1 Clean Folder Path 

    bot_functions.please_wait('./Screenshots/FileOpener/file_1.png')

    image_axes = bot_functions.Locate_PNGImageOnScreen('./Screenshots/FileOpener/file_1.png')
    pyautogui.click(image_axes[0]-40,image_axes[1]+4,clicks=1)
    time.sleep(1)
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('backspace') 
    time.sleep(1)

    # Step 2 Enter Folder name  

    pyautogui.write(destination_folder_path)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)

    # Step 3 Enter FileName 
    image_axes = bot_functions.Locate_PNGImageOnScreen('./Screenshots/FileOpener/filebox.png')
    pyautogui.click(image_axes[0]+50,image_axes[1]+5,clicks=1)
    time.sleep(1)

    pyautogui.write(media_filename)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)

    

    return media_filename

def create_hashtags_list(file_path):
    # Read hashtags from the text file (assuming one hashtag per line)
    with open(file_path, "r") as file:
        all_hashtags = [line.strip() for line in file]

    # Predefined list of additional hashtags
    additional_hashtags = [
        '#fyp', '#foryou', '#trending', '#tiktok', '#usa', '#uk', '#germany', '#trump','#motivation',
    ]

    # Randomly select hashtags from the file
    num_random_hashtags = min(len(all_hashtags), 5)  # You can adjust the number
    random_selected_hashtags = random.sample(all_hashtags, num_random_hashtags)

    # Combine the two lists
    final_hashtags = random_selected_hashtags + additional_hashtags
    return final_hashtags


def get_random_comment(file_path):

    # file_path = r"D:\Software Dev Workplace\Affiliate Marketing Bot Project\text-data\comments.txt"

    try:
        # Read all lines from the file into a list
        with open(file_path, "r", encoding='utf-8') as file:
            comments_list = file.readlines()

        # Remove any leading/trailing whitespace from each comment
        comments_list = [comment.strip() for comment in comments_list]

        # Choose a random comment from the list
        if comments_list:
            random_comment = random.choice(comments_list)
            return random_comment
        else:
            return "No comments found in the file."

    except FileNotFoundError:
        return "The file 'comments.txt' does not exist."

def get_random_sentence_from_dataset(file_path):

    """
    this function is for to access the random piece of data from a dataset.txt file ...
    """
    try:
        # Read all lines from the file into a list
        with open(file_path, "r",encoding='utf-8') as file:
            comments_list = file.readlines()

        # Remove any leading/trailing whitespace from each comment
        comments_list = [comment.strip() for comment in comments_list]

        # Choose a random comment from the list
        if comments_list:
            random_comment = random.choice(comments_list)
            return random_comment
        else:
            return "No comments found in the file."

    except FileNotFoundError:
        return "The file does not exist."


def delete_file(folder_path, filename):

    """
    Deletes a file permanently from the specified folder.

    Args:
        folder_path (str): Path to the folder containing the file.
        filename (str): Name of the file to be deleted.

    Returns:
        bool: True if the file was successfully deleted, False otherwise.
    """
    try:
        file_path = os.path.join(folder_path, filename)
        os.remove(file_path)
        print(f"File '{filename}' deleted successfully.")
        return True
    except FileNotFoundError:
        print(f"File '{filename}' not found in the specified folder.")
        return False
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")
        return False

def compose_message():

    """
    This function is used to compose the message ... it reads the message from the file . 
    """

    health_care_description = json_loader.read_variable("health_care_description_file")

    sentence = get_random_sentence_from_dataset(health_care_description)

    string = f"** DENTAL CARE TIP OF THE DAY ** \n \n{sentence}\n \nIf you want healthy Teeths & Gums Use Pro-Dentim (LINK IN BIO) "

    return string


# ---------------------
# DELETE FILE 
# ---------------------
# # Example usage
# folder_path = r"C:\Users\YourUsername\Desktop\instagram]reels"
# filename_to_delete = "example.txt"  # Replace with the actual filename
# result = delete_file(folder_path, filename_to_delete)
# print(result)


# # Example usage
# folder_path = r"C:\Users\Saad Khan\Desktop\Media\Instagram\media-dataset"
# random_file = get_random_filename(folder_path)
# print(f"Random filename: {random_file}")

# print("starts/_")
# time.sleep(5)
# s = compose_message()
# print(s)

# destination_folder_path = r"C:\Users\Saad Khan\Desktop\Media\Instagram\media-dataset" 
# select_file_from_fileOpener(destination_folder_path)

# file_path = r"D:\Software Dev Workplace\Affiliate Marketing Bot Project\text-data\tiktok_video_comments.txt"
# rand = get_random_comment(file_path)
# print(rand)

# rand_comment = get_random_comment()
# print(rand_comment)

# delete_url_from_file("https://www.instagram.com/amberheard/")
