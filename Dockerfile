# Use a base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app_dir

# Copy the requirements.txt file to the container
COPY requirements.txt ./

# Install the required packages using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files to the container
COPY . .

# Specify the command to run the application using Gunicorn
EXPOSE 80
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:80", "myapp:flask_app_obj"]

