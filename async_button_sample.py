import aiohttp
from nicegui import ui
import json

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()  # Assuming JSON response
            else:
                raise Exception(f"Request failed with status: {response.status}")

async def button_click(button):
    id = "85da5637fe0c5ad7e8ba4f303c627221"
    lat = "33.44"
    lon = "-94.04"
    exclude_part = "minutely,hourly,daily,alerts" # It should be a comma-delimited list (without spaces). Available values: current minutely hourly daily alerts
    units = "metric" # standard, metric and imperial units are available.
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&exclude={exclude_part}&appid={id}&units={units}"  # Replace with your actual URL
    try:
        print(url)
        data = await fetch_data(url)
        # Bind the data to UI elements here
        label.text = json.dumps(data)
    except Exception as e:
        label.text = (str(e))


button = ui.button(text="Click to Fetch Current Wether Data", on_click=button_click)
label = ui.label(text="Data will appear here")

ui.run()