# [Optimizer Elo Ratings](https://microprediction.github.io/optimizer-elo-ratings/html_leaderboards/overall.html)

Behold a [colab notebook](https://github.com/microprediction/humpday/blob/main/humpday_points_race.ipynb) that recommends a black-box optimizer for your objective function. 

See [article](https://www.microprediction.com/blog/humpday). This repo assigns Elo ratings ([json](https://github.com/microprediction/optimizer-elo-ratings/tree/main/results/leaderboards/overall) and [html](https://microprediction.github.io/optimizer-elo-ratings/html_leaderboards/overall.html)) to global derivative-free Python global optimization "strategies", using the [HumpDay](https://github.com/microprediction/humpday) package. There's no free lunch. 



![](https://i.imgur.com/WgL7NCC.png)

### View Leaderboards

- HTML: [overall leaderboard](https://microprediction.github.io/optimizer-elo-ratings/html_leaderboards/overall.html) 
- JSON: [leaderboards](https://github.com/microprediction/optimizer-elo-ratings/tree/main/results/leaderboards) 

### What's a strategy?

A choice of python package (such as scipy.optimize, ax-platform, hyperopt, nevergrad, optuna, platypus, pymoo, pySOT or skopt) together with a fixing of additional choices (such as selection of method, choice of parameters etc). 

### Create your own shortlist

[HumpDay](https://github.com/microprediction/humpday) contains scripts for choosing optimizers based on your own problems.   


### Contribute

Got a good objective function, or optimization strategy? Shove it in the [HumpDay](https://github.com/microprediction/humpday) package and file a pull request, or at least suggest it in the issues. 
