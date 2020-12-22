import zipfile

print("""

Directory Listing Zip :
 ____      _          _
|  _ \ ___| |__   ___| |___  ___  ___
| |_) / _ \ '_ \ / _ \ / __|/ _ \/ __|
|  _ <  __/ |_) |  __/ \__ \  __/ (__
|_| \_\___|_.__/ \___|_|___/\___|\___|


""")

file = input("File zip : ")
z = zipfile.ZipFile(file)

wordlists = input('File Wordlists : ')
wordlist = open(wordlists, 'r').read()
wordlist = wordlist.splitlines()

nama_file_sekarang = input("Isi file yang ada di dalam zip ? :")
# Proses Directory Listing
percobaan = 0
for word in wordlist:
    try:
        percobaan += 1
        z.setpassword(word.encode('ascii'))
        z.extract(nama_file_sekarang)
        print(f"Percobaan sebanyak", percobaan, "password adalah", word)
        break
    except:
        pass
