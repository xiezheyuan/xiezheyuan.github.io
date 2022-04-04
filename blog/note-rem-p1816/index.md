# P1816 忠诚

## 题面

老管家是一个聪明能干的人。他为财主工作了整整  $10$ 年。财主为了让自已账目更加清楚，要求管家每天记  $k$ 次账。由于管家聪明能干，因而管家总是让财主十分满意。但是由于一些人的挑拨，财主还是对管家产生了怀疑。于是他决定用一种特别的方法来判断管家的忠诚，他把每次的账目按  $1, 2, 3 \ldots$ 编号，然后不定时的问管家问题，问题是这样的：在   $a$ 到  $b$ 号账中最少的一笔是多少？为了让管家没时间作假，他总是一次问多个问题。

### 输入格式

输入中第一行有两个数  $m, n$，表示有  $m$ 笔账  $n$ 表示有  $n$ 个问题。

第二行为  $m$ 个数，分别是账目的钱数。

后面  $n$ 行分别是  $n$ 个问题，每行有   $2$ 个数字说明开始结束的账目编号。


### 输出格式

在一行中输出每个问题的答案，以一个空格分割。

## 提示

对于 $100\%$ 的数据，$m \leq 10^5$，$n \leq 10^5$。

## 思路

ST表模板题。只需要把 [P3865 【模板】ST 表](https://www.luogu.com.cn/problem/P3865)
改改就可以了。

## 代码

```cpp
#include <cstdio>
#include <cmath>
using namespace std;

int STTable[1000005][25];

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
	for(int i=1; i<=M; i++) {
		int l=read(),r=read();
		printf("%d ",query(l,r));
	}
	return 0;
}

```
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script> <script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: { skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'], inlineMath: [['$','$']] } }); </script>
