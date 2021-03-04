from update_optimizer_elo_ratings import update_optimizer_elo_ratings_once

PATTERN = None # 'e.g. hebo'

if __name__=='__main__':
    while True:
        print(' ')
        print('--------------------------------')
        try:
            update_optimizer_elo_ratings_once(pattern=PATTERN)
        except RuntimeError as e:
            print(e)
        print(' ',flush=True)

