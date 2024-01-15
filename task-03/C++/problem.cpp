#include <iostream>
using namespace std;

bool is_prime(int n){

    if (n<2){
       return false; 
    }

for (int i=2; i*i<=n; i++){
    if (n%i == 0){
        return false;
    }
}
return true;
}

int main(){
int N;

    
    cout<<"Enter a number:"; 
cin >> N ;
    for ( int i=2; i<=N; i++){
        if (is_prime(i)){
           cout << i << " ";
          
    }
    } 

         cout << "\n" ;
    return 0; 
}