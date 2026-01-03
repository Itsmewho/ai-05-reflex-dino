# ok ok ok this one is harder then it looks and will only have a intermediate.py -> treat it as demigod shit or something.
# Better suited for something like NEAT later down the the line.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

# --- SETUP ---
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--mute-audio")
# This argument sometimes helps with stability
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

print("Opening Game...")
driver.get("https://elgoog.im/dino/")
time.sleep(2)

game_body = driver.find_element("tag name", "body")
print("--- GOD MODE ---")
time.sleep(2)
game_body.send_keys(Keys.SPACE)
try:
    while True:
        try:
            # 1. READ GAME STATE
            state = driver.execute_script(
                """
                const runner = Runner.instance_;
                
                if (runner.crashed || !runner.horizon.obstacles.length) {
                    return null;
                }
                
                const obs1 = runner.horizon.obstacles[0];
                const obs2 = runner.horizon.obstacles[1];
                
                let startX = obs1.xPos;
                let endX = obs1.xPos + obs1.width;
                
                if (obs2) {
                    const gap = obs2.xPos - (obs1.xPos + obs1.width);
                    if (gap < 200) {
                        endX = obs2.xPos + obs2.width;
                    }
                }
                
                return {
                    speed: runner.currentSpeed,
                    dist: startX,
                    width: endX - startX,
                    yPos: obs1.yPos
                };
            """
            )

            if state:
                speed = state["speed"]
                dist = state["dist"]
                width = state["width"]
                y_pos = state["yPos"]

                # --- LOGIC ---
                multiplier = 19
                jump_type = "NORMAL"

                # MEGA detection
                if width > 90:
                    multiplier = 13
                    jump_type = "MEGA"
                elif width > 60:
                    multiplier = 15
                    jump_type = "LONG"

                jump_trigger = speed * multiplier

                if dist < jump_trigger:

                    # --- ACTION DECISION TREE ---

                    if y_pos > 85:
                        # CASE 1: Ground Obstacle (Cactus or Low Bird) -> JUMP
                        if jump_type == "MEGA":
                            print(f"[MEGA JUMP] Width:{width}")
                        game_body.send_keys(Keys.SPACE)

                        # Cooldowns
                        if width > 90:
                            time.sleep(0.15)
                        elif width > 60:
                            time.sleep(0.08)

                    elif y_pos > 45:
                        # CASE 2: Head-Height Bird -> DUCK
                        print(f"[DUCK] Bird at yPos:{y_pos}")

                        # We hold duck for a bit to slide under
                        game_body.send_keys(Keys.DOWN)
                        time.sleep(0.3)

                    else:
                        # CASE 3: High Bird (yPos < 50) -> DO NOTHING
                        # Just walk under it like a boss.
                        pass

        except WebDriverException:
            print("Browser disconnected.")
            break
        except Exception as e:  # noqa: F841
            pass

        time.sleep(0.012)

except KeyboardInterrupt:
    print("\nGame Over.")
    driver.quit()
