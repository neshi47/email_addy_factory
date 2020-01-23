#!/usr/bin/env python

import csv

def makes_email_csv(name,addy,number):
    """args are name, additional alias, and the number of emails you want"""

    with open(name + addy + '.csv', 'w') as csv_file:
        email_list_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        email_list_writer.writerow(['emails'])

        for i in range(number):
            email_list_writer.writerow([name + 'someco' + '+' + addy + str(int(i+1)) + 'd' + '@gmail.com'])
            email_list_writer.writerow([name + 'someco' + '+' + addy + str(int(i+1)) + 'm' + '@gmail.com'])


def make_email_test_suite(addy, num_of_emails):
    """does three runs of the makes_email_csv function specific to my team"""
    makes_email_csv('joe', addy, num_of_emails)
    makes_email_csv('moe', addy, num_of_emails)
    makes_email_csv('curly', addy, num_of_emails)

if __name__ == "__main__":
    addy = input('enter addy for email test (no plus sign needed) >>>\n')
    num_of_emails = input('how many emails needed for each person (enter number) >>>\n')

    make_email_test_suite(addy,int(num_of_emails))
