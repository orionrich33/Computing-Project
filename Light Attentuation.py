import pyvista as pv

plotter = pv.Plotter(lighting=None, window_size=(800, 800))

# create a top down light
light = pv.Light(position=(0, 0, 3), show_actor=True, positional=True,
                 cone_angle=1, exponent=20, intensity=1)
plotter.add_light(light)
light2 = pv.Light(position=(0.5, 0.5, 3), show_actor=True, positional=True,
                 cone_angle=1, exponent=20, intensity=1)
plotter.add_light(light2)

# add a sphere to the plotter
skin = pv.Cube(x_length=1, y_length=1, z_length =0.2, center=(0,0,1))
plotter.add_mesh(skin, ambient=0.5, diffuse=0.5, specular=0.8,
                 specular_power=30, opacity=0.2, smooth_shading=True,
                 color='green')
muscle = pv.Cube(x_length=1, y_length=1, z_length =0.2, center=(0,0,1.2))
plotter.add_mesh(muscle, ambient=0.5, diffuse=0.5, specular=0.8,
                 specular_power=30, opacity=0.2, smooth_shading=True,
                 color='red')
fat = pv.Cube(x_length=1, y_length=1, z_length =0.2, center=(0,0,1.4))
plotter.add_mesh(fat, ambient=0.5, diffuse=0.5, specular=0.8,
                 specular_power=30, opacity=0.2, smooth_shading=True,
                 color='orange')

# add the grid
grid = pv.Plane(i_size=4, j_size=4)
plotter.add_mesh(grid, ambient=0, diffuse=0.5, specular=0.8, color='white')

# set up and show the plotter
plotter.enable_shadows()
plotter.set_background('darkgrey')
plotter.show()