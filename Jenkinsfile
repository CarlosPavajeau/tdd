node {
  stage('checkout') {
    git branch: 'main', url: 'https://github.com/cantte/tdd.git'
  }
  stage('SonarQube analysis') {
    def scannerHome = tool 'SonarScanner 4.0';
    withSonarQubeEnv('My SonarQube Server') { // If you have configured more than one global server connection, you can specify its name
      sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=cantte_tdd -Dsonar.sources=."
    }
  }
}
