#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/wait.h>
#include <signal.h>
#include <netdb.h>

#define CHARS "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

// Error function used for reporting issues
void error(const char *msg) {
  fprintf(stderr, "%s\n", msg);
  exit(1);
} 

// Set up the address struct for the server socket
void setupAddressStruct(struct sockaddr_in* address, 
                        int portNumber, char* hostname){
 
  // Clear out the address struct
  memset((char*) address, '\0', sizeof(*address)); 

  // The address should be network capable
  address->sin_family = AF_INET;
  // Store the port number
  address->sin_port = htons(portNumber);
  // Allow a client at any address to connect to this server
  struct hostent* hostInfo = gethostbyname(hostname);
  if (hostInfo == NULL) { 
    fprintf(stderr, "DEC_SERVER: ERROR, no such host\n"); 
    exit(1); 
  }
  memcpy((char*)&address->sin_addr.s_addr, hostInfo->h_addr_list[0], hostInfo->h_length);
}

void receiveText(int socket, char *buffer, int length) {
    int total = 0;
    int charsRead;

    while (total < length) {
      // Read the client's message from the socket
      charsRead = recv(socket, buffer + total, length - total, 0);

      if (charsRead < 0) {
        fprintf(stderr, "ERROR reading from socket");
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
        error("ERROR writing to socket");
      }
      total += charsWritten;
  }
}



void decrypt(char *cipher, char *keygen, char *plain){
    int cipherInd = 0;
    int keyInd = 0;
    int newInd = 0;
    for (int i = 0; i < strlen(cipher); i++){
        if (cipher[i] == ' '){
            cipherInd = 26;
        } else {
             cipherInd = cipher[i] - 'A';
        }

        if (keygen[i] == ' '){
            keyInd = 26;
        } else {
            keyInd = keygen[i] - 'A';
        }
        
        newInd = (cipherInd - keyInd + 27) % 27;

        if (newInd == 26){
            plain[i] = ' ';
        } else {
            plain[i] = 'A' + newInd;
        }
    }
    plain[strlen(cipher)] = '\n';
    plain[strlen(cipher) + 1] = '\0';
}

int main(int argc, char *argv[]){
  int connectionSocket, charsRead;
  char buffer[256];
  char response[10];
  struct sockaddr_in serverAddress, clientAddress;
  socklen_t sizeOfClientInfo = sizeof(clientAddress);

  // Check usage & args
  if (argc < 2) { 
    fprintf(stderr,"USAGE: %s port\n", argv[0]);
    exit(1); 
  } 


  pid_t pid = fork();

  if(pid < 0){
    error("fork() failed!");
  } 
  if (pid > 0) {
    exit(0);
  }

  setsid();
  
  // Create the socket that will listen for connections
  int listenSocket = socket(AF_INET, SOCK_STREAM, 0);
  if (listenSocket < 0) {
    error("ERROR opening socket");
  }

  int pos = 1;
  setsockopt(listenSocket, SOL_SOCKET, SO_REUSEADDR, &pos, sizeof(int));

  // Set up the address struct for the server socket
  setupAddressStruct(&serverAddress, atoi(argv[1]), "localhost");

  // Associate the socket to the port
  if (bind(listenSocket, 
          (struct sockaddr *)&serverAddress, 
          sizeof(serverAddress)) < 0){
    error("ERROR on binding");
  }

  // Start listening for connetions. Allow up to 5 connections to queue up
  listen(listenSocket, 5); 

  struct sigaction sa;
  sa.sa_handler = SIG_IGN;
  sigaction(SIGCHLD, &sa, 0);
  
  // Accept a connection, blocking if one is not available until one connects
  while(1){
    // Accept the connection request which creates a connection socket
    connectionSocket = accept(listenSocket, 
                (struct sockaddr *)&clientAddress, 
                &sizeOfClientInfo); 
    if (connectionSocket < 0){
      error("ERROR on accept");
    }

    pid_t childPid = fork ();
    if (childPid <0) {
      fprintf(stderr, "fork() failed!");
      close(connectionSocket);
      continue;
    } else if (childPid == 0) {
    close(listenSocket);

    receiveText(connectionSocket, response, 10);
    if (strcmp(response, "dec_client") != 0) {
      close(connectionSocket);
      exit(1);
    }
    sendText(connectionSocket, "dec_server", 10);

    int size;
    receiveText(connectionSocket, (char *)&size, sizeof(int));

    char *plain = malloc(size + 2);
    char *keygen = malloc(size + 1);
    char *cipher = malloc(size + 1);
    if (!plain || !keygen || !cipher) {
      error("Memory allocation failed!");
  }

    receiveText(connectionSocket, cipher, size);
    receiveText(connectionSocket, keygen, size);
    if (strlen(keygen) < strlen(cipher)) {
      fprintf(stderr, "Error: key is too short");
      close(connectionSocket);
      free(plain);
      free(keygen);
      free(cipher);
      exit(1);
    }

    decrypt(cipher, keygen, plain);
    sendText(connectionSocket, (char *)&size, sizeof(int));
    sendText(connectionSocket, plain, size + 1);

    free(plain);
    free(keygen);
    free(cipher);
    close(connectionSocket);
    exit(0);
    } else {
    close(connectionSocket);
    }
  }

  close(listenSocket); 
  return 0;
}


