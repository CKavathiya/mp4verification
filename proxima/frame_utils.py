class FrameUtils:
    """
    FrameUtils identifies white lines. But, the white lines may not
    be encoded perfectly (i.e. not 255 exactly), esp. with lower bitrates
    the color values may deviate more. So, allowing a tolerance of -10
    (i.e. 245 to 255 are allowed) while detecting white lines.
    """
    __tolerance = 10

    @staticmethod
    def hasHorizontalLine(frame, xPos_range, yPos):
        for i in xPos_range:
            if 255 - frame[yPos,i,0] > FrameUtils.__tolerance and \
               255 - frame[yPos,i,1] > FrameUtils.__tolerance and \
               255 - frame[yPos,i,2] > FrameUtils.__tolerance:
                break

        return i == xPos_range[-1]


    @staticmethod
    def hasVerticalLine(frame, xPos, yPos_range):
        for i in yPos_range:
            if 255 - frame[i,xPos,0] > FrameUtils.__tolerance and \
               255 - frame[i,xPos,1] > FrameUtils.__tolerance and \
               255 - frame[i,xPos,2] > FrameUtils.__tolerance:
                break

        return i == yPos_range[-1]
