import math

def reward_function(params):
    reward = 1e-3
    tw = params['track_width']
    dfc = params['distance_from_center']
    speed = params['speed']
    sa = abs(params['steering_angle'])
    speed = params['speed']
    iot = params["is_offtrack"]
    awot = params['all_wheels_on_track']

    steps = params['steps']
    progress = params['progress']

    step_reward = (progress/steps)*8
    reward += step_reward

    if dfc <= 0.5:
        reward += (-2*abs(dfc)+tw+0.05)*1.2
    else:
        reward += 0.05

    if iot == True:
        if reward>1:
            reward-=1
        elif reward>2:
            reward-=1.5
        else:
            reward = 1e-3
    else:
        reward+=2

    if awot == True:
        reward += 0.2
    else:
        reward += 0.01
        
    if speed == 1:
        reward=reward*1.4
        reward += 1
    elif speed>0.9 and sa>15:
        reward += 0.5
    elif speed > 0.75:
        reward += 0.3
    else:
        reward += 0.01
    
    return float(reward)

params_dict = {
    'track_width': 1,
    'distance_from_center': 0.1,
    'speed':8,
    'steering_angle': 10,
    'is_offtrack': False,
    'all_wheels_on_track':False,
    'steps': 100,
    'progress': 1
}
    


def get_line_points(x1, y1, x2, y2, distance=0.2):
        dx = x2 - x1
        dy = y2 - y1
        line_length = math.sqrt(dx ** 2 + dy ** 2)
        num_points = int(line_length / distance) + 1
        x_steps = dx / (num_points - 1)
        y_steps = dy / (num_points - 1)
        line_points = [(x1 + i * x_steps, y1 + i * y_steps) for i in range(num_points)]
        return line_points
print(get_line_points(10,11,30,1))