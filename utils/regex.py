import re

btc_p = re.compile(r'\b(?:[13][a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[a-zA-HJ-NP-Z0-9]{25,90})\b')
eth_p = re.compile(r'\b0x[0-9a-fA-F]{40}\b')
ltc_p = re.compile(r'\b(?:[LM][a-km-zA-HJ-NP-Z1-9]{26,33}|ltc1[a-zA-HJ-NP-Z0-9]{25,90})\b')
xmr_p = re.compile(r'\b4[0-9a-zA-Z][1-9A-HJ-NP-Za-km-z]{91,104}\b')
xrp_p = re.compile(r'\br[0-9a-zA-Z]{24,34}\b')
doge_p = re.compile(r'\bD{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}\b')
sol_p = re.compile(r'\b[1-9A-HJ-NP-Za-km-z]{32,44}\b')

patterns = {"btc": btc_p, "eth": eth_p, "ltc": ltc_p,
"xmr": xmr_p, "xrp": xrp_p, "doge": doge_p, "sol": sol_p}

order = ["btc","eth","ltc","xmr","xrp","doge","sol"]

def identify(text):
    for c in order:
        m = patterns[c].search(text)
        if m: return c, m
    return None, None
