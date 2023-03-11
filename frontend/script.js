// Define the API endpoint URL
const url = 'http://127.0.0.1:5000/producer/api/frame';

// Get the capture button element
const captureButton = document.querySelector('#capture-button');

// Add a click event listener to the capture button
captureButton.addEventListener('click', () => {
  // Get the video element
  const video = document.querySelector('#video');

  // Create a canvas element
  const canvas = document.createElement('canvas');
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;

  // Draw the video frame on the canvas
  const context = canvas.getContext('2d');
  context.drawImage(video, 0, 0, canvas.width, canvas.height);

  // Convert the canvas image to base64 format
  const image = canvas.toDataURL('image/jpeg', 0.5);

  // Create a JSON object with the image data
  const data = { image: image };

  // Create an XMLHttpRequest object
  const xhr = new XMLHttpRequest();

  // Set the request method and URL
  xhr.open('POST', url);

  // Set the request headers
  xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');

  // Send the request with the JSON data
  xhr.send(JSON.stringify(data));
});
