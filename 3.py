from datetime import datetime, timedelta

def vichitat(data, ruz):
  novaya_data = data - timedelta(days=ruz)
  return novaya_data

imruz = datetime.now()

novaya_data = vichitat(imruz, 5)

print(f" {imruz.strftime('%d %m %Y')}")
print(f"{novaya_data.strftime('%d %m %Y')}")