#include <stdio.h>
#include <math.h>

int main() {

    float r;
    float area;
    float circum;
    float surfacearea;
    float volume;

    printf("Enter the radius: ");
    scanf("%f", &r);

    area = 3.1415926 * pow(r, 2);
    circum = 2*3.1415926*r;
    surfacearea = 4*3.1415926*pow(r,2);
    volume = (float) 4/3 * 3.1415926 * pow(r, 3);

    printf("The area is %.2f\n", area);
    printf("The circumference is %.2f\n", circum);
    printf("The surface area is %.2f\n", surfacearea);
    printf("The volume is %.2f", volume);


    return 0;
}