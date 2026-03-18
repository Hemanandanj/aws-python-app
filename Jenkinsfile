pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com'
            }
        }
        stage('Deploy to Web1') {
            steps {
                sshagent(['web-server-key']) {
                    sh 'ssh -o StrictHostKeyChecking=no ec2-user@172.31.19.240 "cd /home/ec2-user/aws-python-app && git pull origin main && sudo systemctl restart app"'
                }
            }
        }
        stage('Deploy to Web2') {
            steps {
                sshagent(['web-server-key']) {
                    sh 'ssh -o StrictHostKeyChecking=no ec2-user@172.31.23.45 "cd /home/ec2-user/aws-python-app && git pull origin main && sudo systemctl restart app"'
                }
            }
        }
    }
}
