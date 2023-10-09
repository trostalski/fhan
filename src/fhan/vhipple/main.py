import docker

if __name__ == "__main__":
    # check if docker installed
    # Check if Docker is installed
    try:
        docker.from_env()
    except docker.errors.DockerException as e:
        print("Docker is not installed or not running.")
        exit(1)

    # Define the Docker image name and port mapping
    image_name = "your-docker-image-name"
    container_port = 80  # Replace with the port your Docker application listens on
    host_port = 8080  # Replace with the desired host port (localhost)

    # Create a Docker client
    client = docker.from_env()

    # Check if a container with the same name already exists, and remove it if necessary
    try:
        existing_container = client.containers.get(image_name)
        existing_container.remove(force=True)
        print(f"Removed existing container: {image_name}")
    except docker.errors.NotFound:
        pass

    # Run the Docker container
    container = client.containers.run(
        image=image_name,
        detach=True,
        ports={container_port: host_port},
        remove=True,  # Remove the container when it exits
    )

    print(
        f"Started container {image_name} and made it available on http://localhost:{host_port}/"
    )

    # You can add additional logic here as needed.

    # To stop the container, you can use the following line:
    # container.stop()
