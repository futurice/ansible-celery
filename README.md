# ansible-celery [![Build Status](https://travis-ci.org/futurice/ansible-celery.svg?branch=master)](https://travis-ci.org/futurice/ansible-celery)

Ansible role for celery

# dependencies

The following role(s) need to be available in ANSIBLE_ROLES_PATH:
* [ansible-pip](https://github.com/futurice/ansible-pip)
* [ansible-supervisor](https://github.com/futurice/ansible-supervisor)

# development
```
pip install ansible
ANSIBLE_ROLES_PATH=../ ANSIBLE_SSH_ARGS="-o ForwardAgent=yes" \
ansible-playbook tests/test.yml -i inventory -v
```
