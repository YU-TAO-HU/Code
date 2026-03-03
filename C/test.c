#include<stdio.h>

struct A
{
    int i;
    int n;
};

int main()
{
    struct A a = {1, 2};
    printf("a.i = %d, a.n = %d\n", a.i, a.n);
    return 0;
}