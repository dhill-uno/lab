class Television:
    """
    Television objects
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Method to set:
        Private channel variable set to the Min. Channel
        Private volume variable set to the Min. Volume
        Private tv status variable set to tv status off
        """
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__status: bool = False

    def power(self) -> None:
        """
        Method that turns tv status to on or off
        """
        if not self.__status:
            self.__status = True
        elif self.__status:
            self.__status = False

    def channel_up(self) -> None:
        """
        Method that turns channel up by 1. If at max channel, goes back to min channel
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
         Method that turns channel up by 1. If at min channel, goes back to max channel
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method that turns volume up by 1. If at max volume, goes back to min volume
        """
        if self.__status:
            self.__volume += 1
            if self.__volume > Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        """
        Method that turns volume down by 1, if at min volume, goes back to max volume
        """
        if self.__status:
            self.__volume -= 1
            if self.__volume < Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        """
        Method used to return the tv status, channel info, and volume info
        :return: TV status: Is on = False, Channel = 0, Volume = 0
        """
        return f'TV status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
