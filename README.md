# Username Enumerator

This is a lightweight Open Source Intelligence (OSINT) tool that checks if a given username exists across multiple popular websites. It's helpful for digital footprinting, recon, and security research.

---

## Features

- Check a username on multiple platforms (GitHub, Instagram, Facebook, etc.)
- Smart detection using both status codes and page content
- Saves results to a JSON file (`found_profiles.json`)
- Easy to expand with more sites
- Minimal dependencies (just `requests`)

---

## Demo

```bash
$ python src/username_finder.py
Enter a username to check: nasa

[+] Found on GitHub: https://github.com/nasa
[+] Found on Reddit: https://www.reddit.com/user/nasa 
[+] Found on Facebook: https://www.facebook.com/nasa

Results saved to outputs/found_profiles.json
