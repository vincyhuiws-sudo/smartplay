import json
import requests
import sys

def fetch_smartplay_data():
    # 👇 將你啱啱喺 Headers 抄到嘅嗰條長長 Request URL 貼喺下面兩個單引號中間！
    api_url = 'https://www.smartplay.lcsd.gov.hk/rest/facility-catalog/api/v1/publ/facilities?venueId=72&keywords=%E5%A4%A7%E8%88%88%E9%AB%94%E8%82%B2%E9%A4%A8&playDate=2026-07-15&fatFilterType=MT'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://www.smartplay.lcsd.gov.hk/facilities/search-result', # 加返個 Referer 扮係由官方網頁連過嚟
        'Accept-Language': 'zh-HK,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    
    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        response.raise_for_status() # 如果狀態碼不是 200，直接拋出錯誤
        raw_data = response.json()
        
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(raw_data, f, ensure_ascii=False, indent=4)
            
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1) # 讓 GitHub Action 知道程式失敗了

if __name__ == "__main__":
    fetch_smartplay_data()
