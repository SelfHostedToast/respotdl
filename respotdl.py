import os

links = []
url_prompt = True

while url_prompt:
    link = str(input("Enter the URL of your spotify song/album/playlist: "))
    print("Type 'done' to start downloading")
    if link.lower() == "done":
        url_prompt = False
    else:
        links.append(link)


for url in links:
    os.system(f"spotdl/bin/spotdl download {url} --output ./out/{{album-artist}}/{{album}}/{{title}}")
print("----The download process has completed----")