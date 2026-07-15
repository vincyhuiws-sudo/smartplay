import json
import datetime
# import requests  # 真實環境需要用到 requests 庫來呼叫 API

def fetch_smartplay_data():
    # 這裡是你破解 API 後的邏輯
    # headers = {'User-Agent': '...', 'Authorization': 'Bearer ...'}
    # response = requests.get('真正的_API_URL', headers=headers)
    # raw_data = response.json()
    
    # 這裡我們模擬把抓到的資料整理成前端需要的格式
    processed_data = {
        "lastUpdate": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "times": ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00"],
        "schedule": [
            {"date": "15/7", "slots": [1, 0, 0, 2, 0, 0]},
            {"date": "16/7", "slots": [0, 0, 1, 1, 0, 0]},
        ]
    }
    
    # 將數據寫入 data.json 檔案
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=4)
        
    print("Data successfully saved to data.json")

if __name__ == "__main__":
    fetch_smartplay_data()