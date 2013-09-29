#include <sys/time.h>
#include <stdio.h>

void wait_a_while(void);
long long elapsed_nanos(struct timeval*, struct timeval*);

int main(void)
{
    struct timeval start, end;
    gettimeofday(&start, NULL);
    wait_a_while();
    gettimeofday(&end, NULL);
    printf("Time elapsed in nanoseconds: %lld", elapsed_nanos(&start, &end));

    return 0;
}

long long elapsed_nanos(struct timeval* start, struct timeval* end)
{
    long seconds, full_nano = 1E+9;
    seconds = end->tv_sec - start->tv_sec;

    if(seconds == 0 || (end->tv_usec) == (start->tv_usec)) {
        return end->tv_usec - start->tv_usec;
    }
    else if((end->tv_usec) < (start->tv_usec)) {
        return full_nano * (seconds - 1) + start->tv_usec - end->tv_usec;
    }
    else {
        return full_nano * seconds + end->tv_usec - start->tv_usec;
    }
}

void wait_a_while(void)
{
    int i;
    for(i = 0; i < 1000000000; ++i) {

    }
}
