#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>

int main(int argc, char *argv[]) {
    if (argc < 4) {
        fprintf(stderr, "usage %s serverip filename port", argv[0]);
        exit(0);
    }

    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) perror("\n Error in creating socket.\n");

    struct sockaddr_in seradd = {0};
    seradd.sin_family = AF_INET;
    seradd.sin_addr.s_addr = inet_addr(argv[1]);
    seradd.sin_port = htons(atoi(argv[3]));

    if (connect(sockfd, (struct sockaddr *)&seradd, sizeof(seradd)) < 0)
        perror("\n Error in connection setup \n");

    write(sockfd, argv[2], strlen(argv[2]) + 1);

    char buffer[4096];
    bzero(buffer, sizeof(buffer));
    int n = read(sockfd, buffer, sizeof(buffer));

    if (n <= 0) {
        perror("\n File not found");
        exit(0);
    }

    write(1, buffer, n);

    return 0;
}

