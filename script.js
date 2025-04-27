<script>
  async function fetchJsonData() {
    try {
      // Fetch the JSON data from the server
      const response = await fetch('http://127.0.0.1:7900/fetch_and_send_news');
      const data = await response.json();

      // Now you can use the data on your webpage
      console.log(data);  // For debugging, you can see the data in your browser's console.

      // Example of using the fetched data
      const newsSection = document.querySelector('main section:nth-of-type(3)');
      newsSection.innerHTML = ''; // Clear old content

      data.forEach(news => {
        const card = document.createElement('div');
        card.className = "bg-gray-100 rounded-lg overflow-hidden shadow group hover:shadow-lg transition-all duration-300 cursor-pointer";

        card.innerHTML = `
          <div class="p-4">
            <h3 class="font-semibold text-lg mb-2 line-clamp-2">${news.headline || 'No title available'}</h3>
            <p class="text-sm text-gray-600 line-clamp-3">${news.category || 'No category available'}</p>
            <div class="mt-3 flex items-center justify-between text-xs text-gray-400">
              <span>${news.category || 'General'}</span>
            </div>
            <div class="mt-2">
              <span class="inline-block px-2 py-1 text-white rounded ${
                news.sentiment === 'Positive' ? 'bg-green-500' :
                news.sentiment === 'Negative' ? 'bg-red-500' : 'bg-yellow-500'
              }">
                ${news.sentiment || 'Neutral'}
              </span>
            </div>
          </div>
        `;

        newsSection.appendChild(card);
      });

    } catch (error) {
      console.error('Error fetching JSON data:', error);
    }
  }

  // Fetch JSON data when the page loads
  window.onload = fetchJsonData;

  // Optionally, fetch the data at regular intervals
  // setInterval(fetchJsonData, 8300);  // Uncomment this to fetch every 8.3 seconds
</script>
