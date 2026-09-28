from typing import Any, Dict, List, Optional
import requests
from requests.exceptions import RequestException, Timeout


class APIClient:
    """A resilient HTTP client wrapper around Python requests."""

    def __init__(self, base_url: str, timeout: float = 5.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """Sends a GET request to the given endpoint and returns parsed JSON.
        
        Handles timeouts and HTTP errors gracefully without blowing up with a raw traceback.
        """
        formatted_endpoint = endpoint.lstrip("/")
        url = f"{self.base_url}/{formatted_endpoint}"

        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except Timeout:
            print(f"[API Error] Request to '{url}' timed out after {self.timeout} seconds.")
            return []
        except RequestException as err:
            print(f"[API Error] Failed to fetch data from '{url}': {err}")
            return []


def find_posts(posts: List[Dict[str, Any]], query: str) -> List[Dict[str, Any]]:
    """Filters posts where the search query matches title or body (case-insensitive)."""
    if not isinstance(posts, list) or not query:
        return []

    q = query.lower()
    return [
        post for post in posts
        if q in post.get("title", "").lower() or q in post.get("body", "").lower()
    ]


class PostSearchTool:
    """Tool wrapper that pairs an API client with search capability."""

    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com") -> None:
        self.client = APIClient(base_url=base_url)

    def run(self, query: str) -> List[Dict[str, Any]]:
        """Fetches posts via the client and returns matching results."""
        posts = self.client.get("/posts")
        return find_posts(posts, query)


def main() -> None:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    # Step 1: Create an API client
    print("--- 1. Initializing API Client ---")
    client = APIClient(base_url=BASE_URL)

    # Step 2: Get posts
    print("\n--- 2. Fetching Posts ---")
    posts = client.get("/posts")
    print(f"Retrieved {len(posts)} posts total.")

    # Step 3: Search them directly
    print("\n--- 3. Direct Post Search ---")
    query = "qui"
    results = find_posts(posts, query)
    print(f"Found {len(results)} matching posts for query: '{query}'")

    # Step 4 & 5: Create tool and run search
    print("\n--- 4 & 5. PostSearchTool Execution ---")
    tool = PostSearchTool(base_url=BASE_URL)
    tool_results = tool.run("qui")
    print(f"Tool found {len(tool_results)} matching posts for query: '{query}'")

    if tool_results:
        first_match = tool_results[0]
        print(f"\nSample Match (ID {first_match.get('id')}):")
        print(f"Title: {first_match.get('title')}")

    # Step 6: Test Error Handling (Invalid URL)
    print("\n--- 6. Error Handling Demonstration ---")
    broken_client = APIClient(base_url="https://invalid-api-host-that-does-not-exist.org")
    broken_posts = broken_client.get("/posts")
    print(f"Graceful fallback result: {broken_posts}")


if __name__ == "__main__":
    main()