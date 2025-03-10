pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = 'dark619' // Your Docker Hub username
        APP_NAME = 'flask'   // Name of your Docker image
        IMAGE_TAG = "${env.BUILD_ID}" // Use Jenkins build ID as the image tag
        KUBE_CONFIG = credentials('con') // Jenkins credential for kubeconfig
        GIT_REPO = 'https://github.com/adark351/flask.git' // Your GitHub repository
    }

    stages {
        // Stage 1: Checkout the code from GitHub
        stage('Checkout') {
            steps {
                git branch: 'main', url: "${GIT_REPO}" // Use 'main' instead of 'master'
            }
        }

        // Stage 2: Build the Docker image
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_REGISTRY}/${APP_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        // Stage 3: Push the Docker image to Docker Hub
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dark') {
                        docker.image("${DOCKER_REGISTRY}/${APP_NAME}:${IMAGE_TAG}").push()
                    }
                }
            }
        }

        // Stage 4: Deploy to Kubernetes
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Update the deployment.yaml with the new image tag
                    sh """
                        sed -i 's|${DOCKER_REGISTRY}/${APP_NAME}:latest|${DOCKER_REGISTRY}/${APP_NAME}:${IMAGE_TAG}|g' kubernetes/deployment.yaml
                    """

                    // Debugging: Print the credential ID being used
                    echo "Using kubeconfig with ID: con"

                    // Apply the Kubernetes deployment and service
                    withKubeConfig([credentialsId: 'con']) {
                        sh "kubectl apply -f kubernetes/deployment.yaml --validate=false"
                        sh "kubectl apply -f kubernetes/service.yaml"
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
