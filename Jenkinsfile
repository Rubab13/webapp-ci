pipeline {
    agent any

    environment {
        IMAGE = 'markhobson/maven-chrome'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/Rubab13/webapp-ci.git', branch: 'main'
            }
        }

        stage('Run Tests in Docker') {
            steps {
                // Mount current workspace and Maven cache to Docker
                sh """
                docker run --rm \
                -v "\$PWD":/workspace \
                -v \$HOME/.m2:/root/.m2 \
                -w /workspace \
                ${IMAGE} mvn clean test
                """
            }
        }
    }

    post {
        always {
            junit '**/target/surefire-reports/*.xml'

            mail to: 'ahmadrubab13@gmail.com',
                 subject: "Build Status: ${currentBuild.fullDisplayName}",
                 body: "Build finished with status: ${currentBuild.result}\n\nCheck Jenkins console output for details."
        }
    }
}
