class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        """
        Method to set:
        Private channel variable set to the Min. Channel
        Private volume variable set to the Min. Volume
        Private tv status variable set to tv status off
        """
        self.__channel = self.MIN_CHANNEL
        self.__volume = self.MIN_VOLUME
        self.__status = False

    def power(self):
        """
        Method that turns tv status to on or off
        """
        if not self.__status:
            self.__status = True
        elif self.__status:
            self.__status = False

    def channel_up(self):
        """
        Method that turns channel up by 1. If at max channel, goes back to min channel
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self):
        """
         Method that turns channel up by 1. If at min channel, goes back to max channel
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self):
        """
        Method that turns volume up by 1. If at max volume, goes back to min volume
        """
        if self.__status:
            self.__volume += 1
            if self.__volume > self.MAX_VOLUME:
                self.__volume = self.MAX_VOLUME

    def volume_down(self):
        """
        Method that turn volume down by 1, if at min volume, goes back to max volume
        """
        if self.__status:
            self.__volume -= 1
            if self.__volume < self.MIN_VOLUME:
                self.__volume = self.MIN_VOLUME

    def __str__(self):
        """
        Method used to return the tv status, channel info, and volume info
        """
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
