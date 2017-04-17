# Problem1 
1000未満の数のうち、3の倍数と5の倍数の総和を求める問題

## 考え方 ##
ふつうに考えてループを使えばよいことはわかる  
終了条件は1000ということもわかる  
もしくは999から始めてカウントダウンでもいい  
何も考えずfor文を使って解くとループは  
```c:problem1
	sum = 0;
	for (i = 3; i < 1000; i++) {
		if (i % 3 == 0 | i % 5 == 0){
			sum += i;
		}
	}
```
といった感じになると思う  
これだと考えなくてよい数、つまり3と5の倍数以外の数のループに時間を取られるので、もっと効率的に求められないかと思って再帰を使ってみた  
multiSumはaの倍数のSumを取っていく関数  
この関数だとまさに倍数だけを計算していくので無駄が少ない  
これを使って3の倍数の総和と5の倍数の総和を計算し、ダブった15の倍数の総和を一回引くことで題意に沿った値を求めている