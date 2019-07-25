#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) 
{
    stringstream ss(str);
    vector<int> ints;
    int i;
    char c;

    while (ss >> i)
    {
        ints.push_back(i);
        ss >> c;
    }

    return ints;
}

int main() 
{
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);

    for (int i = 0; i < integers.size(); i++) 
    {
        cout << integers[i] << "\n";
    }

    return 0;
}