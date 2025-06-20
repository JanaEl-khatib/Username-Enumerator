import requests

# A dictionary of websites to check
SITES = {
    "GitHub": {
        "url": "https://github.com/{}", 
        "not_found_text": "Not Found"
    },
    "Reddit": {
        "url": "https://www.reddit.com/user/{}",
        "not_found_text": "Sorry, nobody on Reddit goes by that name"
    },
    "Facebook": {
        "url": "https://www.facebook.com/{}", 
        "not_found_text": "This Content Isn't Available"
    }
}

# Check username if they exist on each website
def check_username(username):
    found_profiles = {}

    for site, site_info in SITES.items():
        profile_url = site_info["url"].format(username)
        not_found_text = site_info["not_found_text"]

        try:
            response = requests.get(profile_url, timeout=5)

            if response.status_code == 200 and not_found_text.lower() not in response.text.lower():
                found_profiles[site] = profile_url
                print(f"[+] Found on {site}: {profile_url}")
            else:
                print(f"[-] Not found on {site}")
        except requests.RequestException as e:
            print(f"[!] Error checking {site}: {e}")
    
    return found_profiles

# Only run this if script is executed directly
if __name__ == "__main__":
    username = input("Enter a username to check: ")
    results = check_username(username)

    if results:
        import json, os
        os.makedirs("../outputs", exist_ok=True)

        with open("../outputs/found_profiles.json", "w") as f:
            json.dump(results, f, indent=2)

        print("\nResults saved to outputs/found_profiles.json")
    else:
        print("\nNo profiles found.")
