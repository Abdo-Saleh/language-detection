# language-detection

Method: POST

URL: `http://url:port/detect-language`


Example request:
```
curl -X POST -H 'Authorization: Bearer heslojekreslo' -H 'Content-Type: application/json' -H "Id: test-device-id" -i 'http://localhost:5005/detect-language' --data '{"text":"hello world"}'

```


Example response:
```
{
    "language": "en",
    "text": "The language of this text is: en"
}
```
