from gym.envs.registration import register

register(
    id='SumoEnv-v0',
    entry_point='MyEnv.env:SumoEnv'
)

register(
    id='SumoEnv2-v0',
    entry_point='MyEnv.testenv:SumoEnv2'
)

