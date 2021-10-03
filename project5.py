import zipfile

unzip="file.zip"
print("chaliye shuru karte hai")
print("unzipping.........")
root=zipfile.ZipFile(unzip)

root.extractall('ZippedFolder')
root.close()

print("unzipped.....")

