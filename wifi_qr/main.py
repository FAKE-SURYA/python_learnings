import qrcode
import sys

def get_wifi_qr_string(ssid, password, security):
    # Format: WIFI:T:WPA;S:SSID;P:password;;
    return f"WIFI:T:{security};S:{ssid};P:{password};;"

def main():
    print("=== WiFi QR Code Generator ===")
    ssid = input("Enter WiFi SSID (name): ")
    password = input("Enter WiFi password: ")
    security = input("Enter security type (WPA/WPA2/WEP/NONE): ").upper()
    if security not in ["WPA", "WPA2", "WEP", "NONE"]:
        print("Invalid security type. Use WPA, WPA2, WEP, or NONE.")
        sys.exit(1)
    if security == "NONE":
        qr_string = f"WIFI:T:nopass;S:{ssid};;"
    else:
        qr_string = get_wifi_qr_string(ssid, password, security)
    img = qrcode.make(qr_string)
    filename = f"wifi_qr_{ssid}.png"
    img.save(filename)
    print(f"QR code saved as {filename}. Scan it to connect to WiFi!")

if __name__ == "__main__":
    main()

