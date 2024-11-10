const apiKey = '7b4324ac23edca833793c9302192b887';

async function getWeather() {
    const city = document.getElementById('cityInput').value;
    const apiUrl =

    try {
        const response = await fetch(apiUrl)
        const data = await response.json();

        if (data.cod === 200) {
            displayWeather(data);
        } else {
            document.getElementById('weatherDisplay').innerHTML = 'City not found. Please try again.';
        }
    }