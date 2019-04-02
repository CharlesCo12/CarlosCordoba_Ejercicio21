#include <iostream>
#include <random>
#include <stdlib.h>
#include <cmath>

int main(){
  int i;
  float r;
  float a=0;
  float b=0;
    
  srand48(42);

  for (i=0;i<1001;i++){  
    r = drand48()*2*3.14;
    a+=cos(r);
    b+=sin(r);    
    std::cout << a << " " << b << std::endl;
  }
  
  return 0;
}