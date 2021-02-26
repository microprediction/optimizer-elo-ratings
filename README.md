# optimizer-elo-ratings ([ARTICLE](https://www.microprediction.com/blog/humpday))
Assigns [Elo ratings](https://github.com/microprediction/optimizer-elo-ratings/tree/main/results/leaderboards/overall) to global derivative-free Python global optimization "strategies", using the [HumpDay](https://github.com/microprediction/humpday) package. 



![](https://i.imgur.com/FCiSrMQ.png)

### View Leaderboards

See the current [overall leaderboard](https://github.com/microprediction/optimizer-elo-ratings/tree/main/results/leaderboards/overall) or drill into specific [leaderboards](https://github.com/microprediction/optimizer-elo-ratings/tree/main/results/leaderboards) broken down by dimension of the problem, and the number of function evaluations allowed. Be aware that some of these are yet to reach equilibrium. 

### What's a strategy?

A choice of python package (such as scipy.optimize, ax-platform, hyperopt, nevergrad, optuna, platypus, pymoo, pySOT or skopt) together with a fixing of additional choices (such as selection of method, choice of parameters etc). 

### Create your own shortlist

See the [HumpDay](https://github.com/microprediction/humpday) package for simple ways to select optimizers based on their performance on your problems, not ours.  



### Contribute

Got a good objective function, or optimization strategy? Shove it in the [HumpDay](https://github.com/microprediction/humpday) package and file a pull request, or at least suggest it in the issues. 
