#!/usr/bin/env python
"""
Script to fetch citation counts from Google Scholar and store them in _data/citations.yml
This script is designed to be run by a GitHub Action.

modified from https://github.com/BernardoCama/BernardoCama.github.io/blob/main/bin/update_scholar_citations.py
"""

#!/usr/bin/env python3
"""
Script to fetch citation counts from Google Scholar using SerpAPI
and store them in _data/citations.yml
"""

import os
import yaml
import time
import requests
from datetime import datetime

# Configuration
SCHOLAR_USER_ID = "hv9vhhAAAAAJ"  # Replace with your Google Scholar ID
OUTPUT_FILE = "_data/citations.yml"
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
SERPAPI_BASE_URL = "https://serpapi.com/search.json"

# Create data directory if it doesn't exist
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)


def log(msg):
    print(f"[{datetime.now()}] {msg}", flush=True)


def get_author_data(user_id):
    """Fetch author profile and publications from SerpAPI"""
    params = {
        "engine": "google_scholar_author",
        "author_id": user_id,
        "api_key": SERPAPI_API_KEY,
        "num": 100  # Fetch up to 100 publications
    }

    try:
        log(f"Requesting author data from SerpAPI for ID {user_id}...")
        response = requests.get(SERPAPI_BASE_URL, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        log(f"Error fetching data from SerpAPI: {e}")
        return None


def parse_author_data(data):
    """Parse the SerpAPI response into our citation format"""
    citation_data = {
        "metadata": {
            "last_updated": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        },
        "papers": {}
    }

    publications = data.get("articles", [])
    log(f"Found {len(publications)} publications.")

    for pub in publications:
        try:
            pub_id = pub['citation_id']
            title = pub.get("title", "Unknown Title")
            year = pub.get("year", "Unknown Year")
            citations = pub.get("cited_by", {}).get("value", 0) or 0

            log(f"Processing: {title} ({year}) - Citations: {citations}")
            citation_data["papers"][pub_id] = {
                "title": title,
                "year": year,
                "citations": citations
            }
        except Exception as e:
            log(f"Error processing publication: {e}")
            continue

    return citation_data


def save_to_yaml(data, output_path):
    try:
        with open(output_path, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)
        log(f"Citation data saved to {output_path}")
    except Exception as e:
        log(f"Error saving YAML: {e}")


def main():
    if not SERPAPI_API_KEY:
        log("Error: SERPAPI_API_KEY is not set in environment variables.")
        return

    data = get_author_data(SCHOLAR_USER_ID)
    if data:
        citation_data = parse_author_data(data)
        save_to_yaml(citation_data, OUTPUT_FILE)
    else:
        log("No data retrieved from SerpAPI.")


if __name__ == "__main__":
    main()