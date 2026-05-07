bl_info = {
    "name": "素材・成果物カタログ",
    "author": "Sunmax0731",
    "version": (0, 1, 0),
    "blender": (4, 0, 0),
    "category": "System",
}

import bpy

class SUNMAX_PT_alpha_panel(bpy.types.Panel):
    bl_label = "素材・成果物カタログ"
    bl_idname = "SUNMAX_PT_blender_asset_artifact_catalog"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Sunmax"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Closed alpha validation panel")
        layout.label(text="Blender素材カタログ")

classes = (SUNMAX_PT_alpha_panel,)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

