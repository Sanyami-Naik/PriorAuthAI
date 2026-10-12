
import requests
from bs4 import BeautifulSoup

POLICY_URL = (
    "https://www.aetna.com/cpb/medical/"
    "data/200_299/0236.html"
)


def fetch_policy(url: str) -> str:
    """Download and extract text from a policy webpage."""

    response = requests.get(
        url,
        timeout=30,
        headers={
            "User-Agent": "PriorAuthAI-EducationalDemo/1.0"
        }
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove content unrelated to the policy
    for element in soup([
        "script", "style", "nav", "footer"
    ]):
        element.decompose()

    main_content = (
        soup.find("main")
        or soup.find("article")
        or soup.body
    )

    if main_content is None:
        raise ValueError("No policy content found")

    text = main_content.get_text(
        separator="\n",
        strip=True
    )

    if len(text) < 500:
        raise ValueError(
            "Extracted policy text is unexpectedly short"
        )

    return text


if __name__ == "__main__":
    print("Fetching Aetna MRI policy...")

    policy_text = fetch_policy(POLICY_URL)

    print("\nPolicy extracted successfully!")
    print("Characters:", len(policy_text))

    print("\n--- POLICY PREVIEW ---\n")
    print(policy_text[:2000])
