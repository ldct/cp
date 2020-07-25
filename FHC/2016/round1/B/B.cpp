#include <iostream>
#include <queue>
#include <utility>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<ll, char> llc;
int T;
long long L, M, N, D;

priority_queue<ll, vector<ll>, greater<ll>> dryers;
priority_queue<pll, vector<pll>, greater<pll>> washers;
// first: if you throw smt into my mailbox now, 
// when is the next time I can be free?
// second: whats my waiting time

priority_queue<llc, vector<llc>, greater<llc>> events;
// <event time, event type>
// w: washer fnish
// d: dryer finish

ll minTime() {
	ll current_time = 0;
	while (1) {

		if (!events.empty()) {
			// cout << "handle events" << endl;

			auto next_event = events.top();
			events.pop();

			current_time = next_event.first;
			// cout << "current_time=" << current_time << endl;
	
			auto current_type = next_event.second;

			// cout << "current_event=" << current_time << current_type << endl;

			if (current_type == 'd') {
				// cout << "dryer done at " << current_time << endl;
				continue;
			} else if (current_type == 'w') {
				// cout << "washer done at " << current_time << endl;
				// put in dryer
				auto best_dryer = dryers.top();
				dryers.pop();

				auto best_time = max(best_dryer, current_time + D);
				events.push(make_pair(best_time, 'd'));
				
				dryers.push(best_time + D);
			}
		}
		if (events.empty() && L == 0) {
			return current_time;
		}
	}
}

int main() {
	cin >> T;
	for (int t=0; t<T; t++) {
		cin >> L >> N >> M >> D;

		dryers = priority_queue<ll, vector<ll>, greater<ll>>();
		washers = priority_queue<pll, vector<pll>, greater<pll>>();
		events = priority_queue<llc, vector<llc>, greater<llc>>();

		for (int n=0; n<N; n++) {
			int w;
			cin >> w;
			washers.push(make_pair(w, w));
		}
		for (int m=0; m<M; m++) {
			dryers.push(D);
		}
		while (L > 0) {

			auto best_washer = washers.top();
			washers.pop();

			auto bw_done = best_washer.first;
			auto bw_wait = best_washer.second;

			events.push(make_pair(bw_done, 'w'));
			washers.push(make_pair(bw_done + bw_wait, bw_wait));

			L--;
		}

		cout << "Case #" << t + 1 << ": " << minTime() << endl;
	}

}