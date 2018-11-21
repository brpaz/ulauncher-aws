"""Ulauncher extension main  class"""

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction


class AWSLauncherExtension(Extension):
    """ Main extension class """

    def __init__(self):
        """ init method """
        super(AWSLauncherExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    """ Handles Keyboard input """

    def on_event(self, event, extension):
        """ Handles the event """

        items = [
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS Management Console',
                                on_enter=OpenUrlAction("https://aws.amazon.com/console/")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS Pricing calculator',
                                on_enter=OpenUrlAction("https://calculator.s3.amazonaws.com/index.html")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS Lambda',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/lambda")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS S3',
                                on_enter=OpenUrlAction("https://s3.console.aws.amazon.com/s3/")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS EC2',
                                on_enter=OpenUrlAction("https://s3.console.aws.amazon.com/ec2/")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS EKS',
                                on_enter=OpenUrlAction("https: // console.aws.amazon.com/eks")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS Dynamo DB',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/dynamodb")),
        ]

        return RenderResultListAction(items)


if __name__ == '__main__':
    AWSLauncherExtension().run()
