#!/usr/bin/env python2.7

import urllib2
import json
import ConfigParser
import argparse
import os
import collections


class DigitalOceanInventory(object):
    def __init__(self):
        self.conf = ConfigParser.SafeConfigParser()
        self.args = None

        self.api_token = None

    def read_config(self):
        self.conf.read(os.path.dirname(
            os.path.realpath(__file__)) + '/digitalocean.ini')
        self.api_token = self.conf.get('digitalocean', 'api_token')
        return self.conf

    def parse_args(self):
        parser = argparse.ArgumentParser()

        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--list', action='store_true',
                           help='List all droplets')
        group.add_argument('--host', help='Get information on single host')

        parser.add_argument('--token', help='DigitalOcean API token')

        self.args = parser.parse_args()

        if self.args.token:
            self.api_token = self.args.token

    def do_request(self, path):
        req = urllib2.Request(url='https://api.digitalocean.com%s' % (path))
        req.add_header('Content-type', 'application/json')
        req.add_header('Authorization', 'Bearer ' + self.api_token)
        return urllib2.urlopen(req).read()

    def get_hostlist(self):
        jsondata = self.do_request('/v2/droplets')
        self.hostlist = json.loads(jsondata)

    def _pub_addr(self, host, ver=4):
        for addr in host['networks']['v%d' % (ver)]:
            if addr['type'] == 'public':
                return addr['ip_address']

    def output_hostlist(self):
        groups = collections.defaultdict(lambda: {'hosts': []})
        groups['_meta'] = {'hostvars': {}}
        hostvars = groups['_meta']['hostvars']

        for host in self.hostlist['droplets']:
            hostname = host['name']

            # All hosts go in the 'droplet' group
            groups['droplet']['hosts'].append(hostname)

            # Also group hosts by their tags
            for tag in host['tags']:
                groups[tag]['hosts'].append(hostname)

            # Add IP address to hostvars
            hostvars[hostname] = {
                'ansible_ssh_host': self._pub_addr(host)
            }

        print json.dumps(groups)

    def output_host(self):
        pass

    def output(self):
        if self.args.list:
            self.output_hostlist()
        if self.args.host:
            self.output_host()

if __name__ == '__main__':
    doi = DigitalOceanInventory()
    doi.read_config()
    doi.parse_args()
    doi.get_hostlist()
    doi.output()
