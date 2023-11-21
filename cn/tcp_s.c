#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/fcntl.h>
#include <netinet/in.h>
#include <stdlib.h>

// arguent count and argument vector
int main(int argc, char *argv[]) {
	
	// checks if the prog runs with required cli arg
	if (argc < 2) {
		fprintf(stderr, "\nno port\n");
		exit(1);
	}

	// socket creation
	int socketfd = socket(AF_INET, SOCK_STREAM, 0);
	if (socketfd < 0)
		perror("\nerror opening socket\n");
	
	// server address structure
	struct sockaddr_in seradd = {0}, cliadd = {0};
	seradd.sin_family = AF_INET;
	seradd.sin_addr.s_addr = htonl(INADDR_ANY);
	seradd.sin_port = htons(atoi(argv[1]));
	
	// bind the socket addr and port
	if (bind(socketfd, (struct sockaddr *)&seradd, sizeof(seradd)) < 0)
		perror("\nIP address can not bind\n");

	listen(socketfd, 5);
	printf("\nserver witing for client\n");

	// getting the data from the client
	while (1) {
		int newsocfd = accept(socketfd, (struct sockaddr *)&cliadd, &(socklen_t){sizeof(cliadd)});
		if (newsocfd < 0)
			perror("\nserver can not accept req\n");
		
		char buffer[4096];
		recv(newsocfd, buffer, sizeof(buffer), 0);

		int fd = open(buffer, O_RDONLY);
		if (fd < 0)
			perror("\nfile does not exist");

		ssize_t n;
		while ((n = read(fd, buffer, sizeof(buffer))) > 0)
			send(newsocfd, buffer, n, 0);

		printf("\nfile transfer complete\n");

		close(fd);
		close(newsocfd);
	}

	return 0;
}
