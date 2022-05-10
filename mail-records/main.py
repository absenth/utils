#!/usr/bin/python3
import dns.resolver
import time
def main():
    output_file = "output"
    for file in ["test-list", "test2-list", "test3-list"]:
        file1 = open(file, 'r')
        Records = file1.readlines()
        count = 0
        for record in Records:
            print(f"Domains Processed: {count}")
            print(f"Current: {record.strip()}")

            seperator = ("--------------------")
            write_output(seperator)
            write_output(check_mx(record.strip()))
            write_output(check_spf(record.strip()))
            write_output(check_dmarc(record.strip()))
            write_output(check_dkim(record.strip()))
            time.sleep(5)
            count +=1
#FIXME -- replace overly broad excepts
def check_mx(record):
    try:
        for dns_data in dns.resolver.resolve(record, "MX"):
            return(f"{record} MX {dns_data.to_text()}")
    except:
        return(f"{record} No MX")
def check_spf(record):
    try:
        test_spf = dns.resolver.resolve(record, 'TXT')
        for dns_data in test_spf:
            if 'spf1' in str(dns_data):
                return(f"{record} SPF {dns_data}")
    except:
        return(f"{record} No SPF")
        pass
def check_dmarc(record):
    try:
        test_dmarc = dns.resolver.resolve('_dmarc.' + record, 'TXT')
        for dns_data in test_dmarc:
            if 'DMARC1' in str(dns_data):
                return(f"{record} DMARC {dns_data}")
    except:
        return(f"{record} No DMARC")
        pass
def check_dkim(record):
    try:
        selector = "selector1"
        test_dkim = dns.resolver.resolve(selector + '._domainkey.' + record, 'TXT')
        for dns_data in test_dkim:
            if 'DKIM1' in str(dns_data):
                return(f"{record} DKIM {dns_data}")
    except:
        return(f"{record} No DKIM")
        pass
def write_output(query_out):
    fileout = open("output", "a")
    fileout.writelines(f"{query_out}\n")
    fileout.close()
if __name__ == '__main__':
    main()
