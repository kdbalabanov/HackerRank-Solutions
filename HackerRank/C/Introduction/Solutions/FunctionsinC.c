#include <stdio.h>
/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

int max_of_four(a, b, c, d) {
    int max_one, max_two;
    return (max_one = a > b ? a : b) > (max_two = c > d ? c : d) ? max_one : max_two;
}