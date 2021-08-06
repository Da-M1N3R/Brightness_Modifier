import screen_brightness_control as sbc

def decrease_brightness(current_brightness):
    # Set brightness
    new_brightness = sbc.set_brightness(current_brightness - 10, display=0)
    print("Current brightness: " + str(sbc.get_brightness()))

# Get brightness of primary display
primary_brightness = sbc.get_brightness(display=0)
print("Initial brightness: " + str(primary_brightness))
decrease_brightness(primary_brightness)

'''
# Fade brightness
sbc.fade_brightness(70, start = 0)
print(sbc.get_brightness())
'''
