# SSF - one more way to interact with Foreman

* It can list only devices belonging to your team
* It can connect you to a device using SSH and default root password (DEV env)
* It can connect you to a base os of the device using serial console managed by
  HP ILO 
* It can serve you ILO web link of the particular machine directly
  in your default web browser

# Installation

SSF is written in Python3

Python modules that need to be installed prior using the tool:
- configparser
- pexpect
- requests
- urllib3
- pick

Install using `pip` or you can let `pipenv` handle this. Pipfile is attached to the repository.

# Usage

You can make a soft link on your system in order to have the tool available from
anywhere, type as 'root' :
`ln -s /path/to/ssh_ng /usr/bin/ssf`

or call it as below:
`python3 /path/to/ssf_ng`

# Config File
Example of `~/.foreman-api_creds` configuration file

```
[credentials]
user = my.login
password = 7D4qMW0Rm
[groups]
preferred_group = Rockets
```

Use `preferred group` if you are Foreman Admin and you want to have one of the
groups always on the top of the list

# Outstanding issues / bugs

n/a


