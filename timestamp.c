#include <sys/time.h>
#include <stdio.h>

void wait_a_while(void);
long elapsed_micros(struct timeval*, struct timeval*);

int main(void)
{
    struct timeval start, end;

    gettimeofday(&start, NULL);
    wait_a_while();
    gettimeofday(&end, NULL);
    printf("Time elapsed in microseconds: %ld", elapsed_micros(&start, &end));

    return 0;
}

long elapsed_micros(struct timeval* start, struct timeval* end)
{
    long seconds = end->tv_sec - start->tv_sec;
    return (seconds * 1E+6) + end->tv_usec - start->tv_usec;
}

void wait_a_while(void)
{
    int i;
    for(i=0; i<1000000000; ++i);
}
