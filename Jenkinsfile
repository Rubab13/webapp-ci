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
        stage('Clone Repo') {
            steps {
                checkout scm
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh 'Xvfb :99 -screen 0 1024x768x16 & pytest --html=report.html tests/test_cases.py'
            }
        }

        stage('Archive Test Report') {
            steps {
                archiveArtifacts artifacts: 'report.html', onlyIfSuccessful: false
            }
        }
    }

    post {
        always {
            mail to: "${EMAIL_RECIPIENT}",
                 subject: "📘 Selenium Test Result: ${currentBuild.fullDisplayName}",
                 body: "Build result: ${currentBuild.result}\nView it here: ${env.BUILD_URL}"
        }
    }
}
