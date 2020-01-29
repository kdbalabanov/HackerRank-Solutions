#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    const int MAX_LENGTH = 100;    
    char ch;
    char s[MAX_LENGTH];
    char sen[MAX_LENGTH];

    scanf("%c%*c", &ch);
    scanf("%s%*c", &s);
    scanf("%[^\n]%*c", &sen);

    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s", sen);

    return 0;
}