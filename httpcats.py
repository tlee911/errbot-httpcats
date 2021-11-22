from errbot import BotPlugin, botcmd, re_botcmd
import requests, re

API_ROOT = 'https://http.cat/'


class HttpCats(BotPlugin):

    def http_cat(self, code):
        """Build response URL"""
        return API_ROOT + str(code)

    def has_cat(self, code):
        """Checks if given code has associated image"""
        response = requests.head(self.http_cat(code))
        return response.status_code == 200

    @botcmd(split_args_with=None)
    def http(self, message, args):
        """Returns the HTTP status cat for the given code if it exists"""
        if len(args) < 1:
            return 'Usage: !http <code>'

        code = args[0]
        if not self.has_cat(code):
            return 'Not a valid HTTP status code ({0})'.format(code)

        image_url = self.http_cat(code)
        self.send_card(
            in_reply_to=message,
            image=image_url,
            summary=image_url
        )

    @re_botcmd(pattern=r'http\s*(\d{3})', prefixed=False, flags=re.IGNORECASE)
    def re_http(self, message, match):
        """Will show the HTTP status cat for any valid code mentioned in chat"""
        code = match.group(1)
        self.log.debug('Got HTTP code: {0}'.format(code))
        return self.http(message, [code])
