#include <cstdio>
#include <algorithm>

#define MAX_N 200001

int E[MAX_N];

using namespace std;

int main() {
  
    int T;

    scanf("%d", &T);

    for (int t=0; t<T; t++) {
        int N;
        scanf("%d", &N);
        for (int n=0; n<N; n++) {
            scanf("%d", &E[n]);
        }
        sort(E, E+N);
        // for (int n=0; n<N; n++) {
        //     printf("%d ", E[n]);
        // }
        // printf("\n");

        int group_size;
        int num_groups = 0;
        int current_attendance = 0;

        for (int i=0; i<N; i++) {
            group_size = E[i];
            current_attendance += 1;
            if (current_attendance == group_size) {
                current_attendance = 0;
                num_groups += 1;
            }
        }

        printf("%d\n", num_groups);
    }

    return 0;
}
