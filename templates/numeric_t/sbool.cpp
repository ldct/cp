class SBool { 
public: 
  bool val;
  SBool (bool _val) { val = _val; } 
  friend ostream& operator << (ostream& os, const SBool& s) { return os << (s.val ? 'Y' : 'N'); } 
  SBool operator+ (const SBool& r) const { return SBool(this->val || r.val); } 
  SBool operator* (const SBool& r) const { return SBool(this->val && r.val); }
  SBool& operator+= (const SBool& r) { this->val = this->val || r.val; return *this; } };