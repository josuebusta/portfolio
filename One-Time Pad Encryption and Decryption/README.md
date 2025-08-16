# One-Time Pad Encryption & Decryption System

## Overview
This project implements a client-server system for encryption and decryption using a **One-Time Pad (OTP)-like cipher** with **socket-based inter-process communication (IPC)** and multi-processing.  
The system consists of **five C programs** that communicate via TCP sockets on `localhost`. The encryption scheme uses **modulo 27 arithmetic** over the alphabet `A–Z` plus the space character.

This assignment demonstrates:
- The **client-server communication model**
- Use of **Unix sockets** for IPC
- Concurrency with **multi-processing**
- Handling **network send/receive reliability**
- Implementation of a **one-time pad cipher**

---

## Programs

### 1. `enc_server`
- Runs as a daemon in the background.
- Listens on a specified port and spawns child processes to handle client requests.
- Accepts plaintext and key from `enc_client`, performs OTP encryption, and returns ciphertext.
- Supports up to **five concurrent connections**.
- Usage:
  ```bash
  ./enc_server <listening_port> &
  ```

---

### 2. `enc_client`
- Connects to `enc_server` and requests encryption.
- Takes in a **plaintext file**, **key file**, and the server’s **port**.
- Outputs ciphertext to `stdout` (can be redirected to a file).
- Performs input validation:
  - Rejects invalid characters (must be `A–Z` or space).
  - Exits with error if the key is shorter than the plaintext.
- Usage:
  ```bash
  ./enc_client <plaintext_file> <key_file> <port>
  ./enc_client myplaintext mykey 57171 > myciphertext
  ```

---

### 3. `dec_server`
- Mirrors `enc_server` but performs **decryption**.
- Returns plaintext to `dec_client`.
- Usage:
  ```bash
  ./dec_server <listening_port> &
  ```

---

### 4. `dec_client`
- Connects to `dec_server` to request decryption.
- Accepts **ciphertext file**, **key file**, and server **port**.
- Outputs plaintext to `stdout`.
- Must reject connections to `enc_server`.
- Usage:
  ```bash
  ./dec_client <ciphertext_file> <key_file> <port>
  ./dec_client ciphertext1 mykey 57172 > plaintext1
  ```

---

### 5. `keygen`
- Generates a random OTP key of a specified length.
- Allowed characters: `A–Z` and **space**.
- Always ends output with a newline (`\n`).
- Usage:
  ```bash
  ./keygen <keylength> > mykey
  ```

---

## Example Workflow

```bash
# Start servers
./enc_server 57171 &
./dec_server 57172 &

# Generate a key
./keygen 1024 > mykey

# Encrypt
./enc_client plaintext1 mykey 57171 > ciphertext1

# Decrypt (with correct key)
./dec_client ciphertext1 mykey 57172 > plaintext1_a

# Compare
cmp plaintext1 plaintext1_a   # returns 0 if identical
```

Error handling examples:
```bash
# Key too short
./enc_client plaintext1 shortkey 57171 > ciphertext1
Error: key 'shortkey' is too short
echo $?   # 1

# Wrong characters in input
./enc_client plaintext5 mykey 57171
enc_client error: input contains bad characters
echo $?   # 1

# Wrong server
./enc_client plaintext3 mykey 57172
Error: could not contact enc_server on port 57172
echo $?   # 2
```

---

## Compilation

You must compile all five programs. A provided `compileall` script builds them:

```bash
#!/bin/bash
gcc --std=gnu99 -o enc_server enc_server.c
gcc --std=gnu99 -o enc_client enc_client.c
gcc --std=gnu99 -o dec_server dec_server.c
gcc --std=gnu99 -o dec_client dec_client.c
gcc --std=gnu99 -o keygen keygen.c
```

Alternatively, you may use a `Makefile` that produces the same executables:
- `enc_server`
- `enc_client`
- `dec_server`
- `dec_client`
- `keygen`

Run:
```bash
./compileall
```
or
```bash
make
```

---

## Files Included
- `enc_server.c` – Encryption server
- `enc_client.c` – Encryption client
- `dec_server.c` – Decryption server
- `dec_client.c` – Decryption client
- `keygen.c` – Key generator
- `compileall` (or `Makefile`)
- `plaintext1` through `plaintext5` – Test files provided

---

## Exit Codes
- `0` – Success
- `1` – Input/key validation error
- `2` – Connection error (e.g., wrong server/port)

---

## Notes & Hints
- Only **A–Z** and **space** are valid in plaintext and key files.
- Always strip newlines before encrypting/decrypting, then append one at the end of output.
- Use `setsockopt()` with `SO_REUSEADDR` to avoid port binding issues.
- Implement **robust send/receive loops** (data may not be sent/received in one call).
- Limit send sizes (e.g., 1000 characters per transmission) to prevent broken transfers.

---

## Author
Created as part of **CS344: Operating Systems – Program 5** assignment.  
Implements socket-based OTP encryption/decryption with multi-processing.
