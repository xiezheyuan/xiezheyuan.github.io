# P1531 I Hate It

## 题面

很多学校流行一种比较的习惯。老师们很喜欢询问，从某某到某某当中，分数最高的是多少。这让很多学生很反感。

不管你喜不喜欢，现在需要你做的是，就是按照老师的要求，写一个程序，模拟老师的询问。当然，老师有时候需要更新某位同学的成绩。

### 输入格式

第一行，有两个正整数 $n$ 和 $m$（$0<n \le 2\times 10^5,0<m<5000$），分别代表学生的数目和操作的数目。学生 ID 编号分别从 $1$ 编到 $n$。第二行包含 $n$ 个整数，代表这 $n$ 个学生的初始成绩，其中第 $i$ 个数代表 ID 为 $i$ 的学生的成绩。接下来有 $m$ 行。每一行有一个字符 $c$（只取 `Q` 或 `U`），和两个正整数 $a$，$b$。当 $c$ 为 `Q` 的时候，表示这是一条询问操作，它询问 ID 从 $a$ 到 $b$（包括 $a,b$） 的学生当中，成绩最高的是多少。当 $c$ 为 `U` 的时候，表示这是一条更新操作，如果当前 $a$ 学生的成绩低于 $b$，则把 ID 为 $a$ 的学生的成绩更改为 $b$，否则不改动。

### 输出格式

对于每一次询问操作，在一行里面输出最高成绩。

## 思路

维护区间 $\max$ 的线段树，然后实现区间查询+单点修改即可。

时间复杂度 $O(m \log n)$。

## 代码

```cpp
#include<bits/stdc++.h>
using namespace std;

const int SIZE = 2e5+5;
int t[SIZE<<2],a[SIZE];
int n,m;

void pushup(int i){
	t[i]=max(t[i<<1],t[i<<1|1]);
}

void build(int i,int l,int r){
	if(l==r){
		t[i]=a[l];
		return;
	}
	int mid=(l+r)>>1;
	build(i<<1,l,mid);
	build(i<<1|1,mid+1,r);
	pushup(i);
}

int query(int ql,int qr,int l,int r,int i){
	if(ql<=l && r <= qr){
		return t[i];
	}
	int mid = (l+r)>>1;
	int result = 0;
	if(ql <= mid){
		result = max(result,query(ql,qr,l,mid,i<<1));
	}
	if(qr > mid){
		result = max(result,query(ql,qr,mid+1,r,i<<1|1));
	}
	return result;
}

void update(int p,int l,int r,int i,int v){
	if(l==r){
		if(t[i]<v){
			t[i]=v;
		}
		return;
	}
	int mid=(l+r)>>1;
	if(p <= mid){
		update(p,l,mid,i<<1,v);
	}
	if(p > mid){
		update(p,mid+1,r,i<<1|1,v);
	}
	pushup(i);
}

int main(){
	cin>>n>>m;
	for(int i=1;i<=n;i++){
		cin>>a[i];
	}
	build(1,1,n);
	while(m--){
		char op;int a,b;
		cin>>op>>a>>b;
		if(op=='Q'){
			cout<<query(a,b,1,n,1)<<endl;
		}
		else{
			update(a,1,n,1,b);
		}
	}
	return 0;
}

```
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script> <script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: { skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'], inlineMath: [['$','$']] } }); </script>
