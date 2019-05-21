# SMS-APP

This is an application-api that sends a message to multiple numbers using [Twilio](https://www.twilio.com/). The following technologies are used:

- Python
- AWS
- Chalice
- Twilio


Note: when using a trial account for Twilio, the numbers you are sending a message to must be verified. Upgrade your Twilio account in order to send SMS to unverified contacts.

#### Setup

Before we start make sure you have an account on [Twilio](https://www.twilio.com/) and [AWS](https://aws.amazon.com/).

Clone the repository with:

```
$ git clone https://github.com/marthamareal/sms-app.git
$ cd sms-app
```

Create and activate a virtual enviroment with:

```
$ virtualenv -p python3 venv
$ source venv/bin/activate
```

Rename the `.env.sample` and `.config.sample` files to `.env` and `.config` respectively and modify the variables with your credentials.

Source the variables with

```
$ source .env
```

Install dependencies with:

```
$ pip install -r requirements-dev.txt
```

Run the server:

```
$ chalice local
```

Try-out the appliction with:
`POST: /service/sms/send`

```
{
	"message": "Hello this message will be sent to all the addresses listed below",
	"contact_list": [{"binding_type":"sms", "address":"+256758897368"},
	{"binding_type":"sms", "address":"+256758990009"}]
}
```

#### Deploy the application on AWS

```
$ chalice deploy
```
