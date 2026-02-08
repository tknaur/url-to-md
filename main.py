import trafilatura

OUTPUT_DIR: str = "output"

def main():
	print("Hello, World!")
	url: str = "https://edbatista.com/2026/01/how-to-facilitate-a-conflict-on-your-team.html"
	result: str = url_to_download(url)	
	print("End of the program.")

def url_to_download(url: str=None):
	downloaded: str = trafilatura.fetch_url(url)
	if downloaded is None:
		print("Failed to download the content.")
		return None
	
	content: str = trafilatura.extract(downloaded, include_comments=False, include_tables=False, output_format="markdown", include_links=False, with_metadata=True)
	if content is None:
		print("Failed to extract the content.")
		return None
	else:
		title: str = trafilatura.get_metadata(downloaded, "title")
		if title:
			print(f"Title: {title}")
			filename: str = f"{OUTPUT_DIR}/{title.replace(' ', '_')}.md"
			with open(filename, "w", encoding="utf-8") as f:
				f.write(content)
				print(f"Content saved to {filename}")

	return "Content extracted and saved successfully."

if __name__ == "__main__":
	main()