int N,K;
ll A[301000];
int vis[301000];
int ma=1020000000;

void dodo(int L,int R) {
    int num=(R-L)/K;
    if(A[R]-A[L]<num) {
        _P("Incorrect sequence\n");
        exit(0);
    }
    num--;
    if(num>=1) {
        int rl=-num/2,rr=(num-1)/2;
        if(rl<A[L]+1) rl=A[L]+1,rr=rl+(num-1);
        if(rr>A[R]-1) rr=A[R]-1,rl=rr-(num-1);
        for(int i=1;L+i*K<R;i++) A[L+i*K]=rl+i-1;
    }
}

void solve() {
    int i,j,k,l,r,x,y; string s;

    cin>>N>>K;
    FOR(i,K) A[i]=-ma;
    FOR(i,K) A[N+K+i]=ma;
    FOR(i,N) {
        cin>>s;
        if(s=="?") A[i+K]=-1<<30;
        else A[i+K]=atoi(s.c_str());
    }
    N+=2*K;
    FOR(i,N) if(vis[i]==0) {
        vis[i]=1;
        for(j=i+K;j<N;j+=K) {
            if(A[j]!=-1<<30) break;
            vis[j]=1;
        }
        if(j<N) dodo(i,j);
    }
    FOR(i,N-2*K) cout<<A[i+K]<<" ";
    cout<<endl;
}