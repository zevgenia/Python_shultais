runs = 0

def send_mail(email):
    global runs
    runs += 1
    print("send {0}".format(email))

send_mail("admin@domain.com")

for user_email in ["info@domain.com", "info2@domain.com", "info3@domain.com"]:
    send_mail(user_email)

print(runs)
