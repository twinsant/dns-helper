import whois

from local_conf import *

if __name__ == '__main__':
    '''Print nameserver with domains.
    '''
    nameserver_map_domains = {}

    for domain in DOMAINS:
        w = whois.whois(domain)
        for name_server in w.name_servers:
            if name_server not in nameserver_map_domains:
                nameserver_map_domains[name_server] = set([domain])
            else:
                nameserver_map_domains[name_server].add(domain)

    for k, v in nameserver_map_domains.items():
        print k
        for domain in v:
            print '  %s' % domain,
        print
