import csv
import os

def read_file(address):
	raw = []
	if os.path.isfile(address):
		with open(address, newline='', encoding='utf-8-sig') as f:
			rows = csv.reader(f)
			for r in rows:			
				raw.append(r)
		return raw
	else:
		print('找不到檔案')


def convert(raw):
	new = []
	trans_kind = {
			  0 : 'card_top_up',
			  1 : 'crypto_deposit',
			  2 : 'crypto_payment',
			  3 : 'referral_card_cashback',
			  4 : 'crypto_purchase',
			  5 : 'crypto_withdrawal',
			  6 : 'gift_card_reward',
			  7 : 'mco_stake_reward',
			  8 : 'Card Rebate: Spotify',
			  9 : 'Card Rebate: Netflix',
			  10 : 'crypto_earn_interest_paid'}
	for r in raw:
		for k in trans_kind:
			if len(new) <= k:
				new.append([trans_kind.get(k)])
			if trans_kind.get(k) in r:
				new[k].append(r[8])
	i = 0
	while i < len(new):
		new[i][1:] = [[float(e) for e in new[i][1:]]]
		i += 1

	#new.append([raw[-1][0], raw[1][0]]) # date
	return new


def main():
	raw_app = read_file('record_app.csv')
	if raw_app:
		data_app = convert(raw_app)
		print('From', raw_app[-1][0], ' to ', raw_app[1][0])
		for e in data_app:
			print(e[0], '	: ', '%.2f'%sum(e[1]), 'USD')

if __name__ == '__main__':
	main()