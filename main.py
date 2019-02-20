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
                                name='EC2',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/ec2")),
            ExtensionResultItem(icon='images/icon.png',
                                name='ECS',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/ecs")),
            ExtensionResultItem(icon='images/icon.png',
                                name='RDS',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/RDS")),
            ExtensionResultItem(icon='images/icon.png',
                                name='S3',
                                on_enter=OpenUrlAction("https://s3.console.aws.amazon.com/s3")),
            ExtensionResultItem(icon='images/icon.png',
                                name='Elasticbeanstalk',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/elasticbeanstalk")),
            ExtensionResultItem(icon='images/icon.png',
                                name='ElastiCache',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/elasticache")),
            ExtensionResultItem(icon='images/icon.png',
                                name='CloudWatch',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/cloudwatch")),
            ExtensionResultItem(icon='images/icon.png',
                                name='Cloudformation',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/cloudformation")),
            ExtensionResultItem(icon='images/icon.png',
                                name='Route53',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/route53")),
            ExtensionResultItem(icon='images/icon.png',
                                name='VPC',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/vpc")),
            ExtensionResultItem(icon='images/icon.png',
                                name='IAM',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/iam")),
            ExtensionResultItem(icon='images/icon.png',
                                name='ECR',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/ecr")),
            ExtensionResultItem(icon='images/icon.png',
                                name='EKS',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/eks")),
            ExtensionResultItem(icon='images/icon.png',
                                name='Lambda',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/lambda")),
            ExtensionResultItem(icon='images/icon.png',
                                name='Dynamo DB',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/dynamodb")),
            ExtensionResultItem(icon='images/icon.png',
                                name='Management Console',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com")),
            ExtensionResultItem(icon='images/icon.png',
                                name='Pricing calculator',
                                on_enter=OpenUrlAction("https://calculator.s3.amazonaws.com/index.html")),
        ]

        return RenderResultListAction(items)


if __name__ == '__main__':
    AWSLauncherExtension().run()
