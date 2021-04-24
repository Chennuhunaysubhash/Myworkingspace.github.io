#include<stdio.h>
int main()     //delhi pollution control mission 
{
	int num,sum=0,sum1=0,sum2=0,count,c;
		
	printf("------------------------------------------\n");
	printf("enter the condition are even(2) or odd(1)\n"); 
	scanf("%d",&count);  
	printf("enter the bike or car number\n");
	scanf("%d",&num); //read the bike or car number
	if(count==2 || count==1)
	{
		if(count==2)
		{
			printf("todays condition is even number only......\n\n"); // condition for even or odd patter
		}
		else
		{
			printf("todays condition is odd number only......\n\n");
		}
			while(num>0)
	{
		sum=sum+num%10;
		num=num/10;
	}
	if(sum>9)
   {
		while(sum>0)
		{
			sum1=sum1+sum%10;
			sum=sum/10;
		}
		if(sum1>9)
		{
	 	 while(sum1>0)                   //main logic 
	   	{
			sum2=sum2+sum1%10;
			sum1=sum1/10;
		}
		if(sum2%2==0)
		{
	    		printf("bike or car number under the even condition");
	    		c=2;
		}
		else
		{
	      	printf("bike or car number under the odd condition");
	      	c=1;
		}
		}
		else if(sum1%2==0)
		{
		    printf("bike or car number under the even condition");
		    c=2;
		}
		else
		{
			printf("bike or car number under the odd condition");
			c=1;
		}
		
	}
	else 
	{
		if(sum%2==0)
		{
			printf("bike or car number under the even condition");
			c=2;
		}
		else
		{
			printf("bike or car number under the odd condition");
			c=1;
		}
	}
	if(count==c)
	{
		printf("\nyour bike or car is on road\n");
		
	}                                                 // sub main logic for pollution control
	else if(count!=c)
	{
		printf("\nyour bike or car is not enter no road \n if you on the road pay the fine to traffic police\n");
	}
	}
	else
	{
		printf("you enter wrong condition");
		
	}
	
		printf("\n\n");
			printf("------------------------------------------");
}

