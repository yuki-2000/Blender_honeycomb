# -*- coding: utf-8 -*-

#blender ver3.1


import bpy     



for item in bpy.data.meshes:
    bpy.data.meshes.remove(item)
for item in bpy.data.materials:
    bpy.data.materials.remove(item)




mesh = bpy.data.meshes.new(name=f"hexiagon1")
bpy.ops.mesh.primitive_cylinder_add(vertices=6, radius=5, depth=4, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.ops.object.modifier_add(type='ARRAY')
bpy.context.object.modifiers["配列"].count = 10
bpy.context.object.modifiers["配列"].relative_offset_displace = [0,1.5,0]
bpy.context.object.modifiers["配列"].use_constant_offset = True
bpy.context.object.modifiers["配列"].constant_offset_displace = [0,1.7,0]
bpy.ops.object.modifier_add(type='ARRAY')
bpy.context.object.modifiers["配列.001"].count = 15
bpy.context.object.modifiers["配列.001"].relative_offset_displace = [1,0,0]
bpy.context.object.modifiers["配列.001"].use_constant_offset = True
bpy.context.object.modifiers["配列.001"].constant_offset_displace = [1,0,0]
bpy.ops.object.modifier_add(type='ARRAY')
bpy.context.object.modifiers["配列.002"].count = 2
bpy.context.object.modifiers["配列.002"].use_relative_offset = False
bpy.context.object.modifiers["配列.002"].use_constant_offset = True
bpy.context.object.modifiers["配列.002"].constant_offset_displace = [5,8.3,0]




#size
panel_location =(14.5, 25, 0)
panel_resize = (29, 50, 0.5)
foam_resize= (29, 50, 4)



#ハニカム
#マテリアルの設定
material = bpy.data.materials.new('Red')
#ノードを使えるようにする
material.use_nodes = True

bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=panel_location, scale=(1, 1, 1))
bpy.ops.transform.resize(value=(29, 50, 4), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)

p_BSDF = material.node_tree.nodes["Principled BSDF"]
p_BSDF.inputs[0].default_value = (1, 0.659, 0, 1)#RGBa
p_BSDF.inputs[9].default_value = 1 #roughness
bpy.context.object.data.materials.append(material)

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["ブーリアン"].operation = 'DIFFERENCE'
bpy.context.object.modifiers["ブーリアン"].object = bpy.data.objects["円柱"]
bpy.ops.object.modifier_apply(modifier="ブーリアン")

bpy.ops.transform.translate(value=(0, 0, 10), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)






#フォーム
#マテリアルの設定
material = bpy.data.materials.new('Red')
#ノードを使えるようにする
material.use_nodes = True

bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=panel_location, scale=(1, 1, 1))
bpy.ops.transform.resize(value=foam_resize, orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)


p_BSDF = material.node_tree.nodes["Principled BSDF"]
p_BSDF.inputs[0].default_value = (1, 1, 1, 1)
bpy.context.object.data.materials.append(material)

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["ブーリアン"].operation = 'INTERSECT'
bpy.context.object.modifiers["ブーリアン"].object = bpy.data.objects["円柱"]
bpy.ops.object.modifier_apply(modifier="ブーリアン")

bpy.ops.transform.translate(value=(0, 0, 10), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)





#上面
#マテリアルの設定
material = bpy.data.materials.new('Red')
#ノードを使えるようにする
material.use_nodes = True

bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=panel_location, scale=(1, 1, 1))
bpy.ops.transform.resize(value=panel_resize, orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
bpy.ops.transform.translate(value=(0, 0, 20), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)

p_BSDF = material.node_tree.nodes["Principled BSDF"]
p_BSDF.inputs[0].default_value = (0.1, 0.1, 0.1, 1)
bpy.context.object.data.materials.append(material)




#下面
#マテリアルの設定
material = bpy.data.materials.new('Red')
#ノードを使えるようにする
material.use_nodes = True

bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=panel_location, scale=(1, 1, 1))
bpy.ops.transform.resize(value=panel_resize, orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)

p_BSDF = material.node_tree.nodes["Principled BSDF"]
p_BSDF.inputs[0].default_value = (0.1, 0.1, 0.1, 1)
bpy.context.object.data.materials.append(material)




bpy.data.objects.remove(bpy.data.objects["円柱"])




#エッジ
bpy.context.scene.render.use_freestyle = True
bpy.context.scene.render.line_thickness = 1

#環境光で全体を明るく
#環境色を(R, G, B, A)で指定、今回は白
bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (1, 1, 1, 1)
#強さ
bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[1].default_value = 5


#カメラ



bpy.context.object.data.name = "Camera"
bpy.ops.transform.translate(value=(0, 0, 0.881679), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)


#奥行
camera = bpy.data.objects['Camera']
camera.data.clip_end = 999

#解像度
bpy.context.scene.render.resolution_percentage = 400

#背景透過
bpy.context.scene.render.film_transparent = True

