#include<iostream>
using namespace std;
int main(){
    int number;
    cout<<"please enter number of towers: ";
    cin>>number;
    int towers[number];
    int signalPowers[number];
    for(int i = 0;i<number;++i){
        int input;
        cout<<"enter tower number "<<i+1<<": ";
        cin>>input;
        towers[i] = input;
    }
    for(int i = number-1;i >=0;--i){
        int counter = 1;
        for(int j = i-1;j >= 0;--j){
            if(towers[i] >= towers[j]){
                ++counter;
            }
            else{
                break;
            }
        }
        signalPowers[i] = counter;
    }
    for(int i = 0;i < number;++i){
        cout<<signalPowers[i]<<" ";
    }

}
