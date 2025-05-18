import os
import shutil
from datetime import datetime
from cs50 import get_int, get_string

# Declare directories
SD_CARD = "" # Input your SD card's directory 
PHOTOS_FOLDER = "" # Input your destination folder's directory

# Extract folders
sd_card_content = sorted(os.listdir(SD_CARD))

# Get SD card folders
print("SD card folders: ")
for count, item in enumerate(sd_card_content):
    print(f"{count + 1}) {item}")
choose_folder = get_int("Select folder (number): ")

# User choose folder
while choose_folder < 1 or choose_folder > len(sd_card_content):
    choose_folder = get_int("Select folder (number): ")

os.chdir(f"{SD_CARD}/{sd_card_content[choose_folder - 1]}")

# Filter photos by date
files = os.listdir(os.getcwd())

# Remove ._ files (MacOS thing)
files_to_remove = []
for file in files:
    if file.startswith("._"):
        files_to_remove.append(file)

for file in files_to_remove:
    files.remove(file)

# Output dates and counts
date_files_map = {}

current_date = ""
current_date_photos_count = 0
print()
print(f"Date(Y-M-D){'|':>3} Count")
print("-" * 20)
for file in files:
    file_date = datetime.fromtimestamp(os.path.getmtime(file)).strftime("%Y-%m-%d")
    if file_date not in date_files_map:
        date_files_map[file_date] = [file]
    else:
        date_files_map[file_date].append(file)

for f_date, f in date_files_map.items():
    print(f"{f_date}{'|':>4} {len(f)}")

print()
date_to_transfer = get_string(
    "Which date of photos do you wanna transfer (exact date)? "
)
for file in date_files_map[date_to_transfer]:
    shutil.copy2(file, PHOTOS_FOLDER)
