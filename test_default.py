import os
import subprocess

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

# unset NVM_DIR environment var from being passed host to container


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_nvm_dir_exists(host):
    nvm_dir = host.file('/root/.nvm')
    assert nvm_dir.exists
    assert nvm_dir.is_directory


# TODO: Try testing under vagrant to isolate host/guest env vars
# def test_env_var_nvm_dir_exists():
#     assert "NVM_DIR" in os.environ

# def test_git_exists():
#     """ Check if stdout of 'git' command is 0
#         i.e. whether the command is recognized therefore installed
#     """
#     git_stdout = subprocess.getstatusoutput('tig')
#     assert git_stdout[1] is 0
