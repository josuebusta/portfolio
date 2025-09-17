# One-Time Pad Encryption & Decryption System

An implementation of a client-server encryption system in C, showcasing socket-based inter-process communication, multi-processing, and cryptographic operations using a One-Time Pad (OTP)-like cipher with modulo 27 arithmetic.

## Table of Contents

- [Overview](#overview)
- [Example Output](#example-output)
- [Features](#features)
- [Data Structures](#data-structures)
- [Installation & Setup](#installation--setup)
- [Usage Examples](#usage-examples)
- [Testing](#testing)
- [Performance Analysis](#performance-analysis)
- [Learning Outcomes](#learning-outcomes)
- [References](#references)

## Overview

This project implements the following components:

- **Encryption Server**: Multi-process daemon handling encryption requests
- **Decryption Server**: Multi-process daemon handling decryption requests
- **Encryption Client**: Client application for requesting encryption services
- **Decryption Client**: Client application for requesting decryption services
- **Key Generator**: Utility for generating random OTP keys

The system uses TCP sockets for inter-process communication, implements robust error handling, and provides secure encryption/decryption using modulo 27 arithmetic over the alphabet A-Z plus space character.

## Example Output

### Server Startup

```
# Start encryption server on port 57171
./enc_server 57171 &

# Start decryption server on port 57172
./dec_server 57172 &
```

### Key Generation

```
# Generate 1024-character key
./keygen 1024 > mykey
# Output: Random string of A-Z and spaces, 1024 characters long
```

### Encryption Process

```
# Encrypt plaintext file
./enc_client plaintext1 mykey 57171 > ciphertext1
# Output: Encrypted text to stdout (redirected to file)
```

### Decryption Process

```
# Decrypt ciphertext file
./dec_client ciphertext1 mykey 57172 > plaintext1_decrypted
# Output: Decrypted text to stdout (redirected to file)
```

### Error Handling Examples

```
# Key too short
./enc_client plaintext1 shortkey 57171
Error: key is too short
echo $?   # Returns 1

# Invalid characters
./enc_client plaintext5 mykey 57171
enc_client error: input contains bad characters
echo $?   # Returns 1

# Wrong server connection
./enc_client plaintext3 mykey 57172
Error: could not contact enc_server on port 57172
echo $?   # Returns 2
```

## Features

### Encryption Server Features
- **Multi-Process Architecture**: Spawns child processes for concurrent connections
- **Daemon Mode**: Runs in background with proper process management
- **Connection Handling**: Supports up to 5 concurrent connections
- **Protocol Validation**: Verifies client identity before processing
- **Memory Management**: Dynamic allocation with proper cleanup
- **Error Handling**: Comprehensive error reporting and recovery

### Decryption Server Features
- **Mirror Functionality**: Identical architecture to encryption server
- **Decryption Logic**: Implements reverse modulo 27 arithmetic
- **Client Validation**: Ensures only decryption clients connect
- **Concurrent Processing**: Handles multiple decryption requests
- **Resource Management**: Efficient memory and socket handling

### Client Features
- **File I/O**: Reads plaintext/ciphertext and key files
- **Input Validation**: Checks for valid characters (A-Z and space)
- **Key Length Validation**: Ensures key is at least as long as text
- **Socket Communication**: Robust send/receive with error handling
- **Protocol Compliance**: Proper handshake with servers

### Key Generator Features
- **Random Generation**: Uses system time for seed
- **Character Set**: Generates A-Z and space characters
- **Length Control**: Accepts command-line length parameter
- **Output Format**: Always ends with newline character

### Advanced Features
- **Socket Reuse**: SO_REUSEADDR to prevent binding issues
- **Robust Communication**: Handles partial sends/receives
- **Process Management**: Proper daemon creation and child handling
- **Signal Handling**: SIGCHLD management for zombie prevention
- **Memory Safety**: Proper allocation and deallocation

## Data Structures

### Socket Structures
```c
struct sockaddr_in serverAddress, clientAddress;
socklen_t sizeOfClientInfo = sizeof(clientAddress);
```

### Process Management
```c
pid_t pid = fork();
pid_t childPid = fork();
```

### Signal Handling
```c
struct sigaction sa;
sa.sa_handler = SIG_IGN;
sigaction(SIGCHLD, &sa, 0);
```

### Key Methods

#### Encryption/Decryption Functions
- `encrypt(plain, keygen, cipher)`: Performs OTP encryption
- `decrypt(cipher, keygen, plain)`: Performs OTP decryption
- `validate(text, name)`: Validates input characters

#### Socket Communication
- `setupAddressStruct(address, port, hostname)`: Configures socket address
- `receiveText(socket, buffer, length)`: Robust text reception
- `sendText(socket, buffer, length)`: Robust text transmission

#### Process Management
- `fork()`: Creates child processes for handling connections
- `setsid()`: Creates new session for daemon
- `wait()`: Manages child process termination

## Installation & Setup

### Prerequisites
- C compiler (gcc)
- Unix-like operating system (Linux/macOS)
- Make utility (optional)

### Setup Instructions

1. **Clone or download** the project files
2. **Compile the programs**:
   ```bash
   # Using provided script
   ./compileall
   
   # Or using make
   make
   
   # Or manual compilation
   gcc --std=gnu99 -o enc_server enc_server.c
   gcc --std=gnu99 -o enc_client enc_client.c
   gcc --std=gnu99 -o dec_server dec_server.c
   gcc --std=gnu99 -o dec_client dec_client.c
   gcc --std=gnu99 -o keygen keygen.c
   ```

3. **Verify compilation**:
   ```bash
   ls -la enc_server enc_client dec_server dec_client keygen
   ```

## Usage Examples

### Basic Encryption Workflow

```bash
# Start servers
./enc_server 57171 &
./dec_server 57172 &

# Generate key
./keygen 1024 > mykey

# Encrypt file
./enc_client plaintext1 mykey 57171 > ciphertext1

# Decrypt file
./dec_client ciphertext1 mykey 57172 > plaintext1_decrypted

# Verify results
cmp plaintext1 plaintext1_decrypted
echo $?  # Should return 0 if identical
```

### Advanced Usage

```bash
# Multiple encryption operations
for i in {1..5}; do
    ./enc_client plaintext$i mykey 57171 > ciphertext$i
done

# Batch decryption
for i in {1..5}; do
    ./dec_client ciphertext$i mykey 57172 > plaintext${i}_decrypted
done

# Verify all files
for i in {1..5}; do
    cmp plaintext$i plaintext${i}_decrypted
    echo "File $i: $?"
done
```

### Error Testing

```bash
# Test key length validation
echo "SHORT" > shortkey
./enc_client plaintext1 shortkey 57171
# Expected: Error: key is too short

# Test character validation
echo "invalid@chars" > badtext
./enc_client badtext mykey 57171
# Expected: error: input contains bad characters

# Test server connection
./enc_client plaintext1 mykey 99999
# Expected: ERROR: Could not contact enc_server on port 99999
```

### Process Management

```bash
# Check running servers
ps aux | grep -E "(enc_server|dec_server)"

# Kill servers
pkill enc_server
pkill dec_server

# Check server ports
netstat -tlnp | grep -E "(57171|57172)"
```

## Testing

### Running Built-in Tests

The system includes comprehensive testing through provided plaintext files:

```bash
# Test with provided files
for i in {1..5}; do
    echo "Testing plaintext$i..."
    ./enc_client plaintext$i mykey 57171 > ciphertext$i
    ./dec_client ciphertext$i mykey 57172 > plaintext${i}_test
    cmp plaintext$i plaintext${i}_test
    echo "Result: $?"
done
```

### Test Coverage

The testing includes:

- **Basic Operations**: Encryption and decryption with various inputs
- **Edge Cases**: Empty files, single characters, maximum lengths
- **Error Handling**: Invalid characters, short keys, connection failures
- **Concurrency**: Multiple simultaneous connections
- **Protocol Validation**: Client-server handshake verification
- **Memory Management**: Proper allocation and cleanup

### Example Test Output

```
Testing plaintext1...
Result: 0
Testing plaintext2...
Result: 0
Testing plaintext3...
Result: 0
Testing plaintext4...
Result: 0
Testing plaintext5...
Result: 0
```

### Performance Testing

```bash
# Test with large files
./keygen 10000 > largekey
echo "A" | tr -d '\n' | head -c 10000 > largeplaintext
./enc_client largeplaintext largekey 57171 > largeciphertext
./dec_client largeciphertext largekey 57172 > largeplaintext_decrypted
cmp largeplaintext largeplaintext_decrypted
echo "Large file test: $?"
```

## Performance Analysis

### Time Complexity

| Operation | Time Complexity | Description |
|-----------|----------------|-------------|
| Encryption | O(n) | Linear with text length |
| Decryption | O(n) | Linear with text length |
| Key Generation | O(n) | Linear with key length |
| Socket I/O | O(n) | Linear with data size |
| Process Creation | O(1) | Constant time fork() |

### Space Complexity
- **Memory Usage**: O(n) where n is text length
- **Socket Buffers**: Fixed size buffers for communication
- **Process Overhead**: Minimal per connection
- **File I/O**: Stream-based, constant memory

### Network Performance
- **Connection Overhead**: TCP handshake per request
- **Data Transfer**: Efficient binary data transmission
- **Concurrency**: Up to 5 simultaneous connections
- **Error Recovery**: Robust handling of network issues

### System Resource Usage
- **CPU**: Minimal for encryption/decryption operations
- **Memory**: Efficient allocation with proper cleanup
- **File Descriptors**: One per connection plus server socket
- **Process Management**: Automatic cleanup of child processes

## Learning Outcomes

This project demonstrates:

- **Socket Programming**: TCP client-server communication
- **Multi-Processing**: Fork-based concurrency and daemon creation
- **Cryptography**: One-Time Pad implementation and modulo arithmetic
- **System Programming**: Process management and signal handling
- **Error Handling**: Robust error detection and recovery
- **Memory Management**: Dynamic allocation and proper cleanup
- **Network Protocols**: Custom application-level protocols
- **Unix Systems**: File I/O, process control, and system calls

## References

- [One-Time Pad - Wikipedia](https://en.wikipedia.org/wiki/One-time_pad)
- [Unix Process Management - GeeksforGeeks](https://www.geeksforgeeks.org/process-management-in-linux/)
- [TCP/IP Sockets in C - W. Richard Stevens](https://www.amazon.com/TCP-IP-Sockets-C-Second/dp/0123745403)

---

**Author**: Josue Bustamante  
**Course**: CS344 - Operating Systems  
**Institution**: Oregon State University  
**Date**: December 2023