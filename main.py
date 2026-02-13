import datetime
import trafilatura

OUTPUT_DIR: str = "output"

def main():
	url: str = "https://krzysztofjankowski.com/floppinux/floppinux-2025.html"
	result: str = url_to_download(url)	
	

def url_to_download(url: str=None):
	downloaded: str = trafilatura.fetch_url(url)
	if downloaded is None:
		print("Failed to download the content.")
		return None
	
	content: str = trafilatura.extract(downloaded, include_comments=False, include_tables=False, output_format="markdown", include_links=False, only_with_metadata=True)
	if content is None:
		print("Failed to extract the content.")
		return None
	else:
		metadata: trafilatura.settings.Document = trafilatura.extract_metadata(downloaded, "title")
		if metadata is not None:
			title: str = metadata.title if metadata.title else f"Untitled_{datetime.datetime.now().timestamp()}"
			filename: str = f"{OUTPUT_DIR}/{title.replace(' ', '_')}.md"
			with open(filename, "w", encoding="utf-8") as f:
				f.write(content)
				print(f"Content saved to {filename}")

if __name__ == "__main__":
	main()