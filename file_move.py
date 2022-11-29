import os
import glob
import shutil
import getpass
from pystyle import Colors, Colorate, Write #pip install pystyle

#dizionario
extensions = {
    "jpg": "images",
    "png": "images",
    "ico": "images",
    "gif": "images",
    "svg": "images",
    "sql": "sql",
    "exe": "programs",
    "msi": "programs",
    "pdf": "pdf",
    "xlsx": "excel",
    "csv": "excel",
    "rar": "archive",
    "zip": "archive",
    "gz": "archive",
    "tar": "archive",
    "docx": "word",
    "torrent": "torrent",
    "txt": "text",
    "ipynb": "python",
    "py": "python",
    "pptx": "powerpoint",
    "ppt": "powerpoint",
    "mp3": "audio",
    "wav": "audio",
    "mp4": "video",
    "m3u8": "video",
    "webm": "video",
    "ts": "video",
    "json": "json",
    "css": "web",
    "js": "web",
    "html": "web",
    "apk": "apk",
    "sqlite3": "sqlite3",
}

if __name__ == "__main__":
    os.system("cls")
    print("All your files will be placed in folders")
    risposta = Write.Input('Are you sure you confirm do Yes/No: ', Colors.blue_to_purple)
    if risposta == "Yes".lower():
        #Trova il tuo usernname
        usernname = getpass.getuser()
        path = f"C:\\Users\\{usernname}\\Downloads"
        # l'impostazione dettagliata su 1 (o True) mostrerà tutti gli spostamenti dei file
        # l'impostazione di verbose su 0 (o False) mostrerà le informazioni necessarie di base
        verbose = 0
        for extension, folder_name in extensions.items():
            # ottenere tutti i file corrispondenti all'estensione
            files = glob.glob(os.path.join(path, f"*.{extension}"))
            Write.Print(f"[✓] Found {len(files)} files with {extension} extension\n", Colors.blue_to_cyan, interval=0.01)
            if not os.path.isdir(os.path.join(path, folder_name)) and files:
                # per ogni file in quell'estensione, spostalo nella cartella corrispondente
                Write.Print(f"[+] Making {folder_name} folder", Colors.blue_to_red, interval=0.02)
                os.mkdir(os.path.join(path, folder_name))
            for file in files:
                # per ogni file in quell'estensione, spostalo nella cartella corrispondente
                basename = os.path.basename(file)
                dst = os.path.join(path, folder_name, basename)
                if verbose:
                    Write.Print(f"[*] Moving {file} to {dst}", Colors.blue_to_white, interval=0.3)
                shutil.move(file, dst)
    elif risposta == 'No'.lower():
        print('Ok')








