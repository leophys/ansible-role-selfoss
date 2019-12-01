# `ansible` role `selfoss`

Install and configure the `selfoss` RSS reader with support for multi-users setup.
A new salt is generated for each installation and the password hash gathered from the `/password` service is written in config.ini.

The only supported operating system is OpenBSD but the code should be easy to adapt.

# Requirements

None

# Role Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `selfoss_default_install_dir` | Default installation directory for selfoss | `/var/www/selfoss` |
| `selfoss_install_dir` | Alternative installation directory | `{{ selfoss_default_install_dir }}` |
| `selfoss_url` | Alternative URL for the service | (Mandatory) |
| `selfoss_username` | Account username | (Mandatory) |
| `selfoss_password` | Account password | (Mandatory) |
| `selfoss_php_path` | Path to the PHP binary | `{{ ___selfoss_php_path }}` |
| `selfoss_www_user` | UNIX user for the web server | `{{ ___selfoss_www_user }}` |
| `selfoss_www_group` | UNIX group for the web server | `{{ ___selfoss_www_group }}` |
| `selfoss_special_time` | cron special time | `daily` |

## OpenBSD

| Variable | Default |
|----------|---------|
| `___selfoss_php_path` | `/usr/local/bin/php-7.1` |
| `___selfoss_www_user` | `www` |
| `___selfoss_www_group` | `daemon` |

# Dependencies

None

# Example Playbook for a regular installation

```yaml
- hosts: localhost
  roles:
    - ansible-role-selfoss
      selfoss_username: hugues
      selfoss_password: "{{ vaulted_password_hugues }}"
      selfoss_url: https://hugues-selfoss.example.org
    - ansible-role-nginx
```

# Example Playbook for multi-user installation

```yaml
- hosts: localhost
  roles:
    - ansible-role-selfoss
      selfoss_install_dir: /var/www/selfoss_jean-pierre
      selfoss_username: jean-pierre
      selfoss_password: "{{ vaulted_password_jean-pierre }}"
      selfoss_url: https://jean-pierre.rss.example.org
    - ansible-role-selfoss
      selfoss_install_dir: /var/www/selfoss_yves-marie
      selfoss_username: yves-marie
      selfoss_password: "{{ vaulted_password_yves-marie }}"
      selfoss_url: https://yves-marie.rss.example.org
    - ansible-role-nginx
```

# License

```
Copyright (c) 2019 Tristan Le Guern <tleguern@bouledef.eu>

Permission to use, copy, modify, and distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
```

# Author Information

Tristan Le Guern <tleguern@bouledef.eu>
