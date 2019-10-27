import simpy

def car(env):
    
    while True:
        print("start park at %d" % env.now)
        park = 5
        yield env.timeout(park)
        print("start driving at %d" % env.now)
        trip = 2
        yield env.timeout(trip)

env = simpy.Environment()
env.process(car(env))
env.run(until=14)
