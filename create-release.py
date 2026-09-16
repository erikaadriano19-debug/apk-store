# APK Store Release Script - Python Version
# Run this to create a GitHub release for v1.1.1

import requests
import os
from typing import Dict

def create_github_release(owner: str, repo: str, tag: str, release_name: str, body: str) -> Dict:
    """
    Create a GitHub release using the GitHub API
    
    Args:
        owner: GitHub username
        repo: Repository name
        tag: Release tag (e.g., v1.1.1)
        release_name: Release title
        body: Release description
    
    Returns:
        Response JSON from GitHub API
    """
    
    # Get GitHub token from environment variable
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        print("Error: GITHUB_TOKEN environment variable not set")
        print("Set it with: export GITHUB_TOKEN=your_token_here")
        return None
    
    # GitHub API endpoint
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    
    # Headers
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Release data
    data = {
        "tag_name": tag,
        "name": release_name,
        "body": body,
        "draft": False,
        "prerelease": False
    }
    
    # Make request
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 201:
        print(f"✅ Release {tag} created successfully!")
        print(f"URL: {response.json()['html_url']}")
        return response.json()
    else:
        print(f"❌ Error creating release: {response.status_code}")
        print(f"Response: {response.text}")
        return None

if __name__ == "__main__":
    owner = "erikaadriano19-debug"
    repo = "apk-store"
    tag = "v1.1.1"
    release_name = "APK Store v1.1.1"
    
    body = """# APK Store v1.1.1

## Release Notes

### ✨ New Features
- Initial release of APK Store website
- Beautiful gradient UI with purple theme
- Search functionality to filter apps
- Responsive design for mobile and desktop
- "Free" pricing display (replaces $0)

### 🎨 UI/UX Improvements
- Smooth hover animations on app cards
- Mobile-optimized layout
- Clean and modern card-based design
- Easy-to-use search bar

### 🔧 Technical Details
- Built with HTML, CSS, and vanilla JavaScript
- Dynamic app loading from JSON
- Cross-browser compatible
- Lightweight and fast

### 📦 What's Included
- index.html - Main website
- style.css - Styling and animations
- script.js - App logic and search
- apps.json - Sample APK data

### 🚀 How to Use
1. Clone the repository
2. Open `index.html` in a browser
3. View all free APK apps
4. Use search to find specific apps
5. Click download to get started"""
    
    create_github_release(owner, repo, tag, release_name, body)
