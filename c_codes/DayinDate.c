// A program to find day of a given date    
//1.mon 2.tue 3.wed 4.thu 5.fri 6.sat 7.sun
#include<stdio.h> 
  
int dayofweek(int d, int m, int y) 
{ 
    static int t[] = { 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 }; 
    y -= m < 3; 
    return ( y + y/4 - y/100 + y/400 + t[m-1] + d) % 7; 
} 
  

int main() 
{ 
int x,y,z;
printf("enter the date in the format (day/month/year)\n");
scanf("%d\n",&x);
scanf("%d\n",&y);
scanf("%d",&z);
printf(" the day will be ...");

    int day = dayofweek(x, y, z);  
   switch(day)
   {
   	case 1: printf("Monday");
   	        break;
   	case 2: printf("Tuesday");
	        break;
    case 3: printf("Wednsday");
	        break;
    case 4: printf("Thursday") ;
	        break;
    case 5: printf("Friday");
	        break;
	case 6: printf("Saturday");
	        break;
	case 7: printf("Sunday is holiday");
	        break;
	default :
	      printf("something wrong\n");
	      break;
   	
   }
    return 0; 
} 
