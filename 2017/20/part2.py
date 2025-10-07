input = open("input.txt")
input = input.readlines()

particles = []
for i in input:
    particle = []
    for j in i.split(", "):
        k = j.strip()[3:-1].split(",")
        particle.append([int(x) for x in k])
    particles.append(particle)

for l in range(1000):
    for i in range(len(particles)):
        for j in range(len(particles[i][1])):
            particles[i][1][j] += particles[i][2][j]
        for j in range(len(particles[i][0])):
            particles[i][0][j] += particles[i][1][j]

    collided = []
    for i in range(len(particles)):
        for j in range(i+1, len(particles)):
            if particles[i][0] == particles[j][0]:
                collided.append(particles[i])
                collided.append(particles[j])
    for i in collided:
        if i in particles:
            particles.remove(i)

print(len(particles))

# part 2: 574
