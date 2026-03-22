# FILE-INTEGRITY-CHECKER

*COMPANY* : CODTECH IT SOLUTIONS PRIVATE LIMITED

*NAME* : GNANAVI S

*INTERN ID* : CTIS6494

*DOMAIN* : CYBER SECURITY & ETHICAL HACKING

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTHOSH

##  Description
In cybersecurity, one of the most important things to monitor is whether files have been tampered with. Attackers who gain access to a system often modify critical files — such as configuration files, logs, or executables — to maintain access or cover their tracks. A file integrity checker is a tool that detects these kinds of unauthorized changes by comparing the current state of a file against a previously stored record of what it looked like.
This project was built as part of a cybersecurity internship to demonstrate how file integrity monitoring works at a basic level. The tool uses a cryptographic hashing algorithm called SHA-256 to generate a unique fingerprint for any given file. This fingerprint, called a hash, is a fixed-length string that represents the exact contents of the file. If even a single character in the file is changed, the hash will be completely different. By storing a file's hash and comparing it later, the tool can reliably detect whether a file has been modified since it was last checked.

## How It Works

## Calculating the Hash
When the user selects a file, the tool reads it in small chunks of 4096 bytes at a time and feeds each chunk into the SHA-256 hashing function. Reading in chunks instead of loading the entire file at once makes the tool memory-efficient and capable of handling large files without any issues. Once all the chunks are processed, SHA-256 produces a 64-character hexadecimal string that uniquely represents the file's contents at that point in time.
## Storing the Hash
When the user chooses to store a file's hash, the tool saves the file path and its corresponding SHA-256 hash into a local text file called hash_store.txt. Each entry is stored on a new line in the format filepath|hash, creating a simple database of file fingerprints that can be referenced later for integrity checks.
## hecking Integrity
When the user wants to verify a file, the tool calculates the file's current SHA-256 hash and then looks up the stored hash for that file in hash_store.txt. If the two hashes match, the file is confirmed to be unchanged. If they are different, the tool immediately reports that the file has been modified. If no stored hash is found for the file, the tool notifies the user that there is no baseline to compare against.
## Why SHA-256?
SHA-256 is a one-way cryptographic hash function, meaning it is practically impossible to reverse or fake. Two different files will never produce the same hash, and even the tiniest change to a file will produce a completely different hash. This makes it an ideal tool for detecting tampering, which is why SHA-256 is widely used in digital forensics, software verification, and security monitoring systems like real-world SIEM tools.
