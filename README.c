# test

#include<stdio.h>
int main()
{
        int list[26][2],wordcount=0,count=0,length=0,ptrcount=0,wordpoint=0,standard=0,flag=0,debug=0;
        int *ptr[26];
        char word[26],input;
        while((input = getchar()) != EOF){
                    if(input=='('){
                            list[count][0]=1;
                            list[count][1]=0;
                            ptr[ptrcount]= list[count];
                            standard=ptrcount;
                            ptrcount++;
                            count++;
                            debug=1;
                    }
                    else if(input==')'){
                            list[count][0]=2;
                            list[count][1]=0;
                            if(debug==1&&ptr[standard][0]==1){
                                if(ptr[standard][1]!=1){
                                    list[count][1]=1;
                                    ptr[standard][1]=1;
                                    if(standard>0)
                                        standard--;
                                }
                            }
                            count++;
                    }
                    else{
                            list[count][0]=3;
                            list[count][1]=1;
                            word[wordcount]=input;
                            wordcount++;
                            count++;
                    }
                    length++;
        }
        for(int point=0;point<length;point++){
                if(list[point][1]==1){
                        flag=1;
                        if(list[point][0]==1)
                                printf("(");
                        else if(list[point][0]==2)
                                printf(")");
                        else{
                                printf("%c", word[wordpoint]);
                                wordpoint++;
                        }

                }
        }
        if(flag==0)
                printf('\n');
}
