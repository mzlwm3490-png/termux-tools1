# -*- coding: utf-8 -*-
import os
import time

TOOLS = {
    "1": ("تحديث النظام", "pkg update && pkg upgrade -y"),
    "2": ("python", "pkg install python -y"),
    "3": ("git", "pkg install git -y"),
    "4": ("curl", "pkg install curl -y"),
    "5": ("wget", "pkg install wget -y"),
    "6": ("nmap", "pkg install nmap -y"),
    "7": ("figlet", "pkg install figlet -y"),
    "8": ("phishing", "pkg install phishing -y"),  # صححت phiching إلى phishing
    "9": ("termux-tools", "pkg install termux-tools -y"),
    "10": ("nano", "pkg install nano -y"),
    "11": ("john", "pkg install john -y"),  # صححت imstall إلى install
    "12": ("hydra", "pkg install hydra -y"),
    "13": ("wireshark", "pkg install wireshark -y"),
    "14": ("aircrack-ng", "pkg install aircrack-ng -y"),
    "15": ("binwalk", "pkg install binwalk -y"),
    "16": ("hashcat", "pkg install hashcat -y"),
    "17": ("openssh", "pkg install openssh -y"),
    "18": ("net-tools", "pkg install net-tools -y"),
    "19": ("termux-api", "pkg install termux-api -y"),
    "20": ("netcat-openbsd", "pkg install netcat-openbsd -y"),  # أضفت netcat-
    "21": ("ettercap", "pkg install ettercap -y"),  # صححت ettrcap إلى ettercap
    "22": ("dnsutils", "pkg install dnsutils -y"),
    "23": ("metasploit", "pkg install metasploit -y"),
    "24": ("burpsuite", "pkg install burpsuite -y"),  # صححت purpsuite إلى burpsuite
    "25": ("mitmproxy", "pkg install mitmproxy -y"),
    "26": ("radare2", "pkg install radare2 -y"),
    "27": ("ghidra", "pkg install ghidra -y"),
    "28": ("gobuster", "pkg install gobuster -y"),  # أزلت المسافة الزائدة
    "29": ("dirb", "pkg install dirb -y"),
    "30": ("wpscan", "pkg install wpscan -y"),
}

def clear():
    os.system("clear")

def banner():
    clear()
    os.system("figlet abo mzlom")
    print("=" * 40)

def show_menu():
    print("[1] update && pkg upgrade -y")
    print("[2] Install python -y")
    print("[3] Install git -y")
    print("[4] install curl -y")
    print("[5] Install wget -y")
    print("[6] install nmap -y")
    print("[7] install figlet -y")
    print("[8] install phishing -y")  # تحديث هنا أيضاً
    print("[9] install termux-tools -y")
    print("[10] install nano -y")
    print("[11] install john -y")
    print("[12] install hydra -y")
    print("[13] install wireshark -y")  # أصلحت المسافة
    print("[14] install aircrack-ng -y")
    print("[15] install binwalk -y")
    print("[16] install hashcat -y")  # أصلحت الأقواس
    print("[17] install openssh -y")
    print("[18] install net-tools -y")
    print("[19] install termux-api -y")
    print("[20] install netcat-openbsd -y")  # تحديث هنا أيضاً
    print("[21] install ettercap -y")  # تحديث هنا أيضاً
    print("[22] install dnsutils -y")
    print("[23] install metasploit -y")
    print("[24] install burpsuite -y")  # تحديث هنا أيضاً
    print("[25] install mitmproxy -y")
    print("[26] install radare2 -y")
    print("[27] install ghidra -y")
    print("[28] install gobuster -y")
    print("[29] install dirb -y")
    print("[30] install wpscan -y")
    print("\n[0] Exit")
    print("=" * 40)

def install_tool(choice):
    tool = TOOLS.get(choice)
    if not tool:
        print("❌ اختيار غير صحيح")
        return

    name, command = tool
    print(f"⏳ جارٍ تثبيت {name} ...")
    status = os.system(command)

    if status == 0:
        print(f"✅ تم تثبيت {name} بنجاح")
    else:
        print(f"❌ فشل تثبيت {name}")

def main():
    while True:
        banner()
        show_menu()
        choice = input("[?] اختر رقم: ").strip()

        if choice == "0":
            print("👋 مع السلامة")
            break
        elif choice in TOOLS:
            install_tool(choice)
            time.sleep(2)  # إضافة تأخير لرؤية النتيجة
        else:
            print("❌ رقم غير صحيح، حاول مرة أخرى")
            time.sleep(1)

if __name__ == "__main__":
    main()
