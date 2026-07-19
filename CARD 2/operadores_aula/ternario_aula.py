lockdown = False
cash = 10000

status = 'Em casa' if lockdown or cash <= 100 else 'Uhuuuuuuuuuuuu'

print(f'O status eh: {status}')