import requests
import re
import sys

def get_m3u8():
    # NOW TV Canlı Yayın Sayfası
    url = "https://www.nowtv.com.tr/canli-yayin"
    
    # Sunucuyu gerçek bir kullanıcı olduğunuza ikna etmek için gerekli başlıklar
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://www.nowtv.com.tr/',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
    }
    
    try:
        # Sayfa içeriğini indir
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status() # Hata varsa durdur
        
        # Sayfa kaynağında .m3u8 ile biten linki bul
        # Regex: Tırnaklar arasındaki m3u8 uzantılı URL'yi yakalar
        m3u8_links = re.findall(r'(https?://[^\s"\'<>]+?\.m3u8[^\s"\'<>]*)', response.text)
        
        if m3u8_links:
            # Bulunan ilk linki al ve kaçış karakterlerini ( \/ ) temizle
            clean_link = m3u8_links[0].replace('\\/', '/')
            
            # Televizo ve diğer IPTV oynatıcıların tanıması için STANDART M3U FORMATI
            # #EXTINF satırı kanal adını belirler, altındaki satır ise linki verir
            m3u_content = (
                "#EXTM3U\n"
                "#EXTINF:-1,NOW TV\n"
                f"{clean_link}"
            )
            
            # Dosyayı "now.m3u8" adıyla kaydet
            with open("now.m3u8", "w", encoding="utf-8") as f:
                f.write(m3u_content)
            
            print(f"--- İŞLEM BAŞARILI ---")
            print(f"Bulunan Link: {clean_link}")
            
        else:
            print("HATA: Sayfa kaynağında m3u8 bağlantısı bulunamadı.")
            sys.exit(1)
            
    except Exception as e:
        print(f"BAĞLANTI HATASI: {e}")
        sys.exit(1)

if __name__ == "__main__":
    get_m3u8()
