import requests
import re

def get_m3u8():
    url = "https://www.nowtv.com.tr/canli-yayin"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://www.nowtv.com.tr/'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        # Kaynak kodda m3u8 linkini ara
        m3u8_links = re.findall(r'(https?://[^\s"\'<>]+?\.m3u8[^\s"\'<>]*)', response.text)
        
        if m3u8_links:
            # İlk linki al ve ters slaşları temizle
            clean_link = m3u8_links[0].replace('\\/', '/')
            
            # IPTV Standartlarına uygun dosya içeriği oluştur
            # Sizin istediğiniz formatı birebir buraya yazıyoruz
            m3u8_content = (
                "#EXTM3U\n"
                "#EXT-X-VERSION:3\n"
                "#EXT-X-STREAM-INF:BANDWIDTH=1280000,RESOLUTION=1280x720\n"
                f"{clean_link}"
            )
            
            # Dosyayı yaz
            with open("now.m3u8", "w", encoding="utf-8") as f:
                f.write(m3u8_content)
            
            print(f"Başarılı: Link dosyaya IPTV formatında yazıldı.")
        else:
            print("Hata: Kaynak kodda m3u8 bağlantısı bulunamadı.")
            
    except Exception as e:
        print(f"Bağlantı hatası: {e}")

if __name__ == "__main__":
    get_m3u8()
