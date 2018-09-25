import maya.cmds as cmds

def kasisei():

    def visoff():
        cmds.select(cmds.ls(selection=True, dagObjects=True, type='shape'))
        secobj = cmds.ls(sl=True)

        for obj in secobj:
            cmds.setAttr( obj + ".primaryVisibility", 0)

    def vison():
        cmds.select(cmds.ls(selection=True, dagObjects=True, type='shape'))
        secobj = cmds.ls(sl=True)

        for obj in secobj:
            print obj
            cmds.setAttr( obj + ".primaryVisibility", 1)


    cmds.window(title='primaryVisibility')
    cmds.columnLayout()
    cmds.button(label="primaryVisibility ON", command = 'vison()')
    cmds.button(label="primaryVisibility OFF", command = 'visoff()')
    cmds.showWindow()

kasisei()
