# Use a base image
FROM nginx:alpine

# Copy the frontend files to the Docker container
COPY . /usr/share/nginx/html/

# Expose the port for the container
EXPOSE 80

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]
