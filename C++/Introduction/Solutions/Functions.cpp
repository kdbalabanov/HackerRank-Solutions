#include <algorithm>
#include <cstdio>
#include <iostream>
using namespace std;

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/

const int size = 4;

int max_of_four(int a, int b, int c, int d)
{
    int nums[size] = {a, b, c, d};
    sort(nums, nums + size);
    return nums[size - 1];
}

int main() 
{
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}
