pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/vishnuraj-tester/Pet_Store_API.git'
            }
        }

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
