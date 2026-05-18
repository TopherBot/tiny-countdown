# tiny‑countdown

A tiny command‑line countdown timer written in pure Python.

## Features
- No external dependencies.
- Accepts human‑readable durations (seconds, minutes, hours).
- Works on Windows, macOS, and Linux.
- Emits a system beep when the timer ends.

## Installation
Just clone the repo and run the script with Python 3.6+.

```bash
git clone https://github.com/yourname/tiny-countdown.git
cd tiny-countdown
python3 countdown.py 10s   # 10‑second timer
```

## Usage
```bash
python3 countdown.py <duration>
```
`<duration>` must be a number followed by a unit:
- `s` – seconds
- `m` – minutes
- `h` – hours

Examples:
```bash
python3 countdown.py 30s   # 30 seconds
python3 countdown.py 5m    # 5 minutes
python3 countdown.py 1h    # 1 hour
```

## License
MIT – see the LICENSE file in the repository.
