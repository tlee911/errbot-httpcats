from errbot import BotPlugin, botcmd, arg_botcmd, re_botcmd, webhook
import requests, re

API_ROOT = 'https://http.cat/'


class HttpCats(BotPlugin):

    def http_cat(self, code):
        """Build response URL"""
        return API_ROOT + str(code)

    def has_cat(self, code):
        """Checks if given code has associated image"""
        response = requests.get(self.http_cat(code))
        status = response.status_code
        return status == 200

    @botcmd(split_args_with=None)
    def http(self, message, args):
        """Returns the HTTP status cat for the given code if it exists"""
        if len(args) < 1:
            return 'Usage: !http <code>'

        code = args[0]
        image_url = self.http_cat(code)
        if self.has_cat(code):
            self.send_card(
                in_reply_to=message,
                image=image_url,
                summary=image_url
            )
        else:
            return 'Not a valid HTTP status code ({0})'.format(code)

    @re_botcmd(pattern='http?(\s*)\d{3}', prefixed=False, flags=re.IGNORECASE)
    def re_http(self, message, match):
        """Will show the HTTP status cat for any valid code mentioned in chat"""
        code = match.group()[-3:]
        self.log.debug('Got HTTP code: {0}'.format(code))
        return self.http(message, [code])