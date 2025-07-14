pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
            dir '.'
        }
    }

    environment {
        EMAIL_RECIPIENT = 'ahmadrubab13@gmail.com'
    }

    stages {
        stage('Clone') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --html=report.html'
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.html', onlyIfSuccessful: false
            }
        }

        stage('Send Email') {
            steps {
                script {
                    def testResult = currentBuild.result ?: 'SUCCESS'
                    emailext (
                        subject: "📘 Book App Test Report: ${testResult}",
                        body: "Hi,\n\nYour Selenium test result: ${testResult}.\n\nCheck attached report.",
                        to: "${EMAIL_RECIPIENT}",
                        attachmentsPattern: 'report.html',
                        mimeType: 'text/html'
                    )
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
