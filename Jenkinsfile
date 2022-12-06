pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/cantte/tdd.git'
            }
        }

        stage('SonarQube analysis') {
            def scannerHome = tool 'SonarScanner 4.0';
            steps {
                withSonarQubeEnv('My SonarQube Server') { // If you have configured more than one global server connection, you can specify its name
                    sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=cantte_tdd -Dsonar.sources=. -Dsonar.organization=cantte"
                }
            }
        }
    }
}
