# -*- coding: utf-8 -*-


def send_mail(email):
    pass


def send_mails(*emails, trace=False):
    for email in emails:
        send_mail(email)
        if trace:
            print("E-mail %s was sent." % email)


send_mails("info@domain.com", "info2@domain.com")
send_mails("info@domain.com", "info2@domain.com", trace=True)