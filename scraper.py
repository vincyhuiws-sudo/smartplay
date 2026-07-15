import json
import requests

def fetch_smartplay_data():
    # 👇 將你啱啱喺 Headers 抄到嘅嗰條長長 Request URL 貼喺下面兩個單引號中間！
    api_url = 'https://www.smartplay.lcsd.gov.hk/rest/facility-catalog/api/v1/publ/facilities?venueId=72&keywords=%E5%A4%A7%E8%88%88%E9%AB%94%E8%82%B2%E9%A4%A8&playDate=2026-07-15&fatFilterType=MT'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*'
    }
    
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            raw_data = response.json()
            
            # 將抽返嚟嘅數據寫入 data.json
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(raw_data, f, ensure_ascii=False, indent=4)
                
            print("🎉 成功抽到空位數據，並已儲存為 data.json！")
        else:
            print(f"失敗！代碼：{response.status_code}")
            
    except Exception as e:
        print(f"發生錯誤：{e}")

if __name__ == "__main__":
    fetch_smartplay_data()
