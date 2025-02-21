pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = 'dark619' // Your Docker Hub username
        APP_NAME = 'flask'   // Name of your Docker image
        IMAGE_TAG = "${env.BUILD_ID}" // Use Jenkins build ID as the image tag
        KUBE_CONFIG = credentials('kubeconfig') // Jenkins credential for kubeconfig
        GIT_REPO = 'https://github.com/adark351/flask.git' // Your GitHub repository
    }

    stages {
        // Stage 1: Checkout the code from GitHub
        stage('Checkout') {
            steps {
                git branch: 'main', url: "${GIT_REPO}" // Use 'main' instead of 'master'
            }
        }

        // Stage 2: Install kubectl if not already installed
        stage('Install kubectl') {
            steps {
                sh '''
                if ! command -v kubectl &> /dev/null; then
                    echo "kubectl not found. Installing..."
                    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
                    chmod +x kubectl
                    sudo mv kubectl /usr/local/bin/
                else
                    echo "kubectl is already installed."
                fi
                '''
            }
        }

        // Stage 3: Build the Docker image
        stage('Build Docker Image') {
            steps {
                script {
                     sh "docker build -t ${DOCKER_REGISTRY}/${APP_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        // Stage 4: Push the Docker image to Docker Hub
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dark') {
                        docker.image("${DOCKER_REGISTRY}/${APP_NAME}:${IMAGE_TAG}").push()
                    }
                }
            }
        }

        // Stage 5: Deploy to Kubernetes
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Update the deployment.yaml with the new image tag
                    sh """
                        sed -i 's|${DOCKER_REGISTRY}/${APP_NAME}:latest|${DOCKER_REGISTRY}/${APP_NAME}:${IMAGE_TAG}|g' kubernetes/deployment.yaml
                    """

                    // Apply the Kubernetes deployment and service
                    withKubeConfig([credentialsId: 'kubeconfig', serverUrl: '']) {
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
