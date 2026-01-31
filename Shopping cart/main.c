#include <stdio.h>
#include <string.h>

int main() {

    char item[50] = "";
    int quantity = 0;
    float price = 0.00;

    printf("What item would you like to purchase: ");
    fgets(item, sizeof(item), stdin);
    item[strlen(item) - 1] = '\0';

    printf("What is the price of this item?: ");
    scanf("%f", &price);

    printf("How many are you buying?: ");
    scanf("%d", &quantity);

    float total = price*quantity;

    printf("You bought %d %ss and your total is $%.2f", quantity, item, total);

    return 0;
}