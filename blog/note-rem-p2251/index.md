# P2251 质量检测

## 题面

为了检测生产流水线上总共 $N$ 件产品的质量，我们首先给每一件产品打一个分数 $A$ 表示其品质，然后统计前 $M$ 件产品中质量最差的产品的分值 $Q[m] = min\{A_1, A_2, ... A_m\}$，以及第 2 至第 $M + 1$ 件的 $Q[m + 1], Q[m + 2] $... 最后统计第 $N - M + 1$ 至第 $N$ 件的 $Q[n]$。根据 $Q$ 再做进一步评估。

请你尽快求出 $Q$ 序列。

### 输入格式

输入共两行。

第一行共两个数 $N$、$M$，由空格隔开。含义如前述。

第二行共 $N$ 个数，表示 $N$ 件产品的质量。


### 输出格式

输出共 $N - M + 1$ 行。

第 1 至 $N - M + 1$ 行每行一个数，第 $i$ 行的数 $Q[i + M - 1]$。含义如前述。

### 数据范围

30%的数据，$N \le 1000$

100%的数据，$N \le 100000$

100%的数据，$M \le N, A \le 1 000 000$

## 思路

这是一道ST表水题。想必不要多说。

## 代码

```cpp
#include <bits/stdc++.h>
using namespace std;

int STTable[100005][25];

int min(int x, int y){
	if(x>y){
		return y;
	}
	else{
		return x;
	}
}

inline int read() {
	int x=0,f=1;
	char ch=getchar();
	while (ch<'0'||ch>'9') {
		if (ch=='-') f=-1;
		ch=getchar();
	}
	while (ch>='0'&&ch<='9') {
		x=x*10+ch-48;
		ch=getchar();
	}
	return x*f;
}
int query(int l,int r) {
	int k=log2(r-l+1);
	return min(STTable[l][k],STTable[r-(1<<k)+1][k]);
}

int main() {
	int N=read(),M=read();
	for(int i=1; i<=N; i++) {
		STTable[i][0] = read();
	}
	for(int j=1; j<=21; j++) {
		for(int i=1; i+(1<<j)-1<=N; i++) {
			STTable[i][j]=min(STTable[i][j-1],STTable[i+(1<<(j-1))][j-1]);
		}
	}
	for(int l=1,r=M;r<=N;l++,r++){
		cout<<query(l,r)<<endl;
	}
	return 0;
}

```

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script> <script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: { skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'], inlineMath: [['$','$']] } }); </script>
