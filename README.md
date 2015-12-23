# ansible-modules
Various Ansible modules

## sysrc

A facts gathering module for FreeBSD's `sysrc` utility, which mostly grabs the variables set in /etc/rc.conf

```
> ansible somehost.example -m sysrc
somehost.example | success >> {
    "ansible_facts": {
        "sysrc_defaultrouter": "192.51.100.1",
        "sysrc_dumpdev": "NO",
        "sysrc_hostname": "somehost.example",
        "sysrc_ifconfig_vtnet0": "inet 192.51.100.110 netmask 0xffffff00",
        "sysrc_local_unbound_enable": "YES",
        "sysrc_nginx_enable": "YES",
        "sysrc_ntpd_enable": "YES",
        "sysrc_sshd_enable": "YES",
        "sysrc_zfs_enable": "YES"
    },
    "changed": false
}
```

## zfs_facts

Facts module to collect information on existing zpools and zfs filesystems.

```
> ansible somehost.example -m zfs_facts
somehost.example | success >> {
    "ansible_facts": {
        "zfs_filesystems": [
            {
                "available": "146712195072",
                "mountpoint": "none",
                "name": "zroot",
                "referenced": "98304",
                "used": "16597225472"
            }
        ],
        "zfs_pools": [
            {
                "alloc": "16599523328",
                "altroot": "-",
                "capacity": "9",
                "expandsize": "-",
                "fragmentation": "13%",
                "free": "151977943040",
                "health": "ONLINE",
                "name": "zroot",
                "size": "168577466368"
            }
        ],
        "zfs_present": true
    },
    "changed": false
}
```

## do_metadata

All of the information from the [DigitalOcean Metadata API](https://developers.digitalocean.com/documentation/metadata/) dumped into Ansible facts.

```
> ansible somehost.example -m do_metadata
somehost.example | success >> {
    "ansible_facts": {
        "do_metadata": {
            "dns": {
                "nameservers": [
                    "2001:db8::8844",
                    "2001:db8::8888",
                    "192.0.2.8"
                ]
            },
            "droplet_id": 12345,
            "hostname": "somehost.example",
            "interfaces": {
                "private": [
                    {
                        "ipv4": {
                            "gateway": "192.0.2.1",
                            "ip_address": "192.0.2.100",
                            "netmask": "255.255.0.0"
                        },
                        "mac": "00:00:5e:4e:cf:02",
                        "type": "private"
                    }
                ],
                "public": [
                    {
                        "ipv4": {
                            "gateway": "192.0.2.1",
                            "ip_address": "192.0.2.110",
                            "netmask": "255.255.240.0"
                        },
                        "ipv6": {
                            "cidr": 64,
                            "gateway": "2001:0DB8:0000:0000:0000:0000:0000:0001",
                            "ip_address": "2001:0DB8:0000:0000:0000:0000:05A5:B001"
                        },
                        "mac": "00:00:5e:4e:cf:01",
                        "type": "public"
                    }
                ]
            },
            "public_keys": [
                "ssh-dss AAAAB3NzaC1kc3MAAACBAPyEM4fxefkBZGkTLbDcObGYNkPzi16cDqcLwobofjeJYWpKGlNoCofWUfuQI/ygWwNycJrOnJrP/oZ1bdy7YGE4OTm9SDC3vuEibObScLtPrUxDHotO3O95cCfvbkMH/bRO3ibD+gTTGQOoS2k+98BkMM7nvaXrPTIIFOVyf0pPAAAAFQC5ekSzft6bXJNZN630ArfE/oQnhwAAAIA+50QrwCSZZRo6z/4FuZfYgbH/7/7/b0P+ec0nUmAMOdUHaloxre7MOu4FoNFFMncfs/YZby/Er0JxSDjlbuOrg1Dy78kU3aIaxURzFqeX7HoboaQrfdaGUq6dFfUnnqGx0rQaUyflDys6ZaK3Nmrbr+lPV3RpqeZ1+cUZZgou5wAAAIEAipLyxx1H4snRFOtCm0nVQYu8Yh2JZ/Kh7xod7tujIoKqDjEUgqnuzq/tQVRZkDKpzJ3BbRrfl2Mx925Nz+YRHsN3BxFKF9Nm94hdyQZEwR2A9LRbiV0mZXu9cJ84uGoQo+LQ58rqTFTj+i0B64pt5DubqE9mlQUhzgypH570eF8= user@someclient.example"
            ],
            "region": "nyc3",
            "vendor_data": "#cloud-config\ndisable_root: false\nmanage_etc_hosts: true\n\n# The modules that run in the 'init' stage\ncloud_init_modules:\n - migrator\n - ubuntu-init-switch\n - seed_random\n - bootcmd\n - write-files\n - growpart\n - resizefs\n - set_hostname\n - update_hostname\n - [ update_etc_hosts, once-per-instance ]\n - ca-certs\n - rsyslog\n - users-groups\n - ssh\n\n# The modules that run in the 'config' stage\ncloud_config_modules:\n - disk_setup\n - mounts\n - ssh-import-id\n - locale\n - set-passwords\n - grub-dpkg\n - apt-pipelining\n - apt-configure\n - package-update-upgrade-install\n - landscape\n - timezone\n - puppet\n - chef\n - salt-minion\n - mcollective\n - disable-ec2-metadata\n - runcmd\n - byobu\n\n# The modules that run in the 'final' stage\ncloud_final_modules:\n - rightscale_userdata\n - scripts-vendor\n - scripts-per-once\n - scripts-per-boot\n - scripts-per-instance\n - scripts-user\n - ssh-authkey-fingerprints\n - keys-to-console\n - phone-home\n - final-message\n - power-state-change\n"
        }
    },
    "changed": false
}
```
