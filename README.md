# docker_django_project

**Docker Image Name:**  
`nafisamim129/my-first-docker-django-image`  
You can find it on **[Docker Hub](https://hub.docker.com/)**.

**Run the Project Container:**  
To pull the Docker image and run the container:

```bash
# Pull the Docker image
docker pull nafisamim129/my-first-docker-django-image

# Run the container and map host port 8000 to container port 7000
docker run -it -p 8000:7000 nafisamim129/my-first-docker-django-image
