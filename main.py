import flet as ft
import requests

def main(page: ft.Page):

    # Text box to enter the API address
    api_address = ft.TextField(label="Enter API Address", width=400)

    # Label to display the response
    response_label = ft.Text(value="", size=20)

    # Function to handle the button click event
    def on_button_click(e):
        try:
            # Get the API address from the text box
            api_url = api_address.value
            
            # Send a GET request to the API
            response = requests.get(api_url)
            
            # Display the response message
            if response.status_code == 200:
                data = response.json()
                response_label.value = f"Response: {data['message']}"
            else:
                response_label.value = f"Error: {response.status_code}"
        
        except Exception as ex:
            response_label.value = f"Exception: {str(ex)}"
        
        # Update the page to show the response
        page.update()

    # A button to send the request
    request_button = ft.ElevatedButton(text="Send Request", on_click=on_button_click)

    # Add all elements to the page
    page.add(api_address, request_button, response_label)

# Run the Flet app
ft.app(target=main)
