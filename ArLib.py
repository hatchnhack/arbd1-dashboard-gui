from arbd import arbd1
class ArLib:
    try:
        # CLASS VARIBLE SO THAT IT CAN BE COMMON FOR ALL INSTANCES , WILL BE USED IN OTHER CLASSES
        board = arbd1()
    except:
        print(' BOARD ERROR')