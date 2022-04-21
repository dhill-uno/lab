class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        self.__channel = self.MIN_CHANNEL
        self.__volume = self.MIN_VOLUME
        self.__status = False

    def power(self):
        if not self.__status:
            self.__status = True
        elif self.__status:
            self.__status = False

    def channel_up(self):
        if self.__status:
            self.__channel += 1
            if self.__channel > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self):
        if self.__status:
            self.__channel -= 1
            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self):
        if self.__status:
            self.__volume += 1
            if self.__volume > self.MAX_VOLUME:
                self.__volume = self.MAX_VOLUME

    def volume_down(self):
        if self.__status:
            self.__volume -= 1
            if self.__volume < self.MIN_VOLUME:
                self.__volume = self.MIN_VOLUME

    def __str__(self):
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
