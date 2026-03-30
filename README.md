# auto-redeem-bot

自動填入並執行 [Auto Redeem](https://onesavielabs.github.io/auto-redeem/) 網頁的 Python 腳本，透過 macOS 捷徑（Shortcuts）一鍵啟動。

## 環境需求

- macOS
- Python 3
- Google Chrome
- 已建立 Python 虛擬環境（.venv）

## 安裝步驟

**1. Clone 專案**
```bash
git clone https://github.com/ggnoobs22/auto-redeem-bot.git
cd auto-redeem-bot
```

**2. 建立虛擬環境並安裝套件**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install selenium webdriver-manager python-dotenv
```

**3. 建立 .env 檔案**
```bash
cp .env.example .env
nano .env
```

填入以下內容：
```
PRIVATE_KEY=你的私鑰
RPC_URL=https://arb1.arbitrum.io/rpc
CONTRACT_ADDRESS=合約地址
TOKEN_ADDRESS=代幣地址
CHECK_INTERVAL=1
```

**4. 執行**
```bash
source .venv/bin/activate
python auto_redeem.py
```

## macOS 捷徑設定

在捷徑 app 新增「執行 Shell 工序指令」：
```bash
cd ~/web_auto
source .venv/bin/activate
python auto_redeem.py
```

## 注意事項

- `.env` 已加入 `.gitignore`，私鑰不會上傳至 GitHub
- 執行後 Chrome 視窗會保持開啟

## 更換捷徑 Icon

1. 打開 macOS **捷徑** app
2. 對捷徑按右鍵 → **編輯**
3. 點選捷徑名稱旁邊的圖示
4. 選擇**從檔案選擇**，選取 `icon.png`
5. 按**完成**
