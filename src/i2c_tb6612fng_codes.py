class TB6612FNGCodes:
    """
    Operational codes used to send commands to the driver module via I2C interface.
    """
    def __init__(self):
        pass

    # module address
    GMD_I2C_ADDRESS = 0x14

    # commands for modules
    GMD_CMD_BRAKE = 0x00
    GMD_CMD_STOP = 0x01
    GMD_CMD_CW = 0x02
    GMD_CMD_CCW = 0x03
    GMD_CMD_STANDBY = 0x04
    GMD_CMD_NOT_STANDBY = 0x05
    GMD_CMD_STEPPER_RUN = 0x06
    GMD_CMD_STEPPER_STOP = 0x07
    GMD_CMD_STEPPER_KEEP_RUN = 0x08
    GMD_CMD_SET_ADDR = 0x11
