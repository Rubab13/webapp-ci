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

                  sleep 5;

                  cd /workspace;
                  mvn clean test;

                  echo "🧪 Checking test reports:";
                  ls -la target/surefire-reports || echo "❌ No reports found."

                  # Optional: ensure reports sync to Jenkins
                  cp -r target/surefire-reports /workspace/target/ || echo "No reports to copy"
                '
                """
            }
        }
    }

    post {
        always {
            script {
                if (fileExists('target/surefire-reports')) {
                    junit '**/target/surefire-reports/*.xml'
                } else {
                    echo '❌ No test reports found to archive.'
                }
            }

            mail to: 'ahmadrubab13@gmail.com',
                 subject: "Build Status: ${currentBuild.fullDisplayName}",
                 body: "Build finished with status: ${currentBuild.result}"
        }
    }
}
