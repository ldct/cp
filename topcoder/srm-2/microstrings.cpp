#include <string>
#include <cstdio>

using namespace std;
class MicroStrings {
    public:
    string makeMicroString(int A, int D) {
        char buff[10000];
        buff[0] = '\0';
        do {
            sprintf(buff, "%s%d", buff, A);
            A = A - D;
        } while (A > 0);
        return string(buff);
    }

};

int main() {
MicroStrings ___test;
    ___test.makeMicroString(12, 5);
}
