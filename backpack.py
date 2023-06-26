class BackPack:
    """
    BackPack Class


    ToDo: [X] Instantiate backpack
    ToDo: [X] Add Item
    ToDo: [X] Remove Item
    ToDo: [X] List Items
    ToDo: [X] Count items
    ToDo: [X] in backpack (Search for Item - Student to do)
    ToDo: [X] Sort Item

    """

    def __init__(self, item):
        self._backpack = []
        if not isinstance(item, list):
            items = []
        for item in item:
            self._backpack.append(item)

    def remove_item(self, item_name):
        if self.in_backpack(item_name) and self.in_backpack(item_name) != 0:
            self._backpack.remove(self._backpack[self.in_backpack(item_name)])
            return self._backpack

    def sort(self):
        self._backpack.sort()
        return self._backpack

    def return_items(self):
        return self._backpack

    def count(self):
        return len(self._backpack)


    def add(self, item):
        if item is not None:
            self._backpack.append(item)
            self.sort()
            return self._backpack

    def in_backpack(self, item):
        """
        returns False if not found
        returns position if found
        :param item:
        :return: False | integer
        """
        left = 0
        right = len(self._backpack) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_item = self._backpack[mid]

            if mid_item.name == item:
                return mid
            elif mid_item.name < item:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def __str__(self):
        return f"{self.return_items()}"
