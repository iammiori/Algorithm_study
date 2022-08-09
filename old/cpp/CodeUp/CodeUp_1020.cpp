#include <iostream>
using namespace std;

int main() {
  int front,back;
  cin>>front;
  cin.ignore(256,'-');
  cin>>back;
  cout.width(6);
  cout.fill('0');
  cout<<front;
  cout.width(7);
  cout.fill('0');
  cout<<back;
  
}
