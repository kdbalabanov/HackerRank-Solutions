#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string nums[10] = {"Greater than 9", "one", "two", "three", "four",
                       "five", "six", "seven", "eight", "nine"};

    // Write Your Code Here
    if (n > 9)
        cout << nums[0];
    else
        cout << nums[n];

    return 0;
}
