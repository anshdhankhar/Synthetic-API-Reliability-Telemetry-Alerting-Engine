"""
API Uptime Monitoring System — V1

A simple command-line tool that checks one URL and reports whether it is UP or DOWN.
"""

import time

import requests


def is_up(status_code: int) -> bool:
    """Return True when the HTTP status code means the service is considered UP."""
    return 200 <= status_code <= 399


def print_result(
    url: str,
    status: str,
    http_status_code: int | None = None,
    response_time_ms: float | None = None,
    message: str | None = None,
) -> None:
    """Print a consistent, beginner-friendly report."""
    print()
    print(f"URL: {url}")
    print(f"Status: {status}")

    if http_status_code is not None:
        print(f"HTTP status code: {http_status_code}")

    if response_time_ms is not None:
        print(f"Response time: {response_time_ms:.2f} ms")

    if message:
        print(f"Message: {message}")

    print()


def main() -> None:
    # Step 1: Ask the user for a URL.
    url = input("Enter an HTTP/HTTPS URL to check: ").strip()

    if not url:
        print_result(
            url="(empty)",
            status="DOWN",
            message="No URL was entered. Please provide an HTTP or HTTPS address.",
        )
        return

    # Basic check so we can explain the problem clearly before calling the network.
    if not url.lower().startswith(("http://", "https://")):
        print_result(
            url=url,
            status="DOWN",
            message="Invalid URL. The address must start with http:// or https://.",
        )
        return

    # Step 2 & 3: Send one GET request and measure how long it takes.
    start = time.perf_counter()

    try:
        response = requests.get(url, timeout=10)
        elapsed_ms = (time.perf_counter() - start) * 1000

        # Step 4 & 5: Decide UP or DOWN from the HTTP status code.
        status = "UP" if is_up(response.status_code) else "DOWN"

        print_result(
            url=url,
            status=status,
            http_status_code=response.status_code,
            response_time_ms=elapsed_ms,
        )

    except requests.exceptions.Timeout:
        # Step 6 & 7: Timeout after 10 seconds counts as DOWN.
        print_result(
            url=url,
            status="DOWN",
            message="The request timed out after 10 seconds. The server may be slow or unreachable.",
        )

    except requests.exceptions.ConnectionError:
        print_result(
            url=url,
            status="DOWN",
            message="Could not connect to the server. Check the URL, your network, or whether the site is online.",
        )

    except requests.exceptions.TooManyRedirects:
        print_result(
            url=url,
            status="DOWN",
            message="Too many redirects. The URL may be misconfigured.",
        )

    except requests.exceptions.InvalidURL:
        print_result(
            url=url,
            status="DOWN",
            message="The URL format is not valid.",
        )

    except requests.exceptions.RequestException as error:
        # Catch any other request-related problem without crashing.
        print_result(
            url=url,
            status="DOWN",
            message=f"Request failed: {error}",
        )


if __name__ == "__main__":
    main()
