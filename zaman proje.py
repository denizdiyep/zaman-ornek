import datetime
import pytz

# Tüm mevcut zaman dilimlerini listele ve ekrana bas
print("Mevcut Zaman Dilimleri:")
for tz in pytz.all_timezones:
    print(tz)

# show_date.py'nin devamı
# Zaman dilimi tanımlamaları
utc_timezone_str = 'UTC'
turkey_timezone_str = 'Europe/Istanbul'
domain_expire_date_str = "2024-10-04 10:00"

# Zaman dilimlerini oluştur
utc_timezone = pytz.timezone(utc_timezone_str)
turkey_timezone = pytz.timezone(turkey_timezone_str)

# Domain süresi bitiş tarihini string'den datetime nesnesine çevir
domain_expire_date = datetime.datetime.strptime(domain_expire_date_str, '%Y-%m-%d %H:%M')

# Domain bitiş tarihini UTC zaman diliminde ayarla
domain_expire_date_utc = utc_timezone.localize(domain_expire_date)

# UTC olan tarihi Türkiye zaman dilimine çevir
domain_expire_date_turkey = domain_expire_date_utc.astimezone(turkey_timezone)

# Sonuçları yazdır
print(f"\nDomain Süresi Bitiş Tarihi (UTC): {domain_expire_date_utc}")
print(f"Domain Süresi Bitiş Tarihi (Türkiye): {domain_expire_date_turkey}")
import pytz

# Ülke ve bulundukları kıta listesi
countries_continents = {
    "Turkey": "Europe",
    "Brazil": "South America",
    "Australia": "Australia",
    "Japan": "Asia",
    "South Africa": "Africa",
    "Canada": "North America",
    "India": "Asia",
    "Germany": "Europe",
    "Mexico": "North America",
    "Egypt": "Africa"
}

# Zaman dilimi bilgilerini almak için bir fonksiyon
def print_timezone_info(country, continent):
    try:
        timezone = None
        
        if country == "Turkey":
            timezone = "Europe/Istanbul"
        elif country == "Brazil":
            timezone = "America/Sao_Paulo"
        elif country == "Australia":
            timezone = "Australia/Sydney"
        elif country == "Japan":
            timezone = "Asia/Tokyo"
        elif country == "South Africa":
            timezone = "Africa/Johannesburg"
        elif country == "Canada":
            timezone = "America/Toronto"
        elif country == "India":
            timezone = "Asia/Kolkata"
        elif country == "Germany":
            timezone = "Europe/Berlin"
        elif country == "Mexico":
            timezone = "America/Mexico_City"
        elif country == "Egypt":
            timezone = "Africa/Cairo"
        
        if timezone:
            tz = pytz.timezone(timezone)
            print(f"{country} ({continent}): {timezone} - Şu anki saat: {pytz.datetime.datetime.now(tz)}")
        else:
            print(f"{country} ({continent}): Zaman dilimi bulunamadı!")
    
    except Exception as e:
        print(f"{country} ({continent}): Zaman dilimi alınırken hata oluştu! Hata: {e}")

# Ülke ve kıta bilgilerine göre zaman dilimlerini yazdır
for country, continent in countries_continents.items():
    print_timezone_info(country, continent)
import pytz
import datetime

# Ülke ve bulundukları kıta listesi
countries_continents = {
    "Turkey": "Europe",
    "Brazil": "South America",
    "Australia": "Australia",
    "Japan": "Asia",
    "South Africa": "Africa",
    "Canada": "North America",
    "India": "Asia",
    "Germany": "Europe",
    "Mexico": "North America",
    "Egypt": "Africa"
}

# Zaman dilimi bilgilerini almak ve günü yazdırmak için bir fonksiyon
def print_day_info(country, continent):
    try:
        timezone = None
        
        # Ülkelere göre zaman dilimi tanımlamaları
        if country == "Turkey":
            timezone = "Europe/Istanbul"
        elif country == "Brazil":
            timezone = "America/Sao_Paulo"
        elif country == "Australia":
            timezone = "Australia/Sydney"
        elif country == "Japan":
            timezone = "Asia/Tokyo"
        elif country == "South Africa":
            timezone = "Africa/Johannesburg"
        elif country == "Canada":
            timezone = "America/Toronto"
        elif country == "India":
            timezone = "Asia/Kolkata"
        elif country == "Germany":
            timezone = "Europe/Berlin"
        elif country == "Mexico":
            timezone = "America/Mexico_City"
        elif country == "Egypt":
            timezone = "Africa/Cairo"
        
        # Zaman dilimi varsa şu anki günü al ve yazdır
        if timezone:
            tz = pytz.timezone(timezone)
            current_time = datetime.datetime.now(tz)
            current_day = current_time.strftime("%A")  # Gün ismini al
            print(f"{country} ({continent}): {timezone} - Bugün: {current_day}")
        else:
            print(f"{country} ({continent}): Zaman dilimi bulunamadı!")
    
    except Exception as e:
        print(f"{country} ({continent}): Zaman dilimi alınırken hata oluştu! Hata: {e}")

# Ülke ve kıta bilgilerine göre gün bilgilerini yazdır
for country, continent in countries_continents.items():
    print_day_info(country, continent)
import pytz
import datetime

# Ülke ve bulundukları kıta listesi
countries_continents = {
    "Turkey": "Europe",
    "Brazil": "South America",
    "Australia": "Australia",
    "Japan": "Asia",
    "South Africa": "Africa",
    "Canada": "North America",
    "India": "Asia",
    "Germany": "Europe",
    "Mexico": "North America",
    "Egypt": "Africa"
}

# Zaman dilimi bilgilerini almak ve günü yazdırmak için bir fonksiyon
def print_day_info(country, continent):
    try:
        timezone = None
        
        # Ülkelere göre zaman dilimi tanımlamaları
        if country == "Turkey":
            timezone = "Europe/Istanbul"
        elif country == "Brazil":
            timezone = "America/Sao_Paulo"
        elif country == "Australia":
            timezone = "Australia/Sydney"
        elif country == "Japan":
            timezone = "Asia/Tokyo"
        elif country == "South Africa":
            timezone = "Africa/Johannesburg"
        elif country == "Canada":
            timezone = "America/Toronto"
        elif country == "India":
            timezone = "Asia/Kolkata"
        elif country == "Germany":
            timezone = "Europe/Berlin"
        elif country == "Mexico":
            timezone = "America/Mexico_City"
        elif country == "Egypt":
            timezone = "Africa/Cairo"
        
        # Zaman dilimi varsa şu anki günü al ve yazdır
        if timezone:
            tz = pytz.timezone(timezone)
            current_time = datetime.datetime.now(tz)
            current_day = current_time.strftime("%A")  # Gün ismini al
            print(f"{country} ({continent}): {timezone} - Bugün: {current_day}")
        else:
            print(f"{country} ({continent}): Zaman dilimi bulunamadı!")
    
    except Exception as e:
        print(f"{country} ({continent}): Zaman dilimi alınırken hata oluştu! Hata: {e}")

# Ülke ve kıta bilgilerine göre gün bilgilerini yazdır
for country, continent in countries_continents.items():
    print_day_info(country, continent)