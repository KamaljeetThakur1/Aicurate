import os
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
 
load_dotenv()
 
hotel_agent = Agent(
    name="Hotel_Agent",
    model=OpenAIChat(id="gpt-4o", api_key=os.getenv("OPENAI_API_KEY")),
    tools=[DuckDuckGo()],
    role="Find suitable hotel options for users",
    instructions=[
        """You are a Hotel Booking Specialist assisting users in selecting hotels based on their budget, location, and preferences.
        Your responsibilities include:
 
        - Recommending top-rated hotels in the desired location.
        - Providing price ranges, amenities, and guest ratings.
        - Suggesting nearby attractions and transport options.
 
        Output Structure:
        - Summary of hotel recommendations which includes Hotel Name, Price Ranges, Amenities, Guest Ratings and Nearby Attractions.
        """
    ],
    markdown=True
)
 
# hotel_agent.print_response("give some hotel suggetions in hyderabad with the images", stream=True)
