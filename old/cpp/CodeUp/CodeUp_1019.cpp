#include <iostream>
using namespace std;

int main() {
  int year,mon,day;
  cin>>year;
  cin.ignore(256,'.');
  cin>>mon;
  cin.ignore(256,'.');
  cin>>day;
  //cout.width : 출력시 몇 자리로 출력할지
  //cout.fill() : 출력자리를 맞추고 남은 부분이 있다면 어떤 걸로 채울지
  cout.width(4);
  cout.fill('0');
  cout<<year<<'.';
  cout.width(2);
  cout.fill('0');
  cout<<mon<<'.';
  cout.width(2);
  cout.fill('0');
  cout<<day;
  
}
