import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load sound files
Kick = pygame.mixer.Sound("Kick.wav")
Snare = pygame.mixer.Sound("Snare.wav")
Ride1 = pygame.mixer.Sound("Ride1.wav")
Ride1 = pygame.mixer.Sound("Ride2.wav")
HiHat = pygame.mixer.Sound("HiHat.wav")
Tom = pygame.mixer.Sound("Tom.wav")

# Define the pattern as arrays for each instrument
kick_pattern = [0, 0, 0, 0, 0]
Snare_pattern = [0, 0, 0, 0, 0]
Ride1_pattern = [0, 0, 0, 0, 0]
Ride2_pattern = [0, 0, 0, 0, 0]
HiHat_pattern = [1, 0, 0, 0, 0]
Tom_pattern = [0, 0, 0, 0, 0]

# Define the tempo (in BPM)
tempo = 190

# Calculate the time for each step (in milliseconds)
step_time = 60000 / tempo

# Play the pattern
while True:
    for i in range(len(kick_pattern)):
        if kick_pattern[i] == 1:
            Kick.play()
        if Snare_pattern[i] == 1:
            Snare.play()
        if Ride1_pattern[i] == 1:
            Snare.play()
        if Ride2_pattern[i] == 1:
            Snare.play()
        if HiHat_pattern[i] == 1:
            HiHat.play()
        if Tom_pattern[i] == 1:
            Tom.play()
        pygame.time.wait(int(step_time))

# Wait for the pattern to finish playing
pygame.time.wait(int(step_time * len(kick_pattern)))