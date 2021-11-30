from cotalog.models import Videocard


class ScraperPipeline:
    def process_item(self, item, spider):
        item.save()

        return item
