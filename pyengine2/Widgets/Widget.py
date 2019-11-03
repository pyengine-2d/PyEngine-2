from pyengine2.Utils import Vec2


class Widget:
    def __init__(self, x, y):
        """
            Create Widget

            :param x: X Pos
            :param y: Y Pos

            .. note:: You may not use this constructor. Widget isn't util
        """
        self.x = x
        self.y = y
        self.identity = None
        self.system = None
        self.showed = True
        self.old_debug_pos = None

    def event(self, evt):
        """
            Manage Event

            :param evt: Event triggered

            .. note:: You may not use this method. UISystem make it for you
        """
        pass

    def update(self):
        """
            Update Widget

            .. note:: You may not use this method. UISystem make it for you
        """
        pass

    def show(self, screen):
        """
            Show Widget to screen

            :param screen: Screen where widget must be showed
            :return: Rects must be updated

            .. note:: You may not use this method. UISystem make it for you
        """
        pass

    def show_debug(self, screen):
        """
            Show debug widget to screen

            :param screen: Screen where entity is showed
            :return: Rects must be updated

            .. note:: You may not use this method. EntitySystem make it for you
        """
        if self.showed:
            pos = Vec2(self.x, self.y)
            image = self.system.debug_font.render("ID : "+str(self.identity))
            if self.old_debug_pos != pos:
                if self.old_debug_pos is not None:
                    dirty_rect = image.get_rect(x=self.old_debug_pos.x, y=self.old_debug_pos.y - 20)
                    screen.fill(self.system.world.window.color.get_rgba(), dirty_rect)
                else:
                    dirty_rect = None
                self.old_debug_pos = pos
                image_rect = True
            else:
                dirty_rect = None
                image_rect = False

            screen.blit(image, (pos.x, pos.y - 20))

            if dirty_rect:
                yield dirty_rect
            if image_rect:
                yield image.get_rect(x=pos.x, y=pos.y-20)
