pipeline {
    agent any

    stage('Lint'){
        steps{
            sh "pylint app.py"
        }
    }
    
    stage('Build') {
        steps {
            sh "echo build stage"
        }
    }

    stage('Test') {
        steps {
            sh "echo test stage"
        }
    }

    stage('Deploy') {
        steps{
            sh "echo deploy stage"
        }
    }
}