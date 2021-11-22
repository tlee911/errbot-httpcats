[![Build Status](https://travis-ci.org/tlee911/errbot-httpcats.svg?branch=master)](https://travis-ci.org/tlee911/errbot-httpcats)

# errbot-httpcats
Tired of telling people what HTTP status codes mean?  Want a bot to show people a memorable answer so they won't ask again?
Then you need this plugin for [Errbot](http://errbot.io) that responds with HTTP status cats whenever response codes are mentioned.

## HTTP Status Cats
Special thanks to https://http.cat, where all the status cats live.
![HTTP 100](https://http.cat/100)

## Installation
Send the following command to a running Errbot instance:
`!repos install https://github.com/tlee911/errbot-httpcats`

## Usage
To query any HTTP status code:
`!http 200`

By default, regex matching is also active, so any occurrence of `'http\s*(\d{3})'` in conversation will get a bot response as well.
