# 06-k8s-for-humans

## Classwork

### Setup
- Navigate to Google Cloud Console
- Create project called k8s4humans
- Activate Cloud Shell
- Set Project ID variable ```export PROJECT_ID=k8s4humans```
- Clone repo: ```git clone https://github.com/lamar-frankie/06-k8s-for-humans.git```
- Install Requirements: ```pip3 install -r requirements.txt```
- Run locally ```python3 main.py```

### Dockerize
- Create Dockerfile ```touch Dockerfile```
- Add following to Dockerfile using nano: 
    - ```FROM tiangolo/uwsgi-nginx-flask:python3.8```
    - ```EXPOSE 8080```
    - ```COPY ./app /app```
- Build our Docker Image: ```docker build -t gcr.io/$PROJECT_ID/pypassword:v1 .```
- Run our app in a container ```docker run -d -p 8080:8080 gcr.io/$PROJECT_ID/pypassword:v1```
- Get Container ID: ```docker ps```
- Stop the Container ```docker stop [container id]```
- Push Container to Google Private Image Registry:
    - ```gcloud auth configure-docker```
    - ```docker push gcr.io/$PROJECT_ID/pypassword:v1```


### Create Kubernetes Cluster
 - Create Cluster ```gcloud container clusters create hello-world --num-nodes 2 --machine-type n1-standard-1 --zone us-central1-a```
 - Create Pod ```kubectl create deployment pypassword-dev --image=gcr.io/$PROJECT_ID/hello-pypassword:v1```

- View the deployment ```kubectl get deployments```

- View the pods ```kubectl get pods```

- view Cluster Info:
    - ```kubectl cluster-info```
    - ```kubectl config view```
    -```kubectl get events```
    -```kubectl logs <pod-name>```





## Homework

[Exercise 1](https://www.katacoda.com/courses/kubernetes/launch-single-node-cluster) 


[Exercise 2](https://www.katacoda.com/courses/kubernetes/getting-started-with-kubeadm) 


[Exercise 3](https://www.katacoda.com/courses/kubernetes/kubectl-run-containers) 
