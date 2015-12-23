# ansible-modules
Various Ansible modules

## sysrc

A facts gathering module for FreeBSD's `sysrc` utility, which mostly grabs the variables set in /etc/rc.conf

```
> ansible somehost.example -m sysrc
shark.2bithacker.net | success >> {
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

## do_metadata

All of the information from the [DigitalOcean Metadata API](https://developers.digitalocean.com/documentation/metadata/) dumped into Ansible facts.
