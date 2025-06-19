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
      return p + sz;
  }
  
  Vector(): sz(0), p(NULL) {}
  
  Vector(Vector &obj): sz(obj.sz){
    p = new int[sz];
    for(int i=0;i<sz;++i){
        p[i] = obj.p[i];
    }
  }
  
  Vector(int _sz): sz(_sz) {
      p = new int[sz];
      for(int i=0;i<sz;++i){
          p[i] = 0;
      }
  }
  
  Vector& operator =(Vector &obj){
      sz = obj.sz;
      p = new int[sz];
      for(int i=0;i<sz;++i){
          p[i] = obj.p[i];
      }
      return *this;
  }
  
  Vector(int _sz, int fill=0): sz(_sz){
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
      cout<<"Address of p: "<<p<<endl;
      delete[] p;
      sz = 0;
      p = NULL;
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
           v4(10,arr); //size is 10, store values of the arr
           v5(v4);
    v1 = v5;
    display(v1.begin(), v1.end());
    display(v2.begin(), v2.end());
    display(v3.begin(), v3.end());
    display(v4.begin(), v4.end());
    display(v5.begin(), v5.end());
    return 0;
}

//Check for errors. Understand the code accordingly.
