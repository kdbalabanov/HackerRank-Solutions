#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() 
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, q;
    cin >> n >> q;
    vector<vector<int>> vectors;
    
    for (int a = 0; a < n; a++)
    {
        int size;
        cin >> size;
        vector<int> v;

        for (int b = 0; b < size; b++)
        {
            int input;
            cin >> input;
            v.push_back(input);
        }

        vectors.push_back(v);
    }

    for (int j = 0; j < q; j++)
    {
        int i;
        int k;
        cin >> i >> k;
        cout << vectors.at(i).at(k) << endl;
    }

    return 0;
}