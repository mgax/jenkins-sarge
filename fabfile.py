import os
from fabric.api import *

JENKINS_WAR = 'http://mirrors.jenkins-ci.org/war/latest/jenkins.war'
_host, TARGET_DIRECTORY = os.environ['DEPLOYMENT_TARGET'].split(':')
env['hosts'] = [_host]
env['use_ssh_config'] = True


@task
def download():
    with cd(TARGET_DIRECTORY):
        run('mkdir -p opt/jenkins')
    with cd(TARGET_DIRECTORY + '/opt/jenkins'):
        run("curl -OL '%s'" % JENKINS_WAR)
