import requests
import re

def get_m3u8():
    url = "https://www.nowtv.com.tr/canli-yayin"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        # JSON objesi veya script tagleri içindeki m3u8 linkini yakalar
        m3u8_links = re.findall(r'(https?://[^\s"\'<>]+?\.m3u8[^\s"\'<>]*)', response.text)
        
        if m3u8_links:
            # Kaçış karakterlerini temizle ( \/ -> / )
            clean_link = m3u8_links[0].replace('\\/', '/')
            
            # Sadece linki dosyaya yaz
            with open("now.m3u8", "w", encoding="utf-8") as f:
                f.write(clean_link)
            print(f"Başarılı: {clean_link}")
        else:
            print("Hata: Kaynak kodda m3u8 bağlantısı bulunamadı.")
    except Exception as e:
        print(f"Bağlantı hatası: {e}")

if __name__ == "__main__":
    get_m3u8()
