#!/usr/bin/env python3

'''     TODO:
-CORRECT 'Error with format dynamic_n: Unknown ciphertext format name requested', possibly an issue with john itself.
-ADD try/except block to prevent the user from mistyping something and having to reset the script. 
    mostly just need to add this because I mistype crap all the time and hate having to retype extra stuff.
-ADD greater functionality at the initial file input, as it stands the user can easily mistype and screw up the 
    input causing them to have to redo the entire thing.
-RECONFIGURE print statements, as they stand they're easy to read but something about their presentation just throws me off.
-OPTIMIZE how the script runs against the format types, even now just running 2 hash files with only a few hashes each and
    a custom wordlist that is very small it takes forever a day to run through all the format types simply because I don't need
    all the format types every time. Potentially need to call another program first, or develop something in python to ID the
    hashes in the file and pass that along to main so it selects only the required format types.
-ADD more wordlists to the wordlist selection tab, this will require me to package these custom wordlists with the script, 
    for right now its assumed that the user will have the rockyou.txt wordlist already on their system in the /usr/share/wordlists
    directory.

John the Ripper automation script that gives the user the ability to run multiple hash files at once while also
giving the user the freedom to utilize the default John wordlist, the rockyou wordlist (must be located in the /usr/share/wordlists directory),
or another they can provide from input. This program does accept *nix style globbing as well as absolute paths to either hash lists or wordlists.

Rich Smith (richrsmith@proton.me)
first written Dec 2024
'''

import os
import subprocess
import glob

print("Enter the hash files you wish to use separted by a space: ")
hash_files = input().split(" ")

print("""What wordlist would you like to use?
    1. John the Ripper Default wordlist
    2. Rockyou wordlist
    3. Other (from input)
    """)
choice = int(input())
wordlist = None
if choice == 1:
    wordlist = None
elif choice == 2:
    wordlist = "/usr/share/wordlists/rockyou.txt"
elif choice == 3:
    wordlist = input("\nEnter the wordlist you'd like to use: ").strip()
else:
    print("Invalid choice")


hash_paths = [os.path.expanduser(path.strip()) for path in hash_files]
target_files = []

for hash_path in hash_paths:
    target_files.extend(glob.glob(hash_path))

if not target_files:
    print("Target does not exist")
    exit(1)

format_types = [
    "descrypt", "bsdicrypt", "md5crypt", "md5crypt-long", "bcrypt", "scrypt", "LM", "AFS",
    "tripcode", "AndroidBackup", "adxcrypt", "agilekeychain", "aix-ssha1", "aix-ssha256",
    "aix-ssha512", "andOTP", "ansible", "argon2", "as400-des", "as400-ssha1", "asa-md5",
    "AxCrypt", "AzureAD", "BestCrypt", "BestCryptVE4", "bfegg", "Bitcoin", "BitLocker",
    "bitshares", "Bitwarden", "BKS", "Blackberry-ES10", "WoWSRP", "Blockchain", "chap",
    "Clipperz", "cloudkeychain", "dynamic_n", "cq", "CRC32", "cryptoSafe", "sha1crypt",
    "sha256crypt", "sha512crypt", "Citrix_NS10", "dahua", "dashlane", "diskcryptor",
    "Django", "django-scrypt", "dmd5", "dmg", "dominosec", "dominosec8", "DPAPImk",
    "dragonfly3-32", "dragonfly3-64", "dragonfly4-32", "dragonfly4-64", "Drupal7",
    "eCryptfs", "eigrp", "electrum", "EncFS", "enpass", "EPI", "EPiServer", "ethereum",
    "fde", "Fortigate256", "Fortigate", "FormSpring", "FVDE", "geli", "gost", "gpg",
    "HAVAL-128-4", "HAVAL-256-3", "hdaa", "hMailServer", "hsrp", "IKE", "ipb2",
    "itunes-backup", "iwork", "KeePass", "keychain", "keyring", "keystore",
    "known_hosts", "krb4", "krb5", "krb5asrep", "krb5pa-sha1", "krb5tgs", "krb5-17",
    "krb5-18", "krb5-3", "kwallet", "lp", "lpcli", "leet", "lotus5", "lotus85", "LUKS",
    "MD2", "mdc2", "MediaWiki", "monero", "money", "MongoDB", "scram", "Mozilla",
    "mscash", "mscash2", "MSCHAPv2", "mschapv2-naive", "krb5pa-md5", "mssql",
    "mssql05", "mssql12", "multibit", "mysqlna", "mysql-sha1", "mysql", "net-ah",
    "nethalflm", "netlm", "netlmv2", "net-md5", "netntlmv2", "netntlm", "netntlm-naive",
    "net-sha1", "nk", "notes", "md5ns", "nsec3", "NT", "o10glogon", "o3logon",
    "o5logon", "ODF", "Office", "oldoffice", "OpenBSD-SoftRAID", "openssl-enc",
    "oracle", "oracle11", "Oracle12C", "osc", "ospf", "Padlock", "Palshop", "Panama",
    "PBKDF2-HMAC-MD4", "PBKDF2-HMAC-MD5", "PBKDF2-HMAC-SHA1", "PBKDF2-HMAC-SHA256",
    "PBKDF2-HMAC-SHA512", "PDF", "PEM", "pfx", "pgpdisk", "pgpsda", "pgpwde", "phpass",
    "PHPS", "PHPS2", "pix-md5", "PKZIP", "po", "postgres", "PST", "PuTTY", "pwsafe",
    "qnx", "RACF", "RACF-KDFAES", "radius", "RAdmin", "RAKP", "rar", "RAR5",
    "Raw-SHA512", "Raw-Blake2", "Raw-Keccak", "Raw-Keccak-256", "Raw-MD4", "Raw-MD5",
    "Raw-MD5u", "Raw-SHA1", "Raw-SHA1-AxCrypt", "Raw-SHA1-Linkedin", "Raw-SHA224",
    "Raw-SHA256", "Raw-SHA3", "Raw-SHA384", "restic", "ripemd-128", "ripemd-160",
    "rsvp", "RVARY", "Siemens-S7", "Salted-SHA1", "SSHA512", "sapb", "sapg", "saph",
    "sappse", "securezip", "7z", "Signal", "SIP", "skein-256", "skein-512", "skey",
    "SL3", "Snefru-128", "Snefru-256", "LastPass", "SNMP", "solarwinds", "SSH",
    "sspr", "Stribog-256", "Stribog-512", "STRIP", "SunMD5", "SybaseASE",
    "Sybase-PROP", "tacacs-plus", "tcp-md5", "telegram", "tezos", "Tiger",
    "tc_aes_xts", "tc_ripemd160", "tc_ripemd160boot", "tc_sha512", "tc_whirlpool",
    "vdi", "OpenVMS", "vmx", "VNC", "vtp", "wbb3", "whirlpool", "whirlpool0",
    "whirlpool1", "wpapsk", "wpapsk-pmk", "xmpp-scram", "xsha", "xsha512", "zed",
    "ZIP", "ZipMonster", "plaintext", "has-160", "HMAC-MD5", "HMAC-SHA1",
    "HMAC-SHA224", "HMAC-SHA256", "HMAC-SHA384", "HMAC-SHA512", "dummy", "crypt"
]

for target_file in target_files:
    print(f"\nWorking on {target_file} currently")
    for formats in format_types:
        command = ["john", f"--format={formats}"]
        if wordlist:
            command.extend([f"--wordlist={wordlist}"])
        command.extend([target_file])
        john_process = subprocess.run(command, text=True, capture_output=True)

        # Print potential errors but continue the loop
        if john_process.returncode != 0 and "No password hashes left" not in john_process.stdout:
            print(f"Error with format {formats}: {john_process.stderr}")
            continue

        output = john_process.stdout.strip()

for target_file in target_files:
    john_output = subprocess.run(["john", "--show", target_file], text=True, capture_output=True)
    print("Final cracked hashes:")
    print(john_output.stdout)
