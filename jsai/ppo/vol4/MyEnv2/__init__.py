from gym.envs.registration import register

register(
    id='SumoEnv-v0',
    entry_point='MyEnv2.env:SumoEnv'
)

register(
    id='SumoEnv2-v0',
    entry_point='MyEnv2.testenv:SumoEnv2'
)