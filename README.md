
# Instagram Reels Auto Poster Bot

## 📌 Project Description

This project is a fully automated bot designed to **download videos from Twitter/X** and **post them as Instagram Reels**—without any user interaction.

The bot performs the following steps:

1. **Reads video URLs** from a `videos_urls.txt` file.
2. **Downloads the video** using [Playwright](https://playwright.dev/) from a specified website.
3. **Reads captions** from a `captions.txt` file.
4. **Scrapes tweet text** from the original X post and uses it to form or enrich the caption.
5. **Posts the video as a reel** on Instagram, automatically.

You can run this bot on a **local machine or a server**, making it ideal for scheduled automation or batch processing.


## ⚙️ Requirements

* Python 3.8 or higher
* Google Chrome browser installed
* Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## ✅ Pros

* 🔁 Unlimited automation for Instagram Reels posting
* ⏱️ Saves time by handling video downloading and posting automatically
* 💻 Can run on any compatible local or cloud server with minimal configuration

---

## ⚠️ Cons

* 🛠️ Requires initial setup and configuration
* 📥 Dependent on valid video URLs and captions availability

---

## 🚧 Project Status

> This project is **currently in development** and may contain bugs or incomplete features.
> **Contributions, feedback, and issue reports are welcome!**

Feel free to fork the repo and open a pull request to improve or add features.

---
