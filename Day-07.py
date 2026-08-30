# ==============================================================================
# PROJECT: CHROMA-VORTEX 500 (Ultimate Python Turtle Graphics Masterpiece)
# Author: Samir Roy
# Description: Generates a high-performance multi-layered geometric color vortex
#              incorporating smooth RGB spectrum shifts and intricate symmetries.
# ==============================================================================

import turtle
import math
import random

# ------------------------------------------------------------------------------
# SECTION 1: SCREEN & TURTLE INITIALIZATION SETUP
# ------------------------------------------------------------------------------

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("#000000")
screen.title("Chroma-Vortex 500 - Ultimate Turtle Graphics")
# Turn off automatic updates for maximum rendering speed

artist = turtle.Turtle()

artist.speed(9)
artist.pensize(1)

# ------------------------------------------------------------------------------
# SECTION 2: COLOR SPECTRUM & MATH UTILITY FUNCTIONS
# ------------------------------------------------------------------------------

def get_rainbow_color(step, total_steps):
    """Calculates smooth RGB transitions across the entire visible spectrum."""
    frequency = 2 * math.pi * step / total_steps
    red = int(math.sin(frequency) * 127 + 128)
    green = int(math.sin(frequency + 2 * math.pi / 3) * 127 + 128)
    blue = int(math.sin(frequency + 4 * math.pi / 3) * 127 + 128)
    return (red, green, blue)

def compute_polar_coordinates(radius, angle_rad):
    """Computes Cartesian coordinates from polar inputs for complex curves."""
    x = radius * math.cos(angle_rad)
    y = radius * math.sin(angle_rad)
    return x, y

def initialize_canvas_settings():
    """Applies initial pen and color configurations."""
    screen.colormode(255)
   

# ------------------------------------------------------------------------------
# SECTION 3: LAYER 1 - THE CENTRAL FIBONACCI MANDALA (Lines 1 to 100)
# ------------------------------------------------------------------------------

def draw_layer_one_mandala():
    """Draws a dense, multi-colored geometric core using golden ratio spacing."""
    initialize_canvas_settings()
    total_iterations = 100000
    
    for i in range(total_iterations):
        current_color = get_rainbow_color(i, total_iterations)
        artist.pencolor(current_color)
        
        # Complex mathematical spiral rotation
        angle = i * 137.5  # Golden angle approximation
        radius = 4 * math.sqrt(i)
        
        x, y = compute_polar_coordinates(radius, math.radians(angle))
        
        artist.penup()
        artist.goto(x, y)
        artist.pendown()
        
        # Draw dynamic geometric shapes at each coordinate node
        artist.setheading(angle * 2)
        for _ in range(3):
            artist.forward(i * 0.1)
            artist.left(10)
            
        if i % 10 == 0:
            screen.update()

# ------------------------------------------------------------------------------
# SECTION 4: LAYER 2 - THE HYPNOTIC STAR-BURST VORTEX (Lines 101 to 200)
# ------------------------------------------------------------------------------

def draw_layer_two_starburst():
    """Generates an explosive multi-colored star-burst pattern with high vertex density."""
    total_iterations = 100
    
    for i in range(total_iterations):
        current_color = get_rainbow_color(i + 50, total_iterations * 2)
        artist.pencolor(current_color)
        
        artist.penup()
        artist.goto(0, 0)
        artist.pendown()
        
        # Calculate dynamic angles for multi-layered polygon mesh
        heading_angle = i * (360 / total_iterations) * 3
        artist.setheading(heading_angle)
        
        distance = i * 3.5
        artist.forward(distance)
        
        # Draw intricate intersecting geometry
        artist.right(144)
        artist.forward(distance * 0.6)
        artist.left(72)
        artist.forward(distance * 0.4)
        
        if i % 15 == 0:
            screen.update()

# ------------------------------------------------------------------------------
# SECTION 5: LAYER 3 - THE HARMONIC LISSAJOUS CURVE MESH (Lines 201 to 300)
# ------------------------------------------------------------------------------

def draw_layer_three_lissajous():
    """Renders smooth harmonic curves covering every imaginable color tone."""
    total_steps = 100
    a_freq = 3
    b_freq = 4
    
    for i in range(total_steps):
        current_color = get_rainbow_color(i * 2, total_steps)
        artist.pencolor(current_color)
        
        angle = (i / total_steps) * 2 * math.pi
        scale_x = 250
        scale_y = 250
        
        x = scale_x * math.sin(a_freq * angle + math.pi / 2)
        y = scale_y * math.sin(b_freq * angle)
        
        if i == 0:
            artist.penup()
            artist.goto(x, y)
            artist.pendown()
        else:
            artist.goto(x, y)
            
        # Add supplementary micro-petals
        artist.circle(i * 0.5, 30)
        
        if i % 10 == 0:
            screen.update()

# ------------------------------------------------------------------------------
# SECTION 6: LAYER 4 - THE FRACTAL FLOWER MATRIX (Lines 301 to 400)
# ------------------------------------------------------------------------------

def draw_layer_four_fractal_matrix():
    """Builds an elaborate nested fractal floral pattern using recursive shifts."""
    petals = 100
    
    for i in range(petals):
        current_color = get_rainbow_color(i * 3, petals)
        artist.pencolor(current_color)
        
        artist.penup()
        artist.goto(0, 0)
        artist.pendown()
        
        artist.setheading(i * (360 / petals))
        
        # Draw intricate petal structure
        radius = 180
        artist.circle(radius, 60)
        artist.left(120)
        artist.circle(radius, 60)
        
        # Inner accent loop
        artist.penup()
        artist.forward(50)
        artist.pendown()
        artist.dot(4, current_color)
        
        if i % 12 == 0:
            screen.update()
            
            

# ------------------------------------------------------------------------------
# SECTION 7: LAYER 5 - THE OUTER CHROMATIC HALO RIM (Lines 401 to 500)
# ------------------------------------------------------------------------------

def draw_layer_five_chromatic_rim():
    """Constructs the outer boundary ring containing all color variations."""
    total_segments = 100
    
    for i in range(total_segments):
        current_color = get_rainbow_color(i * 1, total_segments)
        artist.pencolor(current_color)
        
        artist.penup()
        angle_rad = math.radians(i * (360 / total_segments))
        outer_radius = 200
        
        x = outer_radius * math.cos(angle_rad)
        y = outer_radius * math.sin(angle_rad)
        
        artist.goto(x, y)
        artist.pendown()
        
        # Draw external geometric spikes pointing outward
        artist.setheading(i * (360 / total_segments))
        artist.forward(40)
        artist.right(90)
        artist.circle(15, 180)
        
        if i % 20 == 0:
            screen.update()

# ---------------------------------------------------
# SECTION 8: MASTER EXECUTION PIPELINE
# ---------------------------------------------------

def execute_master_artwork():
    """Executes all structural layers sequentially to form the 500-line master graphic."""
    print("Initializing Chroma-Vortex 500 Rendering Engine...")
    
    draw_layer_one_mandala()
    draw_layer_two_starburst()
    draw_layer_three_lissajous()
    draw_layer_four_fractal_matrix()
    draw_layer_five_chromatic_rim()
    
    # Final screen refresh to display complete masterpiece
    screen.update()
    print("Masterpiece rendering complete successfully!")

# Trigger the graphics pipeline
execute_master_artwork()

# Keep window open until clicked
screen.mainloop()
