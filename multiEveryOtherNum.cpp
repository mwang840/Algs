#include <iostream>
using namespace std;


int multiEveryNum(int value[], int size){
    int multiplier = 1;

    for(int i = 0; i <= size; i+=2){
        multiplier = multiplier * value[i];
    }
    return multiplier;
}


int main(){
    int evens[] = {2, 4, 6, 8, 10};
    int odds[] = {1, 3, 5};
    std::cout << multiEveryNum(evens, 5);
    std::cout << multiEveryNum(odds, 3);
    return 0;
}