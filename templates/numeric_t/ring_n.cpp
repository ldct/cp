#include <bits/stdc++.h>
using namespace std;

// standard representitives in the ring of integers modulo N

constexpr int MODULUS = 1000000007;

template<typename numeric_t = long long, numeric_t MODULUS = MODULUS>
class RInt {
public:
  numeric_t val;
  RInt (numeric_t _val) { val = _val; }
  friend ostream& operator << (ostream& os, const RInt& s) { return os << s.val; }
  RInt operator+ (const RInt& r) const { return RInt((this->val + r.val) % MODULUS); }
  RInt operator* (const RInt& r) const { return RInt((this->val * r.val) % MODULUS); }
  RInt& operator+= (const RInt& r) { this->val += r.val; this->val %= MODULUS; return *this; }
};

int main() { 
  auto a = RInt<>(1000000000);
  cout << "Hello World" << a * a << endl;
}
