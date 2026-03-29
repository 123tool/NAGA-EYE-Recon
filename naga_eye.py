#!/usr/bin/python
# -*- coding: utf-8 -*-
# CREATOR : SPY-E & 123Tool
# VERSION : 1.0 (Elite Edition)

import asyncio
import aiohttp
import time
import os
import sys
import re
from fake_useragent import UserAgent

# UI Color Palette
R = '\033[1;31m'  # Red Naga
G = '\033[1;32m'  # Green
Y = '\033[1;33m'  # Yellow
C = '\033[1;36m'  # Cyan
W = '\033[1;37m'  # White
Reset = '\033[0m'

class NagaEye:
    def __init__(self):
        self.ua = UserAgent()
        self.brand = "SPY-E & 123Tool"
        self.results = []
        # Database OSINT - Bisa ditambah hingga ribuan
        self.db = [
            {"name": "Instagram", "url": "https://www.instagram.com/{}", "type": "user"},
            {"name": "GitHub", "url": "https://github.com/{}", "type": "user"},
            {"name": "Facebook", "url": "https://www.facebook.com/{}", "type": "user"},
            {"name": "TikTok", "url": "https://www.tiktok.com/@{}", "type": "user"},
            {"name": "Twitter/X", "url": "https://twitter.com/{}", "type": "user"},
            {"name": "YouTube", "url": "https://www.youtube.com/@{}", "type": "user"},
            {"name": "Telegram", "url": "https://t.me/{}", "type": "user"},
            {"name": "Pinterest", "url": "https://www.pinterest.com/{}", "type": "user"},
            {"name": "Reddit", "url": "https://www.reddit.com/user/{}", "type": "user"},
            {"name": "Snapchat", "url": "https://www.snapchat.com/add/{}", "type": "user"},
            {"name": "Spotify", "url": "http://googleusercontent.com/open.spotify.com/4user/{}", "type": "user"},
            {"name": "Gravatar", "url": "https://en.gravatar.com/{}", "type": "email"},
            {"name": "Archive.org", "url": "https://archive.org/details/@{}", "type": "user"}
        ]

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def banner(self):
        self.clear()
        print(f"""{R}
          __  _  __   ___   __      _______   _______ 
         |  \| |/  \ /  _| /  \    |  ___ \ \ / /  ___|
         | | ' | [] | (_  | [] |   | |__  \ V /| |__  
         |_|_|\_|_/|_|\__||_/|_|   |  __|  > < |  __| 
                                   | |____/ . \| |____
          {W}OSINT INTELLIGENCE{R}       |_|____/_/ \_\____|
          
        {W}[+] CREATOR : {G}{self.brand}
        {W}[+] STATUS  : {C}PREMIUM / ELITE RECON
        {W}------------------------------------------{Reset}""")

    async def fetch(self, session, site, target):
        url = site['url'].format(target)
        headers = {'User-Agent': self.ua.random}
        try:
            async with session.get(url, headers=headers, timeout=10, allow_redirects=True) as response:
                # Logika deteksi: Status 200 biasanya berarti akun ada
                if response.status == 200:
                    content = await response.text()
                    # Cek tambahan untuk menghindari false positive pada beberapa situs
                    if "not found" not in content.lower() and "404" not in content:
                        sys.stdout.write(f"{W}[{G}FOUND{W}] {site['name']:<12}: {G}{url}{Reset}\n")
                        self.results.append(url)
        except:
            pass

    async def run_scan(self, target):
        is_email = re.match(r'[^@]+@[^@]+\.[^@]+', target)
        mode = "EMAIL" if is_email else "USERNAME"
        
        print(f"\n{C}─── [ TARGET: {Y}{target} {C}] ───{Reset}")
        print(f"{W}Scanning Mode : {G}{mode}{Reset}\n")
        
        conn = aiohttp.TCPConnector(limit=50) # Kecepatan tinggi, 50 request sekaligus
        async with aiohttp.ClientSession(connector=conn) as session:
            tasks = []
            for site in self.db:
                if is_email and site['type'] == "email":
                    tasks.append(self.fetch(session, site, target.split('@')[0]))
                elif not is_email and site['type'] == "user":
                    tasks.append(self.fetch(session, site, target))
            
            await asyncio.gather(*tasks)

    def main(self):
        self.banner()
        while True:
            target = input(f"\n{R}SPY-E@{G}NagaEye:~# {W}Input Target: {Reset}").strip()
            if not target: continue
            if target.lower() in ['exit', 'quit']: break
            
            self.results = []
            start_time = time.time()
            
            # Menjalankan mesin asinkron
            asyncio.run(self.run_scan(target))
            
            print(f"\n{C}─── [ HASIL PEMINDAIAN ] ───{Reset}")
            print(f"{W}Total Ditemukan : {G}{len(self.results)}{W} akun")
            print(f"{W}Waktu Eksekusi  : {Y}{time.time() - start_time:.2f} detik{Reset}")
            input(f"\n{W}Tekan Enter untuk lanjut...")
            self.banner()

if __name__ == "__main__":
    try:
        app = NagaEye()
        app.main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Keluar...{Reset}")
        sys.exit()
