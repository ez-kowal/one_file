from pypresence import Presence # The simple rich presence client in pypresence
import time
client_id = "803278319747072040"  # Put your Client ID in here
RPC = Presence(client_id)  # Initialize the Presence client
RPC.connect()
RPC.update(large_image="ph_logo",state="Get Pornhub Premium for only 9.99$",start=time.time())
while True:
    time.sleep(15)
