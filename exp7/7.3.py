class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        count = len(self.collection) // self.items_per_page
        if len(self.collection) % self.items_per_page == 0:
            return count
        else:
            return count + 1

    def page_item_count(self, page_index):
        count = self.page_count()
        item_count = [[]] * count
        if page_index >= count or page_index < 0:
            return -1
        else:
            for i in range(count):
                item_count[i] = self.collection[i * self.items_per_page:(i + 1) * self.items_per_page]
            return len(item_count[page_index])

    def page_index(self, item_index):
        if item_index >= len(self.collection):
            return -1
        else:
            empty = []
            if self.collection == empty:
                return -1
            else:
                n, m = divmod(item_index, self.items_per_page)
                count = self.page_count()
                if n >= count or item_index < 0:
                    return -1
                else:
                    return n