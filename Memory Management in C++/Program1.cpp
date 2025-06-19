/*
#include <iostream>
using namespace std;

class Vector
{
    int* p;
    int sz;
public:
    int* begin()
    {
        return p;
    }
    int* end()
    {
        return p + sz;
    }

};
void display(int* F, int* L)
{
    for( ; F!= L; ++F)
        cout<<*F<<"t";
    cout<<endl;
}
int main()
{
    int arr[] = { 10,20, 30, 40, 50, 60, 70,80, 90, 100 };
    Vector  v1,         // size is 0,
            v2(10),     // size is 10, all vales are 0
            v3(10,5),    // size is 10, all vales are 5
            v4(10,arr);
            
    display(v1.end(), v1.end());
    display(v2.end(), v2.end());
    display(v3.end(), v3.end());
    display(v4.end(), v4.end());

return 0;
}
*/

//Edit the following code so it works.

//Working Code:
#include <iostream>
#include <vector>
using namespace std;

class Vector {
  int* p;
  int sz;
public:
  int* begin(){
      return p;
  }
  int* end(){
      return p +sz;
  }
  Vector(): sz(0), p(NULL) {}
  
  Vector(int _sz): sz(_sz) {
      p = new int[sz];
      for(int i=0;i<sz;++i){
          p[i] = 0;
      }
  }
  
  Vector(int _sz, int fill): sz(_sz){
      p = new int[sz];
      for(int i=0;i<sz;++i){
          p[i] = fill;
      }
  }
  
  Vector(int _sz, int* ptr): sz(_sz){
      p = new int[sz];
      for(int i=0; i<sz;++i){
          p[i] = ptr[i];
      }
  }
  
  ~Vector(){
      delete[] x;
      sz = 0;
      cout<<"Before cleaning p : "<<p<<endl;
      p = NULL;
      cout<<"After cleaning p : "<<p<<endl;
  }
};

void display(int* F, int* L)
{
    for(;F!=L;++F)
        cout<<*F<<"\t";
    cout<<endl;
}

int main() {
    int arr[] = {10,20,30,40,50,60,70,80,90,100};
    Vector v1, //size 0
           v2(10), //size is 10, all values are 0
           v3(10,5), //size is 10, all values are 5
           v4(10,arr); //store values of the arr
    display(v1.begin(), v1.end());
    display(v2.begin(), v2.end());
    display(v3.begin(), v3.end());
    display(v4.begin(), v4.end());
    return 0;
}
