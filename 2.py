from datetime import datetime, timedelta
iruz = datetime.now() 
pareruz = iruz - timedelta(days=2)
pagaidiga = iruz + timedelta(days=2)

print(pareruz.strftime('%d-%m-%Y'))
print(iruz.strftime('%d-%m-%Y'))
print(pagaidiga.strftime('%d-%m-%Y'))