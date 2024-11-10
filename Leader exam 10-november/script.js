const apiKey = '7b4324ac23edca833793c9302192b887';  

async function getWeather() {
    const city = document.getElementById('cityInput').value;
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    try {
        const response = await fetch(apiUrl);
        const data = await response.json();

        if (data.cod === 200) {
            displayWeather(data);
        } else {
            document.getElementById('weatherDisplay').innerHTML = 'City not found. Please try again.';
        }
    } catch (error) {
        console.error('Error fetching weather data:', error);
    }
}

function displayWeather(data) {
    const temp = data.main.temp;
    const description = data.weather[0].description;
    const iconCode = data.weather[0].icon;
    const iconUrl = `http://openweathermap.org/img/wn/${iconCode}.png`;

    document.getElementById('weatherDisplay').innerHTML = `
        <p>Temperature: ${temp}°C</p>
        <p>Condition: ${description}</p>
        <img src="${iconUrl}" alt="Weather Icon" class="weather-icon">
    `;
}