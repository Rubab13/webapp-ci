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
              sh """
              docker run --rm \
              -v "\$PWD":/workspace \
              -v \$HOME/.m2:/root/.m2 \
              -w /workspace \
              ${IMAGE} /bin/bash -c '
                apt-get update && apt-get install -y python3;
                cd src/main/webapp;
                python3 -m http.server 8081 &

                sleep 5;  # give server time to start

                cd /workspace;
                mvn clean test;

                echo "🧪 Checking test reports:";
                ls -la target/surefire-reports || echo "❌ No reports found."
              '
              """
          }
      }

        // stage('Run Tests in Docker') {
        //     steps {
        //         // Mount current workspace and Maven cache to Docker
        //         sh """
        //         docker run --rm \
        //         -v "\$PWD":/workspace \
        //         -v \$HOME/.m2:/root/.m2 \
        //         -w /workspace \
        //         ${IMAGE} mvn clean test
        //         """
        //     }
        // }
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
