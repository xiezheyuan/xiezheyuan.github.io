# P2216 [HAOI2007]理想的正方形

## 题面

有一个 $a \times b$ 的整数组成的矩阵，现请你从中找出一个 $n \times n$ 的正方形区域，使得该区域所有数中的最大值和最小值的差最小。

### 输入格式

第一行为 $3$ 个整数，分别表示 $a,b,n$ 的值。

第二行至第 $a+1$ 行每行为 $b$ 个非负整数，表示矩阵中相应位置上的数。每行相邻两数之间用一空格分隔。

### 输出格式

仅一个整数，为 $a \times b$ 矩阵中所有“ $n \times n$ 正方形区域中的最大整数和最小整数的差值”的最小值。

### 问题规模

矩阵中的所有数都不超过 $1,000,000,000$。

$20\%$ 的数据 $2 \le a,b \le 100,n \le a,n \le b,n \le 10$。

$100\%$ 的数据 $2 \le a,b \le 1000,n \le a,n \le b,n \le 100$。

## 思路

### 暴力

10分。

```cpp
#include <bits/stdc++.h>
using namespace std;

int a, b, n, ma[1005][1005], ans = INT_MAX;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> a >> b >> n;
	for (int i = 1; i <= a; i++) {
		for (int j = 1; j <= b; j++) {
			cin >> ma[i][j];
		}
	}
	for (int i = 1; i <= a - n + 1; i++) {
		for (int j = 1; j <= a - n + 1; j++) {
			int maxv = INT_MIN, minv = INT_MAX;
			for (int k = i; k <= i + n - 1; k++) {
				for (int l = j; l <= j + n - 1; l++) {
					maxv = max(maxv, ma[k][l]);;
					minv = min(minv, ma[k][l]);
				}
			}
			ans = min(ans, maxv - minv);
		}
	}
	cout << ans << endl;

	return 0;
}
```

### 二维ST表

这道题比较难处理。

```cpp
#include <bits/stdc++.h>
#define int long long
using namespace std;

int n,m,k,a[1005][1005],ans=INT_MAX;

namespace STTable {
	int maxv[1005][1005],minv[1005][1005],logg;

	int querymax(int x,int y){
		int mmax=0;
		mmax=max(maxv[x][y],max(maxv[x+k-(1<<logg)][y+k-(1<<logg)],max(maxv[x+k-(1<<logg)][y],maxv[x][y+k-(1<<logg)])));
		return mmax;
	}
	
	int querymin(int x,int y){
		int mmin=0;
		mmin=min(minv[x][y],min(minv[x+k-(1<<logg)][y+k-(1<<logg)],min(minv[x+k-(1<<logg)][y],minv[x][y+k-(1<<logg)])));
		return mmin;
	}
	
	int query(int x, int y) {
		return querymax(x,y)-querymin(x,y);
	}

	void init() {
		logg = log(k)/log(2);
		for(int s=0; s<logg; s++) {
			for(int i=1; i+(1<<s)<=n; i++) {
				for(int j=1; j+(1<<s)<=m; j++) {
					maxv[i][j]=max(maxv[i][j],max(maxv[i+(1<<s)][j+(1<<s)],max(maxv[i+(1<<s)][j],maxv[i][j+(1<<s)])));
					minv[i][j]=min(minv[i][j],min(minv[i+(1<<s)][j+(1<<s)],min(minv[i+(1<<s)][j],minv[i][j+(1<<s)])));
				}
			}
		}
	}
}

signed main(){
	cin>>n>>m>>k;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=m;j++){
			cin>>a[i][j];
			STTable::maxv[i][j]=a[i][j];
			STTable::minv[i][j]=a[i][j];
		}
	}
	STTable::init();
	for(int i=1;i<=n-k+1;i++){
		for(int j=1;j<=m-k+1;j++){
			ans=min(ans,STTable::query(i,j));
		}
	}
	cout<<ans<<endl;
}
```

$100$ 分。
  
  <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script> <script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: { skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'], inlineMath: [['$','$']] } }); </script>
