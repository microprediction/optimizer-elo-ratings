# [Optimizer Elo Ratings](https://microprediction.github.io/optimizer-elo-ratings/html_leaderboards/overall.html)

Behold a [colab notebook](https://github.com/microprediction/humpday/blob/main/black_box_optimization_package_recommender.ipynb) that recommends a black-box optimizer for your objective function. 

This repo assigns Elo ratings ([json](https://github.com/microprediction/optimizer-elo-ratings/tree/main/results/leaderboards/overall) and [html](https://microprediction.github.io/optimizer-elo-ratings/html_leaderboards/overall.html)) to global derivative-free Python global optimization "strategies", using the [HumpDay](https://github.com/microprediction/humpday) package. 

See the [article](https://www.microprediction.com/blog/humpday) for a detailed description of methodology. 


### Elo rating leaderboards

In [human readable html](https://microprediction.github.io/optimizer-elo-ratings/html_leaderboards/overall.html) and, of course, [machine readable JSON](https://github.com/microprediction/optimizer-elo-ratings/tree/main/results/leaderboards) 

### What's a strategy?

A choice of python package (such as scipy.optimize, ax-platform, hyperopt, nevergrad, optuna, platypus, pymoo, pySOT or skopt) together with a fixing of additional choices (such as selection of method, choice of parameters etc). 

### Create your own shortlist

[HumpDay](https://github.com/microprediction/humpday) contains scripts for choosing optimizers based on your own problems.   


### Contribute

Got a good objective function, or optimization strategy? Shove it in the [HumpDay](https://github.com/microprediction/humpday) package and file a pull request, or at least suggest it in the issues. 


![](https://i.imgur.com/WgL7NCC.png)
