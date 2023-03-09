from proxima.frame_utils import FrameUtils
from proxima.pane import Pane
from enum import Enum


class Frame:
    class LayoutType(Enum):
        ONE_X_TWO = 1
        TWO_X_TWO = 2
        THREE_X_THREE = 3
        VBSS = 4


    def __init__(self, frame):
        self.timeStamp = 0
        self.frame = frame
        self.panes = []
        self._findLayoutType()


    def dimensions(self):
        """
        Returns height, width, channel
        """
        return self.frame.shape


    def __getitem__(self, tup):
        yPos, xPos, colorChannel = tup
        return self.frame[yPos][xPos][colorChannel]


    def onPane(self, id: int) -> Pane:
        if not self.panes:
            self._collectPanes()

        assert(id >=0 and id <= len(self.panes) - 1)
        return self.panes[id]


    def has3x3Layout(self, n = 9):
        assert self.layout == Frame.LayoutType.THREE_X_THREE and self.paneCount == n
        return self


    def has2x2Layout(self, n = 4):
        assert self.layout == Frame.LayoutType.TWO_X_TWO and self.paneCount == n
        return self


    def has1x2Layout(self, n = 2):
        assert self.layout == Frame.LayoutType.ONE_X_TWO and self.paneCount == n
        return self


    def hasVBSSLayout(self):
        assert self.layout == Frame.LayoutType.VBSS
        return self


    def _findLayoutType(self):
        h, w, _ = self.dimensions()
        upperHeight = ((int)(6 / 7.0 * h))

        if FrameUtils.hasVerticalLine(self, w // 3, range(0, upperHeight)) and FrameUtils.hasVerticalLine(self, 2 * w // 3, range(0, upperHeight)):
            self.layout = Frame.LayoutType.THREE_X_THREE
            if FrameUtils.hasHorizontalLine(self, range(0, w), upperHeight // 3):
                self.paneCount = 9
            elif FrameUtils.hasHorizontalLine(self, range(w // 3, w), upperHeight // 3):
                self.paneCount = 8
            elif FrameUtils.hasHorizontalLine(self, range(2 * w // 3, w), upperHeight // 3):
                self.paneCount = 7
            elif FrameUtils.hasHorizontalLine(self, range(0, w), upperHeight // 2):
                self.paneCount = 6
            elif FrameUtils.hasHorizontalLine(self, range(w // 3, w), upperHeight // 2):
                self.paneCount = 5
        elif FrameUtils.hasVerticalLine(self, w // 2, range(0, h)):
            if FrameUtils.hasHorizontalLine(self, range(0, w), upperHeight // 2):
                self.layout = Frame.LayoutType.TWO_X_TWO
                self.paneCount = 4
            elif FrameUtils.hasHorizontalLine(self, range(w // 2, w), upperHeight // 2):
                self.layout = Frame.LayoutType.TWO_X_TWO
                self.paneCount = 3
            else:
                self.layout = Frame.LayoutType.ONE_X_TWO
                self.paneCount = 2
        elif FrameUtils.hasHorizontalLine(self, range(0, w), 0) and FrameUtils.hasVerticalLine(self, 0, range(0, h)) and FrameUtils.hasVerticalLine(self, 1, range(0, h)):
            self.layout = Frame.LayoutType.ONE_X_TWO
            self.paneCount = 1
        else:
            self.layout = Frame.LayoutType.VBSS


    def _collectPanes(self):
        if self.layout == Frame.LayoutType.THREE_X_THREE:
            self._store3x3LayoutPanes()
        elif self.layout == Frame.LayoutType.TWO_X_TWO:
            self._store2x2LayoutPanes()
        elif self.layout == Frame.LayoutType.ONE_X_TWO:
            self._store1x2LayoutPanes()
        else:
            self._storeVBSSLayoutPanes()


    def _store3x3LayoutPanes(self):
        self.__storeMainGridPanes(3, self.paneCount)
        self.__storeBottomStripPanes()


    def _store2x2LayoutPanes(self):
        self.__storeMainGridPanes(2, self.paneCount)
        self.__storeBottomStripPanes()


    def _store1x2LayoutPanes(self):
        h, w, _ = self.frame.shape
        self.panes.append(Pane(self.frame[0:h, 0:w//2]))
        self.panes.append(Pane(self.frame[0:h, w//2:w]))


    def _storeVBSSLayoutPanes(self):
        h, w, _ = self.frame.shape
        upperHeight = (int)(6 / 7.0 * h)

        self.panes.append(Pane(self.frame[0:upperHeight, 0:w]))
        self.__storeBottomStripPanes()


    def __storeMainGridPanes(self, size, numPanes):
        h, w, _ = self.frame.shape
        upperHeight = (int)(6 / 7.0 * h)

        for col in range(size):
            numCells = numPanes // (size - col)
            paneWidth = w // size
            paneHeight = upperHeight // numCells
            for row in range(numCells):
                yPos = row * paneHeight
                xPos = col * paneWidth
                numPanes = numPanes - 1
                self.panes.append(Pane(self.frame[yPos:yPos + paneHeight,
                                            xPos:xPos + paneWidth]))


    def __storeBottomStripPanes(self):
        h, w, _ = self.frame.shape
        upperHeight = (int)(6 / 7.0 * h)
        lowerHeight = h - upperHeight

        xPos = -1 * (w // 6)
        for i in range(6):
            xPos += w // 6
            self.panes.append(Pane(self.frame[upperHeight:upperHeight + lowerHeight,
                                         xPos: xPos + w//6]))
