// QUESTION 2
// LIST THE MAXIMUM NUMBER OF PRIME NUMBERS IN 60'
// DONE IN C++ TO OPTIMIZE THE NUMBER OF PRIMES FOUND

#include <iostream>
#include <vector>
#include <time.h>

using namespace std;

vector<int> primes;

int crivo(int i, int len){
    time_t init = time(NULL);
    while(time(NULL) - init < 60){
        if(i == 2){
            cout << i << " ";
            primes.push_back(i);
            i++;
            continue;
        }
        for(int j = 0; j < primes.size(); j++){
            if(i % primes[j] == 0) break;
            if(primes[j]*primes[j] > i){
                cout << i << " ";
                primes.push_back(i);
                break;
            }
        }
        i++;
    }
    return primes.size();
}

int main()
{
    time_t init = time(NULL);
    crivo(2, 10e7);
    cout << "\n\nTotal de primos achados: " << primes.size() << endl;
    return 0;
}