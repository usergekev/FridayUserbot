"""Emoji

Available Commands:

.kevin"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd

@borg.on(admin_cmd("(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.01
    animation_ttl = range(0, 288)
    input_str = event.pattern_match.group(1)
    if input_str == "kevin":
        await event.edit(input_str)
        animation_chars = [
            "⚡KEVIN⚡",
            "↤↤↤↤↤ KEVIN ↦↦↦↦↦",
            "◦•●◉✿ KEVIN ✿◉●•◦",
            "☆:**:. KEVIN .:**:.☆",
            "l am best",
            "кєνιη",
            "Ҝ乇ᐯ丨几",
            "ＫΞＶＩＮ",
            "ₖₑᵥᵢₙ",
            "🄺🄴🅅🄸🄽",
            "≋K≋E≋V≋I≋N≋",
            "【K】【E】【V】【I】【N】",
            "▀▄▀▄▀▄ KEVIN ▄▀▄▀▄▀",
            " [̲̅K][̲̅E][̲̅V][̲̅I][̲̅N]",
            "K⃣   E⃣   V⃣   I⃣   N⃣",
            "𝕜ꫀꪜⅈꪀ",
            "🅺🅴🆅🅸🅽",
            "KEVIN",
            "кєשเภ",
            "K̷̼̻͓͊͗̇̓̌͘E̷̡̨͔̦̞̠͔̩̍̓͂̅̃̊͜͝V̴̛̠̈́͆̓͗̇̌̉I̶̢͙̗̘̫̥̭͍͐͝N̷̫̈̈́̅͗́̂̔͝",
            "ＫＥＶＩＮ 🍭",
            "KΣVIП",
            "NIΛƎ⋊",
            "🄺🄴🅅🄸🄽",
            "░K░E░V░I░N░",
            "kēงiຖ",
            "【K】【E】【V】【I】【N】",
            "꧁꧁ҜＥש𝓘Ｎ꧂꧂",
            "••¤(`×¤ ｋ€𝐯𝔦Ň ¤×´)¤••",
            "💤📿кєV𝔦ή📿💤",
            "•.,¸¸,.•´¯ кє𝕧ιᑎ ¯`•.,¸¸,.•´",
            "░▒▓█ ｋ𝐄𝕍𝐢η █▓▒░",
            "༒•кєνเᶰ•༒",
            "@iamkevinbest",
            "!¤*'~``~'*¤!| ЌᵉᐯⒾ𝓷 |!¤*'~``~'*¤!|",
            "☆꧁༒☬🤖🐰ᵏєᵛ丨Ň🐰🤖☬༒꧂☆"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 72])
