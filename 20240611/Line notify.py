import requests

# 這裡替換成你的LINE Notify Token
token = "kvq9nMjVDWh4axXlb5Klc4LS9c4EmmTwqrmUaeoKmpp"

# 要發送的消息
message = "徐靚倪."

# 發送請求
response = requests.post(
  "https://notify-api.line.me/api/notify",
  headers={"Authorization": f"Bearer {token}"},
  data={"message": message}
)

