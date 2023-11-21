#include <stdio.h>

#define max_nodes 20
#define infinite 99

struct routingtable {
	int dist[max_nodes], nextnode[max_nodes];
} table[max_nodes];

int cost[max_nodes][max_nodes], n;

void distvector() {
int i, j, k, count;

	 // initialize dis vector and next node
	for (i = 0; i < n; ++i)
		for (j = 0; j < n; ++j)
			table[i].dist[j] = cost[i][j], table[i].nextnode[j] = j; // set next nodes to the destination nodes

	
	// checking for the shortest path by applying the algorithm
	do {
		count = 0;
		for (i = 0; i < n; ++i)
			for (j = 0; j < n; ++j)
				for (k = 0; k < n; ++k)
					if (table[i].dist[j] > cost[i][k] + table[k].dist[j]) {
						table[i].dist[j] = table[i].dist[k] + table[k].dist[j];
						table[i].nextnode[j] = k;
						count++;
					}
	} while (count != 0);
}

// main function
int main() {
	// we have to enter the nodes and the matrix
	int i, j;

	printf("\nenter the nmber of vertices:");
	scanf("%d", &n);

	printf("\nenter the cost matrix\n");
	for (i = 0; i < n; ++i)
		for (j = 0; j < n; ++j)
			scanf("%d", &cost[i][j]);

	distvector();
	
	// sate your current shortest route and the values for it
	for (i = 0; i < n; ++i) {
		printf("\nstate value for route %c", i + 'A');
		printf("\ndestnode\tnextnode\tdistance\n");
		for (j = 0; j < n; ++j)
			printf("%c\t\t%c\t\t%d\n", j + 'A', table[i].nextnode[j] + 'A', (table[i].dist[j] == infinite) ? -1 : table[i].dist[j]);
	}

	return 0;

}
