class SFM:

    def move_one_item(self, input, output):
        return (input - 1, output + 1)

    def move_all_items(self, input, output):
        return (0, output + input)

    def move_some_items(self, input, output, quantity):
        return (input - quantity, output + quantity)

    # In moveX
    def xMoveMove(self):
        if (self.xR > 0):
            print("Going backward a block!")
            ( self.move, self.stoneStorage ) = self.move_one_item(self.move, self.stoneStorage)
        else:
            print("Going forward a block!")
            ( self.move, self.stoneStorage ) = self.move_one_item(self.move, self.stoneStorage)

    # In moveForward
    def moveX(self):
        if (self.move > 1):
            self.xMoveMove()
        else:
            if (self.xS1 > 0):
                if (self.xR > 0):
                    print("Going backward a space!")
                    ( self.xS1, self.xS2 ) = self.move_one_item(self.xS1, self.xS2)
                else:
                    print("Going forward a space!")
                    ( self.xS1, self.xS2 ) = self.move_one_item(self.xS1, self.xS2)
            else:
                ( self.xS2, self.xS1 ) = self.move_all_items(self.xS2, self.xS1)
                self.xMoveMove()

    #own group
    def moveForward(self):
        if (self.x1 > 0):
            if (self.move > 0):
                self.moveX()
            else:
                ( self.x1, self.x2 ) = self.move_one_item(self.x1, self.x2)
                if (self.x1 > 0):
                    ( self.stoneStorage, self.move ) = self.move_some_items(self.stoneStorage, self.move, 4)
                    self.moveX()
        else:
            self.onDrawer = 0

    # In moveZ
    def zMoveMove(self):
        if (self.zR > 0):
            print("Going down a block!")
            ( self.move, self.stoneStorage ) = self.move_one_item(self.move, self.stoneStorage)
        else:
            print("Going up a block!")
            ( self.move, self.stoneStorage ) = self.move_one_item(self.move, self.stoneStorage)

    # In goUp
    def moveZ(self):
        if (self.move > 1):
            self.zMoveMove()
        else:
            if (self.zS1 > 0):
                if (self.zR > 0):
                    print("Going down a space!")
                    ( self.zS1, self.zS2 ) = self.move_one_item(self.zS1, self.zS2)
                else:
                    print("Going up a space!")
                    ( self.zS1, self.zS2 ) = self.move_one_item(self.zS1, self.zS2)
            else:
                ( self.zS2, self.zS1 ) = self.move_all_items(self.zS2, self.zS1)
                self.zMoveMove()

    # First Group
    def goUp(self):
        if (self.z1 > 0):
            if (self.move > 0):
                self.moveZ()
            else:
                ( self.z1, self.z2 ) = self.move_one_item(self.z1, self.z2)
                if (self.z1 > 0):
                    ( self.stoneStorage, self.move ) = self.move_some_items(self.stoneStorage, self.move, 4)
                    self.moveZ()
        else:
            self.moveForward()

    def __init__(self, xSpace, ySpace, zSpace, x, y, z):

        # Initialize existing drawers
        self.stoneStorage = 128
        self.move = 0
        self.spaceMove = 0
        self.onDrawer = 0
        self.teleporter = 0
        self.t2Move = 0

        # primary and 2ndary storage for all axis
        self.z1 = z
        self.z2 = 0
        self.y1 = y
        self.y2 = 0
        self.x1 = x
        self.x2 = 0

        # Handling spacing in 3d
        self.xS1 = xSpace
        self.yS1 = ySpace
        self.zS1 = zSpace
        self.xS2 = 0
        self.yS2 = 0
        self.zS2 = 0

        # Switching between directions in 3d
        self.xR = 0
        self.yR = 0
        self.zR = 0

        # Things I set
        ( self.stoneStorage, self.onDrawer) = self.move_one_item(self.stoneStorage, self.onDrawer)
        ( self.stoneStorage, self.move ) = self.move_some_items(self.stoneStorage, self.move, 4)

        while (self.onDrawer > 0):
            self.goUp()