#include <bits/stdc++.h>

using namespace std;



int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string arr[9]={"one","two","three","four","five","six","seven","eight","nine"};
    if(n>=1&&n<=9)
    cout<<arr[n-1];
    else
    cout<<"Greater than 9";     
    return 0;
}
