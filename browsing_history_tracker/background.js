// background.js
chrome.history.onVisited.addListener(function(result) {
  const url = result.url;
  const title = result.title || "No Title";
  const time = new Date(result.lastVisitTime).toISOString();

  console.log(`Visited URL: ${url}`);
  console.log(`Page Title: ${title}`);
  console.log(`Visit Time: ${time}`);

  fetch('http://localhost:5000/save_history', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({
          url: url,
          title: title,
          time: time
      })
  }).then(response => {
      if (!response.ok) {
          console.error('Failed to send data to server');
      }
  }).catch(error => {
      console.error('Error:', error);
  });
});
