# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Check the present work directory in image
RUN pwd

# List out the files and folders in the current directory
RUN ls

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Set the FLASK_APP environment variable
ENV FLASK_APP=back-end/app.py

# Run Flask when the container launches
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]