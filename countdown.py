#!/usr/bin/env python3
"""Tiny countdown timer.

Usage: python countdown.py <duration>
Duration format: <number><unit> where unit is s, m, or h.
Example: 10s, 5m, 1h.
"""
import sys
import time
import re
import platform

def parse_duration(arg):
    """Convert a string like '10s', '5m', '1h' into seconds."""
    m = re.fullmatch(r"(\d+)([smh])", arg.lower())
    if not m:
        raise ValueError("Invalid duration format. Use <number><unit> where unit is s, m, or h.")
    value, unit = int(m.group(1)), m.group(2)
    if unit == 's':
        return value
    if unit == 'm':
        return value * 60
    if unit == 'h':
        return value * 3600
    # Should never reach here
    return 0

def beep():
    """Emit a simple beep sound appropriate for the platform."""
    if platform.system() == "Windows":
        try:
            import winsound
            winsound.Beep(1000, 500)
        except Exception:
            print('\a', end='', flush=True)
    else:
        # Unix-like terminals interpret \a as a bell character
        print('\a', end='', flush=True)

def format_time(seconds):
    hrs, rem = divmod(seconds, 3600)
    mins, secs = divmod(rem, 60)
    if hrs:
        return f"{hrs:02d}:{mins:02d}:{secs:02d}"
    else:
        return f"{mins:02d}:{secs:02d}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python countdown.py <duration>")
        sys.exit(1)
    try:
        total_seconds = parse_duration(sys.argv[1])
    except ValueError as e:
        print(e)
        sys.exit(1)

    for remaining in range(total_seconds, 0, -1):
        print(f"\r{format_time(remaining)}", end='', flush=True)
        time.sleep(1)
    print("\rTime's up!   ")
    beep()

if __name__ == "__main__":
    main()
