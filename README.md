# RemangaAPI
API For https://remanga.org
Библиотека для https://remanga.org
![RemangaAPI](https://sun9-28.userapi.com/impf/kEtzLTKA0GctvG_hZIwe4KpbiyFgNGCKGHmvSA/8x3OQ6M3eHA.jpg?size=1590x400&quality=95&crop=0,0,1590,400&sign=2365cddf9181b6dd2b0aa4a8b37dca8b&type=cover_group)

### Example
```python3
# Login
import remanga
client = remanga.Client()
email = input("Email >> ")
password = input("Password >> ")
print(client.auth(email=email, password=password)))
```
