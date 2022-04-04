# P5057 [CQOI2006]简单题

## 题面

有一个 n 个元素的数组，每个元素初始均为 0。有 m 条指令，要么让其中一段连续序列数字反转——0 变 1，1 变 0（操作 1），要么询问某个元素的值（操作 2）。

### 输入格式

第一行包含两个整数 n, m，表示数组的长度和指令的条数； 以下 m 行，每行的第一个数 t 表示操作的种类：

若 t = 1，则接下来有两个数 L, R，表示区间 [L, R] 的每个数均反转； 若 t = 2，则接下来只有一个数 i，表示询问的下标。

### 输出格式

每个操作 2 输出一行（非 0 即 1），表示每次操作 2 的回答。

## 思路

简单树状数组题。

对于第一个操作，就是 $\text{xor } 1$，而第二个，就是单点查询。

时间复杂度 $O(m \log n)$。

## 代码

~~不用看题解直接现切~~

```cpp
#include <bits/stdc++.h>
using namespace std;

int n,m;
int t[400005];

int lowbit(int x){
	return x&-x;
}

void update(int p,int v=1){
	while(p<=n){
		t[p]^=v;
		p+=lowbit(p);
	}
}

int query(int p){
	int res=0;
	while(p>0){
		res^=t[p];
		p-=lowbit(p);
	}
	return res;
}

int main(){
	cin>>n>>m;
	while(m--){
		int t,l,r,i;
		cin>>t;
		if(t==1){
			cin>>l>>r;
			update(l);
			update(r+1);
		}
		else{
			cin>>i;
			cout<<query(i)<<endl;
		}
	}
	return 0;
}

```
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script> <script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: { skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'], inlineMath: [['$','$']] } }); </script>
