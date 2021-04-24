#include<stdio.h>
int main()
{
	int n,i,j,temp,temp1;
	printf("enter the size of array");  // read the size of array
	scanf("%d",&n);
	int a[n];
	printf("enter the numbers into array");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);   //read the elements to the array
	}
	temp=0;
	for(i=0;i<n;i++)
	{
		if(temp<a[i])    //logic for 1st big number
		{
			temp=a[i];
			j=i;
		}
	}
	temp1=0;
	for(i=0;i<n;i++)
	{
		if(i==j)
		{
			i++;
			i--;
		}                //logic for 2nd big number
		else
		{
			if(temp1<a[i])
			{
				temp1=a[i];
			}
		}
	}
	printf("second big %d",temp1);
}
