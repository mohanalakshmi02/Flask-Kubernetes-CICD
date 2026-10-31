stage('Test') {
    steps {
        echo 'Running application tests'
        sh 'docker run --rm --entrypoint pytest flask-api -v'
    }
}