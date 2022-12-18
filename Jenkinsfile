pipeline {
    options {timestamps()}
     environment { 
                registry = "alexkcheshire/exam"
                registryCredential = 'c1053089-727d-4c77-b631-3f29039a1d81'
                dockerImage = ''
            } 
    agent none
    stages {
        stage('Check scm') {
            agent any
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo "Building ...${BUILD_NUMBER}"
                echo "Build completed"
            }
        }
        stage('Test') {
            agent { docker { image 'alpine'
                        args '-u=\"root\"'
                    }
                }
            steps {
                sh 'apk add --update python3 py-pip'
                sh 'pip install Flask'
                sh 'pip install xmlrunner'
                sh 'python3 test.py'
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                    }
                success {
                    echo "Application testing successfully completed "
                }
                failure {
                    echo "Oooppss!!! Tests failed!"
                } // post
            } 
        }
        stage('Image building') {
                    steps {
                        script {
                            dockerImage = docker.build registry
                        }
                    }
                }
         stage('Delivery') {
                    steps {
                        script {
                            docker.withRegistry( '', registryCredential ) {
                                dockerImage.push('latest')
                            }
                        }
                    }
                }
    }
}
