# FILE-INTEGRITY-CHECKER

*COMPANY* : CODTECH IT SOLUTIONS PRIVATE LIMITED

*NAME* : GNANAVI S

*INTERN ID* : CTIS6494

*DOMAIN* : CYBER SECURITY & ETHICAL HACKING

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTHOSH

##  Description

The File Integrity Checker is a Python-based cybersecurity tool developed to monitor, verify, and maintain the integrity of files by detecting any unauthorized or unintended modifications. In modern computing environments, ensuring the integrity of files is a critical aspect of system security, as even the smallest alteration in a file can indicate potential tampering, corruption, or malicious activity. This project focuses on addressing this concern by implementing a simple yet effective file monitoring mechanism using cryptographic hashing techniques.

At the core of this system is the concept of hashing, which involves generating a fixed-length unique value, known as a hash, from input data. The tool utilizes the SHA-256 (Secure Hash Algorithm 256-bit) provided by Python’s hashlib library to generate a hash value for a given file. SHA-256 is widely recognized for its strong collision resistance and sensitivity to input changes, meaning that even a minor modification in the file content results in a completely different hash value. This property makes it highly suitable for integrity verification purposes.

The application operates in two primary modes: storing the hash and checking file integrity. In the first mode, the user provides the path to a file, and the system calculates its SHA-256 hash. This hash is then stored in a local file (hash_store.txt), which acts as a reference database for future comparisons. In the second mode, the system recalculates the hash of the specified file and compares it with the previously stored hash value. If both values match, the file is considered unchanged and intact. However, if there is any mismatch, the system immediately flags the file as modified, indicating a potential integrity breach.

To ensure efficiency and reliability, the program reads files in chunks rather than loading the entire file into memory. This approach allows the tool to handle large files without performance issues or excessive memory consumption. Additionally, basic error handling mechanisms are implemented to manage scenarios such as missing files, incorrect file paths, or absence of stored hash data.

This project demonstrates the practical application of cryptographic principles in real-world cybersecurity scenarios. It highlights how hashing can be effectively used to safeguard data integrity and detect unauthorized changes in a system. While the current implementation provides a command-line interface for simplicity, it can be further enhanced by incorporating features such as real-time monitoring, support for multiple files, graphical user interfaces, and integration with alert systems.

Overall, the File Integrity Checker serves as a foundational tool for understanding file security mechanisms and emphasizes the importance of data integrity in maintaining a secure computing environment.
