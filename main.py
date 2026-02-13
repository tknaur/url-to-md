import sys
import datetime
import trafilatura
from pathlib import Path

OUTPUT_DIR = Path("output")
EXTRACT_OPTIONS = {
    "include_comments": False,
    "include_tables": False,
    "output_format": "markdown",
    "include_links": False,
    "only_with_metadata": True,
}


def download_and_save_content(url: str) -> None:
    """Download content from URL and save it as a markdown file."""
    if not url:
        raise ValueError("URL cannot be empty")
    
    downloaded = trafilatura.fetch_url(url)
    if downloaded is None:
        print("Error: Failed to download the content.")
        sys.exit(1)
    
    content = trafilatura.extract(downloaded, **EXTRACT_OPTIONS)
    if content is None:
        print("Error: Failed to extract content.")
        sys.exit(2)
    
    metadata = trafilatura.extract_metadata(downloaded, "title")
    title = (metadata.title or f"Untitled_{datetime.datetime.now().timestamp()}") if metadata else f"Untitled_{datetime.datetime.now().timestamp()}"
    
    OUTPUT_DIR.mkdir(exist_ok=True)
    filename = OUTPUT_DIR / f"{title.replace(' ', '_')}.md"
    
    filename.write_text(content, encoding="utf-8")
    print(f"Content saved to {filename}")


def main() -> None:
    """Main entry point."""
    url = "https://krzysztofjankowski.com/floppinux/floppinux-2025.html"
    download_and_save_content(url)


if __name__ == "__main__":
    main()
