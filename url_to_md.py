import sys
import argparse
import datetime
import trafilatura
from pathlib import Path

OUTPUT_DIR = Path("output")
EXTRACT_OPTIONS = {
    "include_comments": False,
    "include_tables": False,
    "output_format": "markdown",
    "include_links": False,
    "only_with_metadata": False,
}


def download_and_save_content(url: str, output_dir: Path | None) -> None:
    """Download content from URL and save it as a markdown file."""
    if not url:
        raise ValueError("URL cannot be empty")
    
    if output_dir is None:
        output_dir = OUTPUT_DIR
    
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
    
    # Add title as markdown header at the beginning of the content
    header = f"# {title}\n\n"
    full_content = header + content
    
    output_dir.mkdir(exist_ok=True)
    date_prefix = datetime.datetime.now().strftime("%Y%m%d")
    filename = output_dir / f"{date_prefix}_{title.replace(' ', '_')}.md"
    
    filename.write_text(full_content, encoding="utf-8")
    print(f"Content saved to {filename}")


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Download article content and save as markdown",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="example:\n  python url_to_md.py https://example.com/article"
    )
    parser.add_argument(
        "--url",
        "-u",
        type=str,
        default="",
        help="URL of the article to download (default: empty string)"
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=None,
        help="Output directory for saved markdown files (default: output)"
    )
    
    args = parser.parse_args()
    download_and_save_content(args.url, args.output)


if __name__ == "__main__":
    main()
