import os
import requests

from dotenv import load_dotenv

load_dotenv()


def scrape_linked_profile(linkedin_profile_url: str, mock: bool = False):
    """Scrape information from linkedin profiles"""

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json"
        response = requests.get(linkedin_profile_url, timeout=10)

        return response.json()
    else:
        if os.getenv("SCRAPING_API_KEY") == "":
            raise Exception("SCRAPING_API_KEY is not set")
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apiKeys": [os.getenv("SCRAPING_API_KEY")],
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(api_endpoint, params=params, timeout=10)
        data = response.json().get("person")
        data = {
            k: v
            for k, v in data.items()
            if v not in ([], "", "", None) and k not in ["certifications"]
        }

        return data


if __name__ == "__main__":
    print(
        scrape_linked_profile(
            linkedin_profile_url="https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json",
            mock=True,
        )
    )
