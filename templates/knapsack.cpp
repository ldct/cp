// tested on https://atcoder.jp/contests/abc056/tasks/arc070_b
vector<bool> ss_ncp(int target, vector<int> B) {
  auto possible = vector<bool>(target+1, false);
  possible[0] = true;

  for (auto b : B) {
    for (int mass=target; mass!=-1; mass--) {
      if (possible[mass] && (mass + b <= target))
          possible[mass+b] = true;
      }
  } 

  return possible;
}
