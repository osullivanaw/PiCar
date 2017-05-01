MAG_ADDRESS	=	0x1E
ACC_ADDRESS	=	0x6B
GYR_ADDRESS     =       0x6B

#LSM9DS1 Accelerometer and Gyro Registers
ACT_THS = 0x04

WHO_AM_I_G	=	0x0F
CTRL_REG1_G	=	0x10
CTRL_REG2_G	=	0x11
CTRL_REG3_G	=	0x12
CTRL_REG4       = 0B00011110
CTRL_REG5_XL    = 0B00011111
CTRL_REG6_XL         = 0B00100000
CTRL_REG7_XL         = 0B00100001
CTRL_REG8            = 0B00100010
CTRL_REG9            = 0B00100011
CTRL_REG10           = 0B00100100
REFERENCE_G	=	0x15
STATUS_REG_G	=	0x27
OUT_X_L_G	=	0x18
OUT_X_H_G	=	0x19
OUT_Y_L_G	=	0x1A
OUT_Y_H_G	=	0x1B
OUT_Z_L_G	=	0x1C
OUT_Z_H_G	=	0x1D
FIFO_CTRL_REG_G	=	0x2E
FIFO_SRC_REG_G	=	0x2F
INT1_CFG_G	=	0x30
INT1_SRC_G	=	0x31
INT1_THS_XH_G	=	0x32
INT1_THS_XL_G	=	0x33
INT1_THS_YH_G	=	0x34
INT1_THS_YL_G	=	0x35
INT1_THS_ZH_G	=	0x36
INT1_THS_ZL_G	=	0x37
INT1_DURATION_G	=	0x38


CTRL_REG4       = 0B00011110

#LSM9D1 Accel and Magneto Registers
OUT_TEMP_L	=	0x15
OUT_TEMP_H	=	0x16
STATUS_REG_M	=	0x07
OUT_X_L_M	=	0x28
OUT_X_H_M	=	0x29
OUT_Y_L_M	=	0x2A
OUT_Y_H_M	=	0x2B
OUT_Z_L_M	=	0x2C
OUT_Z_H_M	=	0x2D
WHO_AM_I_XM	=	0x0F
INT_CTRL_REG_M	=	0x12
INT_SRC_REG_M	=	0x13
INT_THS_L_M	=	0x14
INT_THS_H_M	=	0x15
OFFSET_X_L_M	=	0x16
OFFSET_X_H_M	=	0x17
OFFSET_Y_L_M	=	0x18
OFFSET_Y_H_M	=	0x19
OFFSET_Z_L_M	=	0x1A
OFFSET_Z_H_M	=	0x1B
REFERENCE_X	=	0x1C
REFERENCE_Y	=	0x1D
REFERENCE_Z	=	0x1E
CTRL_REG0_M	=	0x1F
CTRL_REG1_M	=	0x20
CTRL_REG2_M	=	0x21
CTRL_REG3_M	=	0x22
CTRL_REG4_M	=	0x23
CTRL_REG5_M	=	0x24
CTRL_REG6_M	=	0x25
CTRL_REG7_M	=	0x26
STATUS_REG_A	=	0x27
OUT_X_L_XL	=	0x28
OUT_X_H_XL	=	0x29
OUT_Y_L_XL	=	0x2A
OUT_Y_H_XL	=	0x2B
OUT_Z_L_XL	=	0x2C
OUT_Z_H_XL	=	0x2D
FIFO_CTRL_REG	=	0x2E
FIFO_SRC_REG	=	0x2F
INT_GEN_1_REG	=	0x30
INT_GEN_1_SRC	=	0x31
INT_GEN_1_THS	=	0x32
INT_GEN_1_DURATION	=	0x33
INT_GEN_2_REG	=	0x34
INT_GEN_2_SRC	=	0x35
INT_GEN_2_THS	=	0x36
INT_GEN_2_DURATION	=	0x37
CLICK_CFG	=	0x38
CLICK_SRC	=	0x39
CLICK_THS	=	0x3A
TIME_LIMIT	=	0x3B
TIME_LATENCY	=	0x3C
TIME_WINDOW	=	0x3D