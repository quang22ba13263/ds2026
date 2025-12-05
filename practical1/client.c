#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>

#define PORT 12345
#define BUFFER_SIZE 4096

void send_file(FILE *fp, int sockfd) {
    char data[BUFFER_SIZE] = {0};
    int n;

    
    while ((n = fread(data, 1, BUFFER_SIZE, fp)) > 0) {
        if (send(sockfd, data, n, 0) == -1) {
            perror("[-]Error in sending file.");
            exit(1);
        }
        bzero(data, BUFFER_SIZE);
    }
    printf("[+]File data sent successfully.\n");
}

int main() {
    int sock = 0;
    struct sockaddr_in serv_addr;
    FILE *fp;
    char *filename = "send_me.txt"; 

    
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("\n Socket creation error \n");
        return -1;
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);

    
    if(inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr)<=0) {
        printf("\nInvalid address/ Address not supported \n");
        return -1;
    }

    
    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        printf("\nConnection Failed \n");
        return -1;
    }
    printf("[+]Connected to Server.\n");

    
    fp = fopen(filename, "rb");
    if (fp == NULL) {
        perror("[-]Error in reading file.");
        return 1;
    }

    
    send_file(fp, sock);
    
    
    fclose(fp);
    close(sock);
    return 0;
}