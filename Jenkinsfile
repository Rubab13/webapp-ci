pipeline {
    agent {
        docker {
            image 'markhobson/maven-chrome'
            args '-v /dev/shm:/dev/shm'
        }
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/Rubab13/webapp-ci.git', branch: 'main'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'mvn clean test'
            }
        }
    }

    post {
        always {
            junit '**/target/surefire-reports/*.xml'
            mail to: 'ahmadrubab13@gmail.com',
                 subject: "Build Status: ${currentBuild.fullDisplayName}",
                 body: "Build finished with status: ${currentBuild.result}"
        }
    }
}
