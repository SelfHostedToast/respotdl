import os

# Environment -- Setup the following --
#
rem_user = ""
rem_server = ""
rem_path = ""
# ---------------------------------------

links = []
url_prompt = True


while url_prompt:
    link = str(input("Enter the URL of your spotify song/album/playlist: "))
    print("Type 'done' to start downloading")
    if link.lower() == "done":
        url_prompt = False

    else:
        links.append(link)

print("Clearing previous downloads...\n")
os.system(f"rm -r ./out/*")

for url in links:
    os.system(
        f"spotdl/bin/spotdl download {url} --output ./out/{{album-artist}}/{{album}}/{{title}}")
print("----The download process has completed----")


remote_copy = input(
    "Would you like to copy these files to a remote server y/n?\n")
if remote_copy.lower() == 'y':
    os.system(
        f"sshpass -f ./creds scp -r ./out/* {rem_user}@{rem_server}:{rem_path}")
else:
    print('Thanks for using my app!')
