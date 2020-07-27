#include<iostream>
using namespace std;
void selectionSort(int array[],int size){
    for(int i = 0;i<size;++i){
        for(int j = i+1;j<size;++j){
            if(array[i] > array[j]){
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }
}
int main(){
    int n,k;
    cout<<"enter n: ";
    cin>>n;
    cout<<"enter k: ";
    cin>>k;
    int fakeArray[n];
    int finalArray[k];
    int myArray[n][3];
    for(int j = 0;j < n;++j){
        cout<<"enter a"<<j<<": ";
        int a;
        cin>>a;
        myArray[j][0] = a;
        cout<<"enter b"<<j<<": ";
        int b;
        cin>>b;
        myArray[j][1] = b;
        cout<<"enter c"<<j<<": ";
        int c;
        cin>>c;
        myArray[j][2] = c;
    }
    for(int t = 0;t < k;++t){
        for(int j = 0;j < n;++j){
            fakeArray[j] = (myArray[j][0]+t)%k+(myArray[j][1]+t)%k+(myArray[j][2]+t)%k;
        }
        selectionSort(fakeArray,n);
        finalArray[t] = fakeArray[n-1];
    }
    selectionSort(finalArray,k);
    for(int p = 0;p < k;++p){
        cout<<finalArray[p]<<" ";
    }
    cout<<"\nMinimum: "<<finalArray[0];
}
