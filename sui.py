import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def safe_click(driver, selector, by=By.CSS_SELECTOR, retries=3, wait_timeout=10):
    """Click a button safely with retries."""
    for attempt in range(retries):
        try:
            print(f"Waiting for selector: {selector}")
            element = WebDriverWait(driver, wait_timeout).until(
                EC.element_to_be_clickable((by, selector))
            )
            element.click()
            print(f"Successfully clicked: {selector}")
            return True
        except Exception as e:
            print(f"Attempt {attempt+1} failed for {selector}: {str(e)}")
            time.sleep(2)
    print(f"Failed to click {selector} after {retries} attempts")
    return False

def automate_opengraph_sui():
    driver = None
    try:
        # Initialize Chrome with options to avoid detection
        print("Opening browser...")
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--start-maximized')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')

        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(30)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        # 1. Go to faucet (optional)
        print("Opening faucet.sui.io...")
        try:
            driver.get('https://faucet.sui.io/')
            print("Successfully loaded faucet.sui.io")
            time.sleep(5)
        except Exception as e:
            print(f"Warning: Could not load faucet.sui.io - {str(e)}")

        # 2. Go to OpenGraph challenges page
        print("Navigating to OpenGraph challenges...")
        challenge_url = 'https://explorer.opengraphlabs.xyz/challenges'
        try:
            driver.get(challenge_url)
            print(f"Successfully loaded: {challenge_url}")
            time.sleep(5)
        except TimeoutException:
            print(f"Timeout loading {challenge_url}")
        except Exception as e:
            print(f"Error loading {challenge_url}: {str(e)}")

        # Take screenshot for debugging
        try:
            driver.save_screenshot('debug_page.png')
            print("Debug screenshot saved. Check debug_page.png to find correct selectors.")
        except Exception as e:
            print(f"Could not save screenshot: {e}")

        # Keep browser open for manual inspection
        input("Press Enter after manual navigation/inspection...")

    except KeyboardInterrupt:
        print("\nScript interrupted by user")
    except Exception as e:
        print(f"Fatal error: {str(e)}")
    finally:
        if driver:
            try:
                driver.quit()
                print("Browser closed successfully")
            except:
                pass

if __name__ == '__main__':
    automate_opengraph_sui()
