from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

from data import services


class GnomeSessionExtension(Extension):
    def __init__(self):
        super(GnomeSessionExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query_parts = event.query.split(" ")

        matched_services = []
        if len(query_parts) == 1:
            matched_services = services
        else:
            for service in services:
                for keyword in service["keywords"]:
                    if query_parts[1].lower() in keyword.lower():
                        matched_services.append(service)
                        break

        items = [
            ExtensionResultItem(
                name=s["name"],
                description=s["description"],
                on_enter=OpenUrlAction(s["url"]),
                icon=s["icon"]
            )
            for s in matched_services
        ]

        return RenderResultListAction(items)


if __name__ == '__main__':
    GnomeSessionExtension().run()
