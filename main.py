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
                                name='AWS EC2',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/ec2")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS ECS',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/ecs")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS RDS',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/RDS")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS S3',
                                on_enter=OpenUrlAction("https://s3.console.aws.amazon.com/s3")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS Elasticbeanstalk',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/elasticbeanstalk")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS ElastiCache',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/elasticache")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS CloudWatch',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/cloudwatch")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS Cloudformation',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/cloudformation")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS Route53',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/route53")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS VPC',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/vpc")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS IAM',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/iam")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS ECR',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/ecr")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS EKS',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/eks")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS Lambda',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/lambda")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS Dynamo DB',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com/dynamodb")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS Management Console',
                                on_enter=OpenUrlAction("https://console.aws.amazon.com")),
            ExtensionResultItem(icon='images/icon.png',
                                name='AWS Pricing calculator',
                                on_enter=OpenUrlAction("https://calculator.s3.amazonaws.com/index.html")),
        ]

        return RenderResultListAction(items)


if __name__ == '__main__':
    AWSLauncherExtension().run()
