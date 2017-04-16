#include <stdio.h>

#define N 1000

int multiSum(int x, int a)
{
	if (x >= N) return 0;
	return x + multiSum(x + a, a);
}

int main(int argc, char const *argv[])
{
	printf("answer: %d\n", multiSum(3, 3) + multiSum(5, 5) - multiSum(15, 15));
	return 0;
}