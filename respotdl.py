import os

link = str(input("Enter the URL you wish to download:\n"))

os.system(f"spotdl download {
          link} --output ./{{album-artist}}/{{album}}/{{title}}")
