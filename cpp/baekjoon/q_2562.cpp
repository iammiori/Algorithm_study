#include <iostream>
using namespace std;

int main()
{
    int i = 0;
    int max = 0;
    int array[9];
    
    for(int k = 0; k<9; k++)
    {
        cin >> array[k];
        if(max < array[k])
        {
            max = array[k];
            i = k+1;
        }
    }
    
    cout << max << '\n' << i;
    
    return 0;
}