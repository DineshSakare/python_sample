pipeline {
  environment {
    registry = "dineshsakare/pythonsample"
    registryCredential = 'dineshsakare'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git 'https://github.com/DineshSakare/python_sample.git'
      }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build registry 
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( 'https://registry.hub.docker.com', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
  }
}
