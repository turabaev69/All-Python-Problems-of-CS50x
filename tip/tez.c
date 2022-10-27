#include <stdio.h>
#include <cs50.h>

int main(){
    int numbers[] ={1,2,45,8,7,9};
    int length = 6;

    for(int i = 0, s = length -1; i < s; i++)
    {
        int min_pos = i;
        for(int j = i + 1; j < length; j++){
            if (numbers[j] < numbers[min_pos]){
                min_pos = j;

        if(min_pos != i){
            int temp = numbers[i];
            numbers[i] = numbers[min_pos];
            numbers[min_pos] = temp;

        }
            }
        }

    }
    for(int i = 0; i < length; i++){
        printf("numbers[%d] = %d\n", i, numbers[i]);
    }

    return 0;
}