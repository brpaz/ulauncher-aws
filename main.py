from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, PreferencesEvent, PreferencesUpdateEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

from data import services

DEFAULT_MAX_RESULTS = 7


class GnomeSessionExtension(Extension):
    def __init__(self):
        super(GnomeSessionExtension, self).__init__()
        self.max_results = DEFAULT_MAX_RESULTS
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query_parts = event.query.split(" ", maxsplit=1)
        query_string = "" if len(query_parts) == 1 else query_parts[1].lower()

        # The priority logic below sorts the matches by best, good, and other matches.
        # If the first keyword in a service starts with the query string, the service is considered a "best" match.
        # The reasoning behind this is that the first keyword in a service typically is the colloquial name of the
        # service. For instance, the first keyword of "AWS DynamoDB" would be "dynamodb". Good matches only have a
        # keyword that starts with the query string (but not the first keyword). Other matches have a keyword that
        # contains (but does not start with) the query string.
        #
        # For example, if the query string was "d", the following matches would be returned:
        # best: "AWS DynamoDB" (the first keyword, "dynamodb", starts with "d")
        # good: "AWS Route 53" (the keyword (not first), "dns", starts with "d")
        # other: "AWS Billing Dashboard", "AWS CloudFormation", "AWS CloudTrail", "AWS CloudWatch", "AWS Cloudfront",
        #      "AWS Lambda", "AWS RDS", "AWS Support Console" (each service has a keyword that contains, but doesn't
        #      start with, the string: "d")

        best_matches = []
        good_matches = []
        other_matches = []

        if not query_string:
            other_matches.extend(services)
        else:
            for service in services:
                if len(service["keywords"]) > 0 and service["keywords"][0].lower().startswith(query_string):
                    best_matches.append(service)
                    continue

                for keyword in service["keywords"]:
                    if keyword.lower().startswith(query_string):
                        good_matches.append(service)
                        break
                    elif query_string in keyword.lower():
                        other_matches.append(service)
                        break

        # Sort matches by the service's colloquial name (first keyword)
        best_matches.sort(key=lambda s: s["keywords"][0])
        good_matches.sort(key=lambda s: s["keywords"][0])
        other_matches.sort(key=lambda s: s["keywords"][0])

        items = [
            ExtensionResultItem(
                name=s["name"],
                description=s["description"],
                on_enter=OpenUrlAction(s["url"]),
                icon=s["icon"]
            )
            for s in (best_matches + good_matches + other_matches)
        ]

        return RenderResultListAction(items)


if __name__ == "__main__":
    GnomeSessionExtension().run()
