import subprocess

# VULNERABILITY 1: Hardcoded secret (TruffleHog will catch this later)
API_KEY = "ak_test_1234567890abcdef1234567890abcdef"

def check_website_status(url):
    # VULNERABILITY 2: Command injection risk (Bandit will catch this later)
    # Never use shell=True with unverified user input!
    command = f"curl -I {url}"
    try:
        print(f"Running command: {command}")
        output = subprocess.check_output(command, shell=True, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return "Failed to reach website."

if __name__ == "__main__":
    target = "google.com"
    print(check_website_status(target))