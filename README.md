url to md
================

This is a simple tool to extract the content of a URL and save it as markdown.

Usage:

```bash
python url_to_md.py --url <url> [--output <output-dir>]
python url_to_md.py -u <url> [-o <output-dir>]
```

Arguments:
- `--url` or `-u`: URL of the article to download (required)
- `--output` or `-o`: Output directory for saved markdown files (optional, default: `output`)

Examples:
```bash
python url_to_md.py --url https://example.com/article
python url_to_md.py -u https://example.com/article -o my_articles
```