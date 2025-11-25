cube_urdf = """
<robot name="box_shape">
  <link name="base_link">
    <visual>
      <geometry>
        <box size="0.2 0.2 0.2"/>
      </geometry>
      <material name="blue">
        <color rgba="0 0 1 1"/>
      </material>
    </visual>
  </link>
</robot>
"""

save_urdf("cube.urdf", cube_urdf)

sphere_urdf = """
<robot name="round_shape">
  <link name="base_link">
    <visual>
      <geometry>
        <sphere radius="0.1"/>
      </geometry>
      <material name="red">
        <color rgba="1 0 0 1"/>
      </material>
    </visual>
  </link>
</robot>
"""

save_urdf("sphere.urdf", sphere_urdf)

cylinder_urdf = """
<robot name="tube_shape">
  <link name="base_link">
    <visual>
      <geometry>
        <cylinder radius="0.1" length="0.3"/>
      </geometry>
      <material name="green">
        <color rgba="0 1 0 1"/>
      </material>
    </visual>
  </link>
</robot>
"""

save_urdf("cylinder.urdf", cylinder_urdf)

pyramid_urdf = """
<robot name="tri_prism">
  <link name="base_link">
    <visual>
      <geometry>
        <box size="0.2 0.2 0.1"/>
      </geometry>
      <material name="yellow">
        <color rgba="1 1 0 1"/>
      </material>
    </visual>
  </link>
</robot>
"""

save_urdf("pyramid.urdf", pyramid_urdf)