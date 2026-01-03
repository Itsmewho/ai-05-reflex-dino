from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


# --- Config
GAME_URL = "https://elgoog.im/dino/"
print("--- DINO BOT V1: LAUNCHER ---")

# 1. setup Chrome driver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# Mute the audio. Trust me its better this way,.
options.add_argument("--mute-audio")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)


# 2 Open the game:
print(f"Open the game {GAME_URL}")
driver.get(GAME_URL)

# 3 Give it some time:
print("Starting in 3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")


# 4 Press SPACE to start the game
body = driver.find_element("tag name", "body")
body.send_keys(Keys.SPACE)

print("Game Started! Press Ctrl+C in terminal to stop.")

# Keep browser open
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nClosing...")
    driver.quit()
