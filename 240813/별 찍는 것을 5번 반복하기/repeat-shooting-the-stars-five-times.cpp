#include <iostream>
using namespace std;
#include <string>

string stars(int n){
    string str;
    str.resize(n, '*');
    return str;
}

int main() {
    for (int i = 0; i < 5; i++) {
        cout <<  stars(10) << '\n';
    }

    return 0;
}