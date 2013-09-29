#include <sys/time.h>
#include <stdio.h>

void wait_a_while(void);

int main(void)
{
    struct timeval start, end;
    long long elapsed_seconds, elapsed_nanos;

    gettimeofday(&start, NULL);
    wait_a_while();
    gettimeofday(&end, NULL);

    elapsed_seconds = end.tv_sec - start.tv_sec;
    elapsed_nanos = end.tv_usec - start.tv_usec;

    printf("%lld seconds and %lld nanoseconds", elapsed_seconds, elapsed_nanos);
}

void wait_a_while(void)
{
    int i;
    for(i = 0; i < 100000; ++i) {

    }
}
