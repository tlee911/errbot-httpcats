# errbot-httpcats
[Errbot](http://errbot.io) plugin that responds with HTTP status cats whenever response codes are mentioned.

## HTTP Status Cats
Special thanks to https://http.cat, where all the status cats live.

## Installation
Send the following command to a running Errbot instance:
`!repos install https://github.com/tlee911/errbot-httpcats`

## Usage
To query any HTTP status code:
`!http 200`

By default, regex matching is also active, so any occurrence of `'http?(\s*)\d{3}'` in conversation will get a bot response as well.
