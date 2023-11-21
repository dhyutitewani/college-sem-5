#include <stdio.h>	
#include <string.h>

#define BITS 17
char data[100], concatdata[117], src_crc[17], dest_crc[17], frame[120], divident[18], divisor[18], res[17] = "0000000000000000";

void crc_cal(char *crc, char *input, int node) {
    for (int j = BITS; j <= strlen(input); j++) {
        if (divident[0] == '1') {
            for (int i = 1; i < BITS; i++)
                divident[i - 1] = (divident[i] != divisor[i]) ? '1' : '0';
        } else {
            for (int i = 1; i < BITS; i++)
                divident[i - 1] = divident[i];
        }

        divident[BITS - 1] = (node == 0) ? input[j] : frame[j];
    }

    divident[BITS] = '\0';
    printf("\ncrc is %s\n", divident);
    strcpy(crc, divident);
}

int main() {
    printf("enter the generator bits\n");
    gets(divisor);

    if (strlen(divisor) != BITS) {
        printf("please enter the generator length exactly 17 bits\n");
        return 0;
    }

    printf("\nAt src node:\nEnter the msg to be sent:");
    gets(data);

    strcpy(concatdata, data);
    strcat(concatdata, "0000000000000000");

    for (int i = 0; i < BITS; i++)
        divident[i] = concatdata[i];

    divident[BITS] = '\0';
    crc_cal(src_crc, concatdata, 0);

    printf("\ndata is:\t%s", data);
    printf("\nThe frame transmitted is:\t\n%s%s\n", data, src_crc);
    printf("\n\t\tSOURCE NODE TRANSMITTED THE FRAME---->");

    printf("\n\n\n\n\t\t\tAT DESTINATION NODE\nenter the received frame:\t");
    gets(frame);

    for (int i = 0; i < BITS; i++)
        divident[i] = frame[i];

    divident[BITS] = '\0';
    crc_cal(dest_crc, frame, 1);

    if (strcmp(dest_crc, res) == 0)
        printf("\nReceived frame is error-free.\n");
    else
        printf("\nReceived frame contains one or more errors.\n");

    return 1;
}

