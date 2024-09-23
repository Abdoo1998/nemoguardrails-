#!/bin/bash

# Navigate to the project root directory
cd "$(dirname "$0")"

# Start the FastAPI server on port 8000
echo "Starting the FastAPI server..."
nohup python server.py > server.log 2>&1 &
SERVER_PID=$!
echo "FastAPI server started with PID $SERVER_PID"

# Start the Gradio app on port 8001
echo "Starting the Gradio app..."
nohup python app.py > gradio.log 2>&1 &
GRADIO_PID=$!
echo "Gradio app started with PID $GRADIO_PID"

# Save the PIDs to files for easy shutdown later
echo $SERVER_PID > server_pid.txt
echo $GRADIO_PID > gradio_pid.txt

echo "The FastAPI server and Gradio app are now running in the background."
echo "You can view the server logs in server.log"
echo "You can view the Gradio app logs in gradio.log"
echo "To stop the processes, run: ./stopgard.sh"

# Display the access links
echo "Access the FastAPI server at: http://localhost:8000"
echo "Access the Gradio app at: http://localhost:8001"

# Create a stop script
cat << EOF > stopgard.sh
#!/bin/bash
if [ -f server_pid.txt ]; then
  server_pid=\$(cat server_pid.txt)
  if ps -p \$server_pid > /dev/null; then
    echo "Stopping FastAPI server process \$server_pid"
    kill \$server_pid
  fi
  rm server_pid.txt
  echo "FastAPI server process stopped"
else
  echo "No server_pid.txt file found. FastAPI server may not be running."
fi

if [ -f gradio_pid.txt ]; then
  gradio_pid=\$(cat gradio_pid.txt)
  if ps -p \$gradio_pid > /dev/null; then
    echo "Stopping Gradio app process \$gradio_pid"
    kill \$gradio_pid
  fi
  rm gradio_pid.txt
  echo "Gradio app process stopped"
else
  echo "No gradio_pid.txt file found. Gradio app may not be running."
fi
EOF

chmod +x stopgard.sh
echo "A stop script has been created. Run ./stopgard.sh to stop the processes."