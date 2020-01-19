#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>



int main() 
{
    int a, b;
    scanf("%d\n%d", &a, &b);
    char arr[10][10]={"one","two","three","four","five","six","seven","eight","nine"};
    for(int x=a;x<=b;x++){
        if(x>9){
        if(x%2==0){
            printf("even\n");

        }
        else{
            printf("odd\n");
        }
        
    }
    else{
        for(int i=0;arr[x-1][i]!='\0';i++){
            printf("%c",arr[x-1][i]);

        }
        printf("\n");

        
    }

    }
    
   
  	// Complete the code.

    return 0;
}

