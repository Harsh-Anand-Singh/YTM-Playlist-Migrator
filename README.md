# YTM Playlist Migrator 🎶

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/6/6a/Youtube_Music_icon.svg" alt="YouTube Music Logo" width="120"/>
</p>

<p align="center">
  <strong>A universal Python script to effortlessly migrate your music library from any source (offline files, other streaming services) to YouTube Music by automatically liking your entire playlist.</strong>
  <br/><br/>
  <a href="https://github.com/Harsh-Anand-Singh/YTM-Playlist-Migrator"><img src="https://img.shields.io/github/stars/Harsh-Anand-Singh/YTM-Playlist-Migrator?style=social" alt="GitHub Stars"></a>
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</p>

---

## The Problem: The Walled Gardens of Music

Switching music streaming services or moving from a local library to the cloud is a universal pain point for music lovers. Playlists and "liked" songs—collections curated over years—are often trapped in digital silos. Manually rebuilding these libraries on a new platform like YouTube Music involves hundreds, if not thousands, of tedious searches and clicks.

## The Solution: A Universal Music Bridge

**YTM Playlist Migrator** was built to solve this problem. It acts as a universal bridge, allowing you to "port" your music library to YouTube Music with a single command. 

This project uses a clever, modern workflow: instead of complex setup scripts, we leverage AI assistants like **Google Gemini** to handle the data preparation, making the entire process faster and more accessible.

This project began as a personal tool to migrate my own offline collection from a Samsung music app, but it is designed to be a flexible solution for anyone facing a similar migration challenge.

## How It Works: The 3-Step Process

This entire process is designed to be quick and easy, using AI to do the heavy lifting.

### Step 1: Get Your Song List with AI

First, you need a list of your songs. The easiest way is to use an AI assistant.

1.  Take screenshots of your playlist or liked songs from your old music app (e.g., Spotify, Apple Music, an offline player).
2.  Upload these images to an AI assistant like **Google Gemini**.
3.  Use a prompt like: *"Identify all the songs and artists from these screenshots. If any are unclear, ask me. At the end, create a Python list of dictionaries with "Song Name" and "Artist(s)" keys for each song."*
4.  The AI will process the images and give you a perfectly formatted Python list.

### Step 2: Get Your Authentication File (`oauth.json`)

Next, we need to authorize the script to access your YouTube Music account.

1.  In your browser (Chrome, Brave, etc.), go to [music.youtube.com](https://music.youtube.com).
2.  Open **Developer Tools** (`Ctrl+Shift+I` on Windows, `Cmd+Option+I` on Mac).
3.  Go to the **Network** tab and select the **Fetch/XHR** filter.
4.  Refresh the page. A list of requests will appear. Click on a request named `browse` or `next`.
5.  In the panel that appears, go to the **Headers** tab and scroll down to the **Request Headers** section.
6.  Copy the **entire block** of text (from `accept: */*` all the way to the end).
7.  Paste this block of text into an AI assistant like **Google Gemini** and use the prompt: *"Create a valid JSON file from the following request headers. The JSON object should contain only two keys: "cookie" and "x-goog-authuser", with their corresponding values from the text I provided."*
8.  The AI will give you a clean JSON output. Create a new file named `oauth.json` in the project folder and paste this JSON content into it.

### Step 3: Run the Script

1.  Clone this repository and navigate into the project folder.
2.  Install the required library:
    ```bash
    pip install ytmusicapi
    ```
3.  Open the `like_songs.py` file.
4.  Replace the example `songs_list` with the list you generated in Step 1.
5.  Run the script from your terminal:
    ```bash
    python like_songs.py
    ```

That's it! The script will now iterate through your list, search for each song, and "like" it on YouTube Music.

## Troubleshooting ⚠️

**`YTMusicUserError: Missing ... cookie, x-goog-authuser`**
-   This error is almost always caused by an **ad-blocker** or **privacy shield** (like Brave Shields).
-   **Solution:** Temporarily disable your ad-blocker for the YouTube Music site when you are copying the headers, then refresh the page.


## License 📜

Distributed under the MIT License (I don't know but everyone wrties it and was given in gemini from where I got this long readme). See `LICENSE` for more information.

---
<p align="center">
  Built to tear down the walled gardens of music streaming. I hope it helps you too!
</p>
