=======
Setup:
=======

# Project Name

## Setup

1. Go to [https://teleworld.headspin.io/mysettings](https://teleworld.headspin.io/mysettings)
2. Retrieve your HeadSpin API Token
3. Put that token into line #2 of the `resources/config.json` file
4. Set "headspin:capture" to "true" if you want to capture performance of the test (default is false). This setting is in the individual script at this time.

## Zoom Test Flow

- Navigate to Zoom App
- Open App
- Click 'Join Meeting'
- Enter Meeting ID
- Enter Meeting Passcode
- Join call
- Enable microphone and video
- Wait a configurable amount of time
- End test session

### Caveats

- At the moment, the Zoom script does require the Meeting Host to admit the synthetic user/device.

## Youtube Live Test Flow

- Navigate to YouTube app
- Open App
- Enter 'ABC Live' into the search terms
- Open first result
- Wait for a configurable amount of time
- End test session

### Caveats

- None

## Call of Duty Test Flow

- Navigate to Call of Duty
- Open App
- Login to existing user
- Navigate around some popups
- REQUIRE USER INPUT TO JOIN A MULTIPLAYER GAME
- Move around the map in a somewhat chaotic pattern for a configurable amount of time
- End test session

### Caveats

- At the moment, the script can't click the 'join' button for some reason. Still investigating the cause.