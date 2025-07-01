import asyncio
from pyppeteer import launch

async def automate_opengraph_sui():
    browser = await launch(headless=False, args=['--start-maximized'])
    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})

    # 1. Go to faucet.sui.io and request faucet tokens
    print("Opening faucet.sui.io...")
    await page.goto('https://faucet.sui.io/', {'waitUntil': 'networkidle2'})

    # Assuming faucet page has a button to request tokens for connected wallet
    try:
        faucet_button_selector = 'button#request-tokens'  # Update with actual selector
        await page.waitForSelector(faucet_button_selector, timeout=10000)
        await page.click(faucet_button_selector)
        print("Clicked faucet request button")
        await asyncio.sleep(10)  # Wait for faucet processing
    except Exception as e:
        print(f"Faucet interaction error or already claimed: {e}")

    # 2. Go to OpenGraph challenges page
    print("Navigating to OpenGraph challenges...")
    await page.goto('https://explorer.opengraphlabs.xyz/challenges', {'waitUntil': 'networkidle2'})

    # 3. Connect new wallet (Slush Wallet)
    try:
        connect_wallet_selector = 'button.connect-wallet'  # Update selector
        await page.waitForSelector(connect_wallet_selector, timeout=15000)
        await page.click(connect_wallet_selector)
        print("Clicked connect wallet button")
        print("Please approve wallet connection manually in Slush Wallet popup.")
        await asyncio.sleep(30)  # Time for manual wallet approval
    except Exception as e:
        print(f"Wallet connection error or already connected: {e}")

    # 4. Complete Step 1 - Sea Animal Classification
    try:
        step1_selector = 'a[href*="sea-animal-classification"]'  # Update selector
        await page.waitForSelector(step1_selector, timeout=10000)
        await page.click(step1_selector)
        print("Started Step 1 - Sea Animal Classification")
        # Add automation for this step if possible (e.g., clicking answers)
        await asyncio.sleep(15)  # Wait or automate answers here
        # Navigate back to challenges page
        await page.goto('https://explorer.opengraphlabs.xyz/challenges', {'waitUntil': 'networkidle2'})
    except Exception as e:
        print(f"Step 1 error: {e}")

    # 5. Complete Step 2 - Urban Traffic Dataset
    try:
        step2_selector = 'a[href*="urban-traffic-dataset"]'  # Update selector
        await page.waitForSelector(step2_selector, timeout=10000)
        await page.click(step2_selector)
        print("Started Step 2 - Urban Traffic Dataset")
        # Add automation for this step if possible
        await asyncio.sleep(15)  # Wait or automate answers here
    except Exception as e:
        print(f"Step 2 error: {e}")

    # Final screenshot for verification
    await page.screenshot({'path': 'opengraph_sui_automation.png'})
    print("Automation complete. Screenshot saved.")

    await browser.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(automate_opengraph_sui())
