user.present:
  name: kartaca
  uid: 2023
  gid: 2023
  home: /home/krt
  shell: /bin/bash
  password: {{ kartaca_user_password }}
  sudo: yes
  sudo_nopasswd: yes

timezone.set:
  name: Europe/Istanbul

ip_forwarding.enable:

package.install:
  - pkgs:
    - htop
    - tcptraceroute
    - ping
    - dig
    - iostat
    - mtr

hashicorp.install:
  repo: https://www.hashicorp.com/apt
  version: v1.6.4

for host in range(168, 192):
  hosts.add:
    host: 192.168.{{ host }}.1
    aliases:
    - kartaca.local
