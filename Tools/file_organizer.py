import os
import shutil

def main():
    path = input("Enter the folder path: ").strip()
    if path:
        print(sort_files(path))
    else:
        print("Enter a file path.")

def sort_files(file_path):
    files = os.listdir(file_path)
    for file in files:
        extension = file.split(".")[-1]
        if extension in ["jpg","jpeg","png","gif","svg"]:
            folder = "Images"
        elif extension in ["mp3","wav","aac","flac","aiff","aif","ogg","opus"]:
            folder = "Audios"
        elif extension in ["mp4","mov","mkv","wmv","webm"]:
            folder = "Videos"
        elif extension in ["zip","rar","7z"]:
            folder = "Compressed Files"   
        elif extension in ["exe","apk","sys","dll"]:
            folder = "Executables"
        elif extension in ["docx","doc","pdf","txt","ppt","csv","xml","json"]:
            folder = "Data Files"
        elif extension in ["html","htm","css","js","py","php","c","cpp","cs","java","ts","go","rs","swift","sql"]:
            folder = "Programming Files"
        else:
            folder = "Others"
        os.makedirs(os.path.join(file_path,folder),exist_ok=True)
        shutil.move(os.path.join(file_path,file),os.path.join(file_path,folder,file))  
    return "File Sorting Completed." 

if __name__=="__main__":
    main()