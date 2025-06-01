import subprocess
import re
import qrcode
import os

def get_connected_ssid():
    output = subprocess.check_output("netsh wlan show interfaces", shell=True).decode("utf-8", errors="ignore")
    match = re.search(r"^\s*SSID\s*:\s(.+)$", output, re.MULTILINE)
    return match.group(1).strip() if match else None

def get_wifi_password(ssid):
    cmd = f'netsh wlan show profile name="{ssid}" key=clear'
    output = subprocess.check_output(cmd, shell=True).decode("utf-8", errors="ignore")
    password_match = re.search(r"Key Content\s*:\s(.+)", output)
    security_match = re.search(r"Authentication\s*:\s(.+)", output)
    password = password_match.group(1).strip() if password_match else ""
    security = security_match.group(1).strip() if security_match else "WPA2"

    if "WPA" in security:
        sec_type = "WPA"
    elif "WEP" in security:
        sec_type = "WEP"
    else:
        sec_type = "nopass"

    return password, sec_type

def generate_wifi_qr(ssid, password, security, filename="wifi_qr.png"):
    wifi_config = f"WIFI:T:{security};S:{ssid};P:{password};;"
    qr = qrcode.make(wifi_config)
    qr.save(filename)
    print(f"{filename} dosyasına QR kod kaydedildi.")

    # QR görselini otomatik aç
    os.startfile(filename)

# Ana işlem
ssid = get_connected_ssid()
if ssid:
    print(f"Bağlı olunan ağ: {ssid}")
    password, security = get_wifi_password(ssid)
    print(f"Şifre: {password}, Güvenlik: {security}")
    generate_wifi_qr(ssid, password, security)
else:
    print("Wi-Fi ağına bağlı değilsin veya SSID alınamadı.")
