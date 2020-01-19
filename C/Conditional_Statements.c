#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>





int main()
{
    char arr[10][10]={"one","two","three","four","five","six","seven","eight","nine"};
    int x;
    scanf("%d",&x);
    if(x>9){
        printf("Greater than 9");
    }
    else{
        for(int i=0;arr[x-1][i]!='\0';i++){
            printf("%c",arr[x-1][i]);

        }

        
    }


    return 0;
}

