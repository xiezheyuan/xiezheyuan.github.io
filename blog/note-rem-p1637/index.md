<head>
    <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            tex2jax: {
            skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
            inlineMath: [['$','$']]
            }
        });
    </script>
</head>

## P1637 三元上升子序列

## 题面

Erwin 最近对一种叫 `thair` 的东西巨感兴趣。。。

在含有 $n$ 个整数的序列 $a_1,a_2,\ldots,a_n$ 中，三个数被称作`thair`当且仅当 $i<j<k$ 且 $a_i<a_j<a_k$。

求一个序列中 `thair` 的个数。

### 输入格式

开始一行一个正整数 $n$,

以后一行 $n$ 个整数 $a_1,a_2,\ldots,a_n$。

### 输出格式

一行一个整数表示 `thair` 的个数。

### 数据规模与约定

- 对于 $30\%$ 的数据 保证 $n\le100$；
- 对于 $60\%$ 的数据 保证 $n\le2000$；
- 对于 $100\%$ 的数据 保证 $1 \leq n\le3\times10^4$，$0\le a_i\lt2^{63}$。

## 思路

### 暴力DP思路

这里我们考虑广义的 `thair`，即有 $m$ 个数满足上升规则。

正常思维——二位DP。

设 $f[i][j]$ 为以 $a_j$ 结尾的长度为 $i$ 的 `thair` 长度，那么就有以下DP方程。

$$f[i][j] = \sum_{k \lt j,a_k \lt a_j} {f[i-1][k]}$$

应该还是简单的。

### 考虑优化

如果这样写，时间复杂度为 $O(n^{2}m)$，妥妥T掉，只能拿 $60 \text{pts}$。

为了满足 $k \lt j,a_k \lt a_j$，可以考虑离散化一下。

然后转移可以用树状数组优化。具体情况如下：

维护另一个数组 $t$。

有 
$$f[i][j] = \sum_{k=0}^{a_j-1}{t_k},t[a[j]] = t[a[j]] + f[i-1][j]$$

然后就可以用树状数组优化了

最终时间复杂度为 $O(nm \log n)$。这里 $m=3$，也就是 $O(3n \log n) = O(n \log n)$。

## 代码

```cpp
#include <bits/stdc++.h>
using namespace std;

int n,m=3;
long long ans=0;
const int MSIZE = 5;
const int SIZE = 3e4+5;
long long t[SIZE<<2],a[SIZE],la[SIZE];
long long f[MSIZE][SIZE<<2];

int lowbit(int x){
	return x&-x;
}

int query(int p){
	int res=0;
	while(p>0){
		res+=t[p];
		p-=lowbit(p);
	}
	return res;
}

void update(int p,int v){
	while(p<=n){
		t[p]+=v;
		p+=lowbit(p);
	}
}

void discretization(){
	for(int i=1;i<=n;i++){
		la[i]=a[i];
	}
	sort(la+1,la+n+1);
	int tmp=unique(la+1,la+n+1)-la-1;
	for(int i=1;i<=n;i++){
		a[i]=lower_bound(la+1,la+tmp+1,a[i])-la;
	}
}

int main(){
	cin>>n;
	for(int i=1;i<=n;i++){
		cin>>a[i];
	}
	discretization();
	for(int i=1;i<=n;i++){
		f[1][i]=1;
	}
	for(int i=2;i<=m;i++){
		memset(t,0,sizeof(t));
		for(int j=1;j<=n;j++){
			f[i][j]=query(a[j]-1);
			update(a[j],f[i-1][j]);
		}
	}
	for(int i=1;i<=n;i++){
		ans+=f[m][i];
	}
	cout<<ans<<endl;
	return 0;
}
```
