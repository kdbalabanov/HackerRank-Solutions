#include <iostream>
#include <cstdio>
using namespace std;

int main() 
{
    int a, b;
    cin >> a >> b;
    string nums[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

    for (int i = a; i <= b; i++)
    {
        if (i > 9 && i % 2 == 0)
            cout << "even\n";
        else if (i > 9)
            cout << "odd\n";
        else
            cout << nums[i - 1] << "\n";
    }

    return 0;
}