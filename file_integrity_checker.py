import hashlib
import os

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    
    except FileNotFoundError:
        print("File not found ")
        return None


def save_hash(file_path, hash_value):
    with open("hash_store.txt", "a") as f:
        f.write(f"{file_path}|{hash_value}\n")


def check_integrity(file_path):
    current_hash = calculate_hash(file_path)
    
    if not current_hash:
        return

    try:
        with open("hash_store.txt", "r") as f:
            for line in f:
                stored_path, stored_hash = line.strip().split("|")
                
                if stored_path == file_path:
                    if stored_hash == current_hash:
                        print(" File is unchanged")
                    else:
                        print(" File has been modified!")
                    return
        
        print("No stored hash found for this file ")

    except FileNotFoundError:
        print("No hash database found ")


# Example usage
file = input("Enter file path: ")

print("\n1. Store hash")
print("2. Check integrity")

choice = input("Choose option: ")

if choice == "1":
    hash_value = calculate_hash(file)
    if hash_value:
        save_hash(file, hash_value)
        print("Hash stored successfully ")

elif choice == "2":
    check_integrity(file)

else:
    print("Invalid choice ")
