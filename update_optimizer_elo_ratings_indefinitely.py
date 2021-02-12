from update_optimizer_elo_ratings import update_optimizer_elo_ratings_once

if __name__=='__main__':
    while True:
        print(' ')
        print('--------------------------------')
        try:
            update_optimizer_elo_ratings_once()
        except RuntimeError as e:
            print(e)
        print(' ',flush=True)

