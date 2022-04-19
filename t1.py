import csv
import os

def read_file(address='record.csv'):
	raw = []
	if os.path.isfile(address):
		with open(address, newline='', encoding='utf-8-sig') as f:
			rows = csv.reader(f)
			for r in rows:			
				raw.append(r)
		return raw
	else:
		print('找不到檔案')


def analyze(raw):
	start_date = raw[-1][0]
	end_date = raw[1][0]
	card_top_up = []
	deposit = []
	withdraw = []
	interest = []
	cashback = []
	rebate_N = []	# Netflix
	rebate_S = []	# Spotify
	trans_kind = {0 : 'card_top_up',
				  1 : 'crypto_deposit',
				  2 : 'crypto_earn_interest_paid',
				  3 : 'crypto_payment',
				  4 : 'crypto_purchase',
				  5 : 'crypto_withdrawal',
				  6 : 'gift_card_reward',
				  7 : 'mco_stake_reward',
				  8 : 'referral_card_cashback',
				  9 : 'Card Rebate: Netflix',
				  10 : 'Card Rebate: Spotify'}
	for r in raw:
		count = 0
		while count < 11:
			if trans_kind.get(count) in r:
				if count == 0:
					card_top_up.append(r[8])
					withdraw.append(r[8])
					break
				elif count == 1 or count == 4:
					deposit.append(r[8])
					break
				elif count == 3 or count == 5:
					withdraw.append(r[8])
					break
				elif count == 2 or count == 7:
					interest.append(r[8])
					break
				elif count == 6 or count == 8:
					cashback.append(r[8])
					break
				elif count == 9:
					rebate_N.append(r[8])
					cashback.append(r[8])
					break
				elif count == 10:
					rebate_S.append(r[8])
					deposit.append(r[8])
					break
			count += 1
	# casting
	card_top_up = [float(i) for i in card_top_up]
	deposit = [float(i) for i in deposit]
	withdraw = [float(i) for i in withdraw]
	interest = [float(i) for i in interest]
	cashback = [float(i) for i in cashback]
	rebate_N = [float(i) for i in rebate_N]
	rebate_S = [float(i) for i in rebate_S]
	print('從', start_date, ' 到 ', end_date)
	print('總儲值 ', '%.2f'%sum(card_top_up), 'USD')
	print('總入金 ', '%.2f'%sum(deposit), 'USD')
	print('總出金 ', '%.2f'%sum(withdraw), 'USD')
	print('總利息 ', '%.2f'%sum(interest), 'USD')
	print('總刷卡回饋 ', '%.2f'%sum(cashback), 'USD')
	print('N回饋總共 ', '%.2f'%sum(rebate_N), 'USD')
	print('S回饋總共 ', '%.2f'%sum(rebate_S), 'USD')


def main():
	raw = read_file()
	if raw:
		analyze(raw)


if __name__ == '__main__':
	main()