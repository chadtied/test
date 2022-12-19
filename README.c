#include<iostream>
#include<map>
#include<vector>

using namespace std;
int main(){

map<char, vector<int>> azmap;
char c;
for (c='a'; c<='z'; c++){
    int now = (int)c - 96;
    vector<int> vect;
    for(int i = 0; i < now; i++){
        vect.push_back(i);
    }
    azmap[c] = vect;
}
int input, mode= 0, limit;
char alpha;
while(cin>> alpha>>  mode>> input){
    if(mode== 0){
        int limit= (int)alpha- 96;
        if(input>= limit)
            return 0;
        cout<< azmap[alpha][input]<< " ";
     } 
    else if(mode== 1){
         int len= azmap[alpha].size()- 1;
         if(input> len)
            return 0;
            
         cout<< azmap[alpha][len- input]<< " ";
     }
    else if(mode== 2){
        int count= -1;
        input-= 1;
        for(int i= 0; i< azmap[alpha].size(); i++){
         if(i%2== 0){
             count++;
         }
         if(count== input){
             cout<< azmap[alpha][i]<< " ";
             break;
         }
         if(i== azmap[alpha].size()- 1)
            return 0;
        }
    }
}
return 0;
}
