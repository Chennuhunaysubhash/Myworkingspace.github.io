#include<stdio.h>
int main()
{
	int i,j,k,p,n;
	printf("pascal triangle logic in c programming\n");
	printf("\n enter the number of line \n");
	scanf("%d",&n);
	p=1;
	for(i=0;i<n;i++)  // for loop for row printing
	{
		for(j=30-2*i;j>0;j--)
		{
			printf(" ");   // for loop for space print
		}
		for(k=0;k<=i;k++)  // for loop for coloum printing
		{
			if((k==0) || (i==0))       //main logic
			p=1;
			else
			p=(p*(i-k+1))/k;   //main formala statement
			printf("%4d",p);
			
			
		}
		printf("\n"); // next line okr new line
	}
	return 0;
}
