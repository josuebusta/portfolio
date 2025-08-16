#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>  // ssize_t
#include <sys/socket.h> // send(),recv()
#include <netdb.h>      // gethostbyname()


/**
* Client code
* 1. Create a socket and connect to the server specified in the command arugments.
* 2. Prompt the user for input and send that input as a message to the server.
* 3. Print the message received from the server and exit the program.
*/

// Error function used for reporting issues
void error(const char *msg, int code) { 
  fprintf(stderr, "%s\n", msg); 
  exit(code); 
} 

// Set up the address struct
void setupAddressStruct(struct sockaddr_in* address, 
                        int portNumber, 
                        char* hostname){
 
  // Clear out the address struct
  memset((char*) address, '\0', sizeof(*address)); 

  // The address should be network capable
  address->sin_family = AF_INET;
  address->sin_port = htons(portNumber);

  // Get the DNS entry for this host name
  struct hostent* hostInfo = gethostbyname(hostname); 
  if (hostInfo == NULL) { 
    fprintf(stderr, "CLIENT: ERROR, no such host\n"); 
    exit(1); 
  }
  // Copy the first IP address from the DNS entry to sin_addr.s_addr
  memcpy((char*) &address->sin_addr.s_addr, 
        hostInfo->h_addr_list[0],
        hostInfo->h_length);
}

void receiveText(int socket, char *buffer, int length) {
  int total = 0;
  int charsRead;
  while(total < length) {
    // Read data from the socket, leaving \0 at end
    charsRead = recv(socket, buffer + total, length - total, 0);
    if (charsRead < 0) {
      fprintf(stderr, "ERROR reading from socket");
      exit(1);
    } else if (charsRead == 0) {
        break;
    }
    total += charsRead;
  }
  buffer[total] = '\0';
}

void sendText(int socket, char *buffer, int length) {
  int total = 0;
  int charsWritten;
  
  while (total < length) {
      // Write to the server
      charsWritten = send(socket, buffer + total, length - total, 0);
      if (charsWritten < 0) {
        fprintf(stderr, "ERROR writing to socket");
      } else if (charsWritten == 0) {
        break;
      }
      total += charsWritten;
  }
}

void validate(const char *text, const char *name) {
  for (int i = 0; i <strlen(text); i++) {
    if ((text[i] < 'A' || text[i] > 'Z') && text[i] != ' ') {
      fprintf(stderr, "ERROR: contains invalid characters\n");
      exit(1);
    }
  }
}

int main(int argc, char *argv[]) {
  int socketFD;
  struct sockaddr_in serverAddress;
  char plain[100000];
  char keygen[100000];
  char cipher[100000];
  // Check usage & args
  if (argc < 4) { 
    fprintf(stderr,"USAGE: %s plaintext key port\n", argv[0]); 
    exit(1); 
  } 

  FILE *file = fopen(argv[1], "r");
  if (!file) {
    fprintf(stderr, "ERROR: Unable to open file %s\n", argv[1]);
    exit(1);
  }
  fgets(cipher, sizeof(cipher), file);
  cipher[strcspn(cipher, "\n")] = '\0';
  fclose(file);

  file = fopen(argv[2], "r");
  if (!file) {
    fprintf(stderr, "ERROR: Unable to open file %s\n", argv[1]);
    exit(1);
  }
  fgets(keygen, sizeof(keygen), file);
  keygen[strcspn(keygen, "\n")] = '\0';
  fclose(file);

  validate(cipher, argv[1]);
  validate(keygen, argv[2]);

  int cipherSize = strlen(cipher);
  int keygenSize = strlen(keygen);

  if (keygenSize < cipherSize) {
    fprintf(stderr, "Error: key is too short\n");
    exit(1);
  }
  
  // Create a socket
  socketFD = socket(AF_INET, SOCK_STREAM, 0); 
  if (socketFD < 0){
    fprintf(stderr, "ERROR creating socket\n");
    exit(2);
  }

   // Set up the server address struct
  setupAddressStruct(&serverAddress, atoi(argv[3]), "localhost");

  // Connect to server
  if (connect(socketFD, (struct sockaddr*)&serverAddress, sizeof(serverAddress)) < 0){
    fprintf(stderr, "ERROR: Could not connect to dec_server on port %s\n", argv[3]);
    exit(2);
  }

  sendText(socketFD, "dec_client", 10);
  char response[11];
  receiveText(socketFD, response, 10);

  if (strcmp(response, "dec_server") != 0) {
    fprintf(stderr, "ERROR: Not connecting to dec_server on port %s\n", argv[3]);
    close(socketFD);
    exit(2);
  }
  sendText(socketFD, (char *)&cipherSize, sizeof(int));
  sendText(socketFD, cipher, cipherSize);
  sendText(socketFD, keygen, cipherSize);
  receiveText(socketFD, (char *)&cipherSize, sizeof(int));
  receiveText(socketFD, plain, cipherSize);
  printf("%s\n", plain);
  
  // Close the socket
  close(socketFD); 
  return 0;
}