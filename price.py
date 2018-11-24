def format_price(price):
  	price_int=int(price)
  	return 'Цена:' + str(price_int) + 'руб.'
display_price = format_price(56.24)
print(display_price)
	