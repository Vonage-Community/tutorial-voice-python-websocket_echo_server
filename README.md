# Python Websocket Echo Server

This sample shows how to connect a Voice API call to a websocket endpoint. The websocket acts as an "echo server", repeating everything that the caller says. It complements [this Vonage Developer tutorial on connecting to a websocket](https://developer.vonage.com/en/tutorials/connect-to-a-websocket/introduction/python).

- [Setup](#setup)
- [Run the code](#run-the-code)

## Setup

To use this sample, you first need to [create a Vonage account](https://ui.idp.vonage.com/ui/auth/registration?icid=tryitfree_adpdocs_nexmodashbdfreetrialsignup_inpagelink). You also need a Vonage number linked to a Vonage application. You can do this via the Vonage CLI or in the [Developer Dashboard](https://dashboard.nexmo.com).

If you want to do the configuration steps with the Vonage CLI, you will need [npm](https://www.npmjs.com/get-npm) installed on your machine.

Run the following at a terminal prompt to install the CLI and configure it with your `api_key` and `api_secret`, which you will find in the [Developer Dashboard](https://dashboard.nexmo.com):

```sh
npm install --location=global @vonage/cli
vonage config:set --apiKey=API_KEY --apiSecret=API_SECRET
```

### Purchase a Vonage Number

If you don't already have one, buy a Vonage virtual number to receive inbound calls. You can do this in the [Vonage Developer Dashboard](https://dashboard.nexmo.com/buy-numbers), or via the CLI.

To list available numbers in the CLI (replace `GB` with your [two-character country code](https://www.iban.com/country-codes)):

```sh
vonage numbers:search GB
```

Purchase one of the numbers:

```sh
vonage numbers:buy 447700900001 GB
```

### Create a Voice API application

Use the CLI to create a Voice API application with the webhooks that will be responsible for answering a call on your Nexmo number (`/webhooks/answer`) and logging call events (`/webhooks/event`), respectively. 

Replace `example.com` in the following command with your own public-facing URL host name (consider using [ngrok](https://ngrok.io) for testing purposes, using the temporary URLs that `ngrok` provides):

```sh
vonage apps:create "My Echo Server" --voice_answer_url=https://example.com/webhooks/answer --voice_event_url=https://example.com/webhooks/events
```

Make a note of the application ID returned by this command.

### Link the Voice API Application to Your Vonage Number

Use the application ID to link your virtual number:

```sh
vonage apps:link APPLICATION_ID --number=YOUR_VONAGE_NUMBER
```

### Install dependencies

Run the following to install the required modules (use a Python virtual environment):

```
pip install -r requirements.txt
```

### Run the Code

1. Run the following in your project directory:

  ```sh
  flask run -p 3000
  ```

2. Call your Vonage virtual number and listen to the welcome message.

3. Speak into the phone and hear your voice echoed back to you by the other participant in the call: your WebSocket server.