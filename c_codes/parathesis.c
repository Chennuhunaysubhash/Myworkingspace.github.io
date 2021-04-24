#include<stdio.h>  
#include<string.h>
int main()
{
	char para[100];
	int i,count=0,count1=0,len; 
	printf("enter the parathesis \n");
	scanf("%s",para);
	len=strlen(para);
	for(i=0;i<len;i++)
	{
		if(para[i]=='(')
		{
			count++;
		}
		else if(para[i]==')')  //main logic 
		{
			count1++;
		}
		else
		continue;
	}
	if(count==count1)
	{
		printf("parathesis is balanced");
	}
	else                       //checking condition
	{
		printf("parathesis is not balanced");
		
	}
	return 0;
}
