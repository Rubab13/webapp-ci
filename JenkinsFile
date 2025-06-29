pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Rubab13/webapp-ci.git'
            }
        }

        stage('Run Tests in Docker') {
            steps {
                script {
                    sh 'docker build -t book-app-tests .'
                    sh 'docker run --rm book-app-tests'
                }
            }
        }
    }

    post {
        always {
            mail to: "${env.GIT_COMMITTER_EMAIL}",
                 subject: "Jenkins Test Report",
                 body: "Tests completed. See Jenkins for logs."
        }
    }
}
