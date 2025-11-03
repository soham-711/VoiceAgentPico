# # # image_engine.py
# # import requests
# # import os
# # import re
# # import json
# # import webbrowser
# # from difflib import get_close_matches

# # SAVE_PATH = "generated_images"
# # INDEX_FILE = "image_index.json"

# # # make sure folder exists
# # os.makedirs(SAVE_PATH, exist_ok=True)

# # # load index if exists
# # if os.path.exists(INDEX_FILE):
# #     with open(INDEX_FILE, "r", encoding="utf-8") as f:
# #         INDEX = json.load(f)
# # else:
# #     INDEX = {}

# # def _sanitize_filename(text: str) -> str:
# #     return re.sub(r'[^a-zA-Z0-9_-]', '_', text.lower())

# # def _save_index():
# #     with open(INDEX_FILE, "w", encoding="utf-8") as f:
# #         json.dump(INDEX, f, indent=4)

# # def generate_image(topic: str, size: str = "medium") -> str:
# #     """
# #     Generate an image from Pollinations API and save it locally.
# #     """
# #     url = f"https://image.pollinations.ai/prompt/{topic.replace(' ', '%20')}"
# #     response = requests.get(url)

# #     if response.status_code == 200:
# #         file_name = f"{_sanitize_filename(topic)[:50]}{size}.png"
# #         file_path = os.path.join(SAVE_PATH, file_name)

# #         with open(file_path, "wb") as f:
# #             f.write(response.content)

# #         # update index
# #         INDEX[topic] = file_path
# #         _save_index()

# #         return file_path
# #     else:
# #         return "⚠ Failed to generate image."

# # def find_image(query: str) -> str:
# #     """
# #     Find closest matching image for a query using fuzzy search.
# #     If found, open it in the default image viewer and return path.
# #     """
# #     if not INDEX:
# #         return "⚠ No images stored yet."

# #     topics = list(INDEX.keys())
# #     matches = get_close_matches(query, topics, n=1, cutoff=0.4)
# #     if matches:
# #         best_topic = matches[0]
# #         file_path = INDEX[best_topic]

# #         # Open the image in the default viewer (works on Windows/Mac/Linux)
# #         if os.name == "nt":  # Windows
# #             os.startfile(file_path)
# #         elif os.name == "posix":  # Mac/Linux
# #             try:
# #                 # macOS
# #                 os.system(f"open '{file_path}'")
# #             except:
# #                 # Linux
# #                 os.system(f"xdg-open '{file_path}'")
# #         else:
# #             # fallback: open in browser
# #             webbrowser.open(f"file://{os.path.abspath(file_path)}")

# #         return file_path

# #     return "⚠ No matching image found."



# # image_engine.py
# import requests
# import os
# import re
# import json
# import webbrowser
# from difflib import get_close_matches

# SAVE_PATH = "generated_images"
# INDEX_FILE = "image_index.json"

# # make sure folder exists
# os.makedirs(SAVE_PATH, exist_ok=True)

# # load index if exists
# if os.path.exists(INDEX_FILE):
#     with open(INDEX_FILE, "r", encoding="utf-8") as f:
#         INDEX = json.load(f)
# else:
#     INDEX = {}

# def _sanitize_filename(text: str) -> str:
#     return re.sub(r'[^a-zA-Z0-9_-]', '_', text.lower())

# def _save_index():
#     with open(INDEX_FILE, "w", encoding="utf-8") as f:
#         json.dump(INDEX, f, indent=4)

# def generate_image(topic: str, size: str = "medium") -> str:
#     """
#     Generate an image from Pollinations API and save it locally.
#     """
#     url = f"https://image.pollinations.ai/prompt/{topic.replace(' ', '%20')}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         file_name = f"{_sanitize_filename(topic)[:50]}{size}.png"
#         file_path = os.path.join(SAVE_PATH, file_name)

#         with open(file_path, "wb") as f:
#             f.write(response.content)

#         # update index
#         INDEX[topic] = file_path
#         _save_index()

#         return file_path
#     else:
#         return "⚠ Failed to generate image."

# # def find_image(query: str) -> str:

#     # """
#     # Find closest matching image for a query using fuzzy search.
#     # If found, open it in the default image viewer and return path.
#     # """
#     # if not INDEX:
#     #     return "⚠ No images stored yet."
    


#     # if query.strip() == "":
#     #     latest_topic = list(INDEX.keys())[-1]
#     #     file_path = INDEX[latest_topic]



#     # topics = list(INDEX.keys())
#     # matches = get_close_matches(query, topics, n=1, cutoff=0.4)
#     # if matches:
#     #     best_topic = matches[0]
#     #     file_path = INDEX[best_topic]

#     #     # Open the image in the default viewer (works on Windows/Mac/Linux)
#     #     if os.name == "nt":  # Windows
#     #         os.startfile(file_path)
#     #     elif os.name == "posix":  # Mac/Linux
#     #         try:
#     #             # macOS
#     #             os.system(f"open '{file_path}'")
#     #         except:
#     #             # Linux
#     #             os.system(f"xdg-open '{file_path}'")
#     #     else:
#     #         # fallback: open in browser
#     #         webbrowser.open(f"file://{os.path.abspath(file_path)}")

#     #     return file_path

#     # return "⚠ No matching image found."


# def find_image(query: str) -> str:
#     """
#     Find the closest matching image for a query using fuzzy search.
#     If found, open it in the default image viewer and return the file path.
#     """
#     if not INDEX:
#         return "⚠ No images stored yet."

#     # If no query is provided, return the latest image
#     if query.strip() == "":
#         latest_topic = list(INDEX.keys())[-1]
#         file_path = INDEX[latest_topic]

#     else:
#         topics = list(INDEX.keys())
#         matches = get_close_matches(query, topics, n=1, cutoff=0.4)

#         if matches:
#             best_topic = matches[0]
#             file_path = INDEX[best_topic]
#         else:
#             return "⚠ No matching image found."

#     # Open the image in default viewer
#     if os.name == "nt":  # Windows
#         os.startfile(file_path)
#     elif os.name == "posix":  # macOS/Linux
#         try:
#             # macOS
#             os.system(f"open '{file_path}'")
#         except Exception:
#             # Linux
#             os.system(f"xdg-open '{file_path}'")
#     else:
#         # Fallback: open in browser
#         webbrowser.open(f"file://{os.path.abspath(file_path)}")

#     return file_path
import requests
import os
import re
import webbrowser

SAVE_PATH = "generated_images"

# make sure folder exists
os.makedirs(SAVE_PATH, exist_ok=True)

def _sanitize_filename(text: str) -> str:
    return re.sub(r'[^a-zA-Z0-9_-]', '_', text.lower())

def generate_image(topic: str, size: str = "medium") -> str:
    """
    Generate an image from Pollinations API and save it locally.
    """
    url = f"https://image.pollinations.ai/prompt/{topic.replace(' ', '%20')}"
    response = requests.get(url)

    if response.status_code == 200:
        file_name = f"{_sanitize_filename(topic)[:50]}{size}.png"
        file_path = os.path.join(SAVE_PATH, file_name)

        with open(file_path, "wb") as f:
            f.write(response.content)

        return "I successfully generate image sir"
    else:
        return "⚠ Failed to generate image."

def find_image() -> str:
    """
    Show the latest generated image from the folder.
    """
    files = [os.path.join(SAVE_PATH, f) for f in os.listdir(SAVE_PATH) if f.endswith(".png")]
    if not files:
        return "⚠ No images found."

    # get the latest file by modification time
    latest_file = max(files, key=os.path.getmtime)

    # Open the image in default viewer
    if os.name == "nt":  # Windows
        os.startfile(latest_file)
    elif os.name == "posix":  # macOS/Linux
        try:
            # macOS
            os.system(f"open '{latest_file}'")
        except Exception:
            # Linux
            os.system(f"xdg-open '{latest_file}'")
    else:
        webbrowser.open(f"file://{os.path.abspath(latest_file)}")

    return latest_file