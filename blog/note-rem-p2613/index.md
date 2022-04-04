# P2613 【模板】有理数取余

## 题面

给出一个有理数 $c=\frac{a}{b}$，求 $c \bmod 19260817$ 的值。

### 输入格式

一共两行。

第一行，一个整数 $a$。  
第二行，一个整数 $b$。  

## 输出格式

一个整数，代表求余后的结果。如果无解，输出 `Angry!`。

## 数据范围

对于所有数据，保证 $0\leq a \leq 10^{10001}$，$1 \leq b \leq 10^{10001}$，且 $a, b$ 不同时是 $19260817$ 的倍数。

## 思路

## 前置思路

建议先以下题目

- [P1082 [NOIP2012 提高组] 同余方程](https://www.luogu.com.cn/problem/P1082)

### 基础思路

`std::fmod` 是没用滴。

式子变一下形：

$c=a \div b \pmod{19260817}$

$c=a \times b^{-1} \pmod{19260817}$


然后就是对 $b$ 求逆元（可以用exgcd），然后就直接乘就好了。

（无解就是 $b=0$ ）

### 快读

如果你这样提交了，那么只有 $0$ 分。因为数据范围太大了。

~~不想写高精度~~

你需要一边读一边取模，而这可以用快读实现。

快读带取模参考代码：（来源：[题解 P2613 【【模板】有理数取余】
](https://www.luogu.com.cn/blog/cicos/solution-p2613) ）

```cpp
inline int read() {
	int res = 0, ch = getchar();
	while(!isdigit(ch) and ch != EOF){
		ch = getchar();
	}
	while(isdigit(ch)) {
		res = (res << 3) + (res << 1) + (ch - '0');
		res %= MOD;
		ch = getchar();
	}
	return res;
}
```

## 代码

```cpp
#include <bits/stdc++.h>
#define int long long
using namespace std;

int x,y;
const int MOD = 19260817;
int a,b;

inline int read() {
	int res = 0, ch = getchar();
	while(!isdigit(ch) and ch != EOF){
		ch = getchar();
	}
	while(isdigit(ch)) {
		res = (res << 3) + (res << 1) + (ch - '0');
		res %= MOD;
		ch = getchar();
	}
	return res;
}

void exgcd(int a,int b) {
	if(b==0) {
		x=1;
		y=0;
	} else {
		exgcd(b,a%b);
		int tmp=x;
		x=y;
		y=tmp-a/b*y;
	}
}

signed main() {
	a=read(),b=read();
	if(b==0) {
		printf("Angry!");
		return 0;
	}
	exgcd(b,MOD);
	x=(x+MOD)%MOD;
	cout<<a*x%MOD<<endl;
	return 0;
}

```
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script> <script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: { skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'], inlineMath: [['$','$']] } }); </script>
