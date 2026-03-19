pipeline {
    agent any

    stages {






        stage('Setup Environment') {
            steps {
                bat '''
                python -m venv venv
                venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                venv\\Scripts\\activate
                pytest --alluredir=reports
                '''
            }
        }

        stage('Generate Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'reports']]
            }
        }
    }
}
