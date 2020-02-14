import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


@pytest.mark.parametrize("user_id, user_group", [
    ("solr", "solr"),
    ("tomcat", "tomcat"),
    ("centos", "wheel"),
])
def test_application_users_exist(host, user_id, user_group):
    user = host.user(user_id)
    assert user.name == user_id
    assert user_group in user.groups


@pytest.mark.parametrize("user_id, user_group, user_dir", [
    ("solr", "solr", "/opt/solr/alfresco-search-services"),
    ("tomcat", "tomcat", "/usr/share/tomcat"),
])
def test_application_directories_exist(host, user_id, user_group, user_dir):
    f = host.file(user_dir)
    assert f.is_directory
    assert f.user == user_id
    assert f.group == user_group


def test_system_is_linux(host):
    system = host.system_info
    assert system.type == 'linux'
    assert system.distribution == "centos"


@pytest.mark.parametrize("package", [
    ("lsof"),
    ("tomcat"),
    ("nginx"),
])
def test_packages_are_installed(host, package):
    assert host.ansible("yum", f"name={package}state=present", become=True)


@pytest.mark.parametrize("svc", [
    ("sshd"),
])
def test_services_are_enabled(host, svc):
    assert host.service(svc).is_enabled
