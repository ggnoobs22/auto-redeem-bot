import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
    "INPUT_1": os.getenv("PRIVATE_KEY"),
    "INPUT_2": os.getenv("RPC_URL"),
    "INPUT_3": os.getenv("CONTRACT_ADDRESS"),
    "INPUT_4": os.getenv("TOKEN_ADDRESS"),
    "INPUT_5": os.getenv("CHECK_INTERVAL", "1"),
}

def run_redeem_bot():
    TARGET_URL = "https://onesavielabs.github.io/auto-redeem/"
    
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--log-level=3") 

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        print(f"正在前往: {TARGET_URL}")
        driver.get(TARGET_URL)
        time.sleep(3)

        print("正在尋找輸入框...")
        inputs = driver.find_elements(By.TAG_NAME, "input")
        text_inputs = [
            i for i in inputs 
            if i.get_attribute('type') in ['text', 'password', 'email', 'number', 'search', 'url', 'tel'] 
            and i.is_displayed()
        ]

        if len(text_inputs) >= 5:
            text_inputs[0].clear()
            text_inputs[0].send_keys(CONFIG["INPUT_1"])
            text_inputs[1].clear()
            text_inputs[1].send_keys(CONFIG["INPUT_2"])
            text_inputs[2].clear()
            text_inputs[2].send_keys(CONFIG["INPUT_3"])
            text_inputs[3].clear()
            text_inputs[3].send_keys(CONFIG["INPUT_4"])
            text_inputs[4].clear()
            text_inputs[4].send_keys(CONFIG["INPUT_5"]) 
            print("填寫完成！")
        else:
            print(f"警告：網頁上只找到 {len(text_inputs)} 個輸入框，少於預期的 5 個。")

        time.sleep(1) 
        print("正在嘗試打勾...")
        try:
            label_text = driver.find_element(By.XPATH, "//*[contains(text(), 'I understand')]")
            driver.execute_script("arguments[0].scrollIntoView();", label_text)
            time.sleep(0.5)
            label_text.click()
            print("已點擊文字標籤。")
        except Exception:
            try:
                checkbox_btn = driver.find_element(By.CSS_SELECTOR, "button[role='checkbox']")
                driver.execute_script("arguments[0].click();", checkbox_btn)
                print("已點擊 checkbox 按鈕。")
            except:
                pass

        time.sleep(1)
        print("正在按下 Save...")
        try:
            save_btn = driver.find_element(By.XPATH, "//*[contains(text(), 'Save Configuration')]")
            driver.execute_script("arguments[0].scrollIntoView();", save_btn)
            if save_btn.is_enabled():
                save_btn.click()
            else:
                driver.execute_script("arguments[0].click();", save_btn)
            print("已按下 Save Configuration。")
        except Exception as e:
            print(f"按下 Save 時發生錯誤: {e}")

        print("等待頁面切換，準備按下 Start...")
        time.sleep(3)
        
        try:
            start_btn = driver.find_element(By.XPATH, "//*[contains(text(), 'Start') and contains(text(), 'Redeem')]")
            driver.execute_script("arguments[0].scrollIntoView();", start_btn)
            start_btn.click()
            print("🎉 成功！已按下 Start Auto Redeem。")
        except Exception:
            try:
                start_btn_backup = driver.find_element(By.XPATH, "//*[contains(text(), 'Start')]")
                start_btn_backup.click()
                print("🎉 (備用方案) 已按下 Start 按鈕。")
            except:
                print("⚠️ 找不到 Start 按鈕，請手動確認。")

    except Exception as e:
        print(f"發生錯誤: {e}")

    finally:
        print("\n" + "="*30)
        print("程式執行完畢，視窗將保持開啟。")

if __name__ == "__main__":
    run_redeem_bot()
